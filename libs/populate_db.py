"""Test DB"""

from aiopg.sa import create_engine


async def populate_question(dsn, question):
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            await conn.execute(
                question.insert().values(
                    question_text='abc', pub_date='2017-01-01'
                )
            )
            await conn.execute(
                question.insert().values(
                    question_text='def', pub_date='2017-01-02'
                )
            )
            await conn.execute(
                question.insert().values(
                    question_text='ghi', pub_date='2017-01-03'
                )
            )
        count = await conn.scalar(question.count())
        print('populated table with {} items'.format(count))
