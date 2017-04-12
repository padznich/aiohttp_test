from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import Integer, Text
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(Text)
    pub_date = Column(DateTime, nullable=False, default=datetime.now)


class Choice(Base):
    __tablename__ = "choice"
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey("question.id"))
    choice_text = Column(Text)
    votes = Column(Integer)
