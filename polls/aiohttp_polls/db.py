
import sqlalchemy as sa
from aiopg.sa import create_engine


meta = sa.MetaData()

question = sa.Table(
    "question", meta,
    sa.Column("id", sa.Integer, nullable=False),
    sa.Column("question_text", sa.String(200), nullable=False),
    sa.Column("pub_date", sa.Date, nullable=False),

    # Indexes #
    sa.PrimaryKeyConstraint("id", name="question_id_pkey")
)

choice = sa.Table(
    "choice", meta,
    sa.Column("id", sa.Integer, nullable=False),
    sa.Column("question_id", sa.Integer, nullable=False),
    sa.Column("choice_text", sa.String(200), nullable=False),
    sa.Column("votes", sa.Integer, server_default="0", nullable=False),

    # Indexes #
    sa.PrimaryKeyConstraint("id", name="choice_id_pkey"),
    sa.ForeignKeyConstraint(["question_id"], [question.c.id],
                            name="choice_question_id_fkey",
                            ondelete="CASCADE"),
)


def setup_db(app):

    # DB initializing
    async def init_pg(app):
        database = app["config"].database
        engine = await create_engine(loop=app.loop, **database)
        app["db"] = engine

    # Graceful shutdown
    async def close_pg(app):
        app["db"].close()
        await app["db"].wait_closed()

    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
