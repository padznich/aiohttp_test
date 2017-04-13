"""Integration Tests Utils"""
from datetime import datetime, timedelta
from unittest import mock

from aiohttp.test_utils import AioHTTPTestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from polls.models import Choice, Question, Base
from polls.main import create_app
from settings import conf


_e = "postgresql"
test_db_name = "test_postgres"
test_db_url = "{_e}://{user}:{passw}@{host}:{port}/{db_name}".format(
    _e=_e,
    user=conf.database["user"],
    passw=conf.database["password"],
    host=conf.database["host"],
    port=conf.database["port"],
    db_name=test_db_name,
)


def fill_db():
    # engine
    e = create_engine(
        test_db_url,
        echo=False,
        pool_size=100,
        max_overflow=200
    )
    # session
    session = sessionmaker(autoflush=False)
    session.configure(bind=e)
    s = session()
    questions = (
        ("Spam", datetime.now()),
        ("Spam", datetime.now() - timedelta(days=1)),
        ("Spam", datetime.now() - timedelta(days=2)),
        ("Mega Psam", datetime.now() - timedelta(days=3)),
        ("Right Psam Check", datetime.now() - timedelta(days=4)),
        ("Psam", datetime.now() - timedelta(days=5)),
    )
    choices = (
        (1, "Spam Choice 007", 3),
        (2, "Spam_Choice_789", 7),
        (3, "Right Spam Choice 10", 23),
        (4, "Spam Choice Oooo", 983),
    )
    Base.metadata.drop_all(e)
    Base.metadata.create_all(e)

    for q in questions:
        s.add(Question(
            question_text=q[0],
            pub_date=q[1]
        ))
    s.commit()
    s = session()

    for i, c in enumerate(choices):
        for j in range(4):
            s.add(Choice(
                question_id=c[0],
                choice_text=c[1],
                votes=c[2] + i + j * 2,
            ))
    s.commit()


class MetaServerTestCases(AioHTTPTestCase):

    @classmethod
    def setUpClass(cls):
        # mock database
        cls.fake_engine = create_engine(
            test_db_url,
            echo=False,
            pool_size=100,
            max_overflow=200
        )
        cls.fake_session = sessionmaker(bind=cls.fake_engine, autoflush=True)
        cls.mock_session = mock.patch("polls.db.Session", cls.fake_session)
        cls.mock_session.start()
        # Create DB if not exists
        if not database_exists(cls.fake_engine.url):
            create_database(cls.fake_engine.url)
        # create database
        Base.metadata.drop_all(cls.fake_engine)
        Base.metadata.create_all(cls.fake_engine)
        # fill database with test data
        fill_db()
        # integration_test_data()

    @classmethod
    def tearDownClass(cls):
        # print(dir(cls.fake_session))
        # cls.mock_session.boom()
        Base.metadata.drop_all(cls.fake_engine)
        cls.mock_session.stop()

    def get_app(self):
        # Switch Original_Db to Fake_Db
        conf.database["database"] = test_db_name
        app = create_app()
        app["config"] = conf
        return app
