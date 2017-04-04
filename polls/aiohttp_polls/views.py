
import aiohttp_jinja2

from .db import question, choice


@aiohttp_jinja2.template('aiohttp_polls/templates/home.html')
async def index(request):
    return


@aiohttp_jinja2.template('aiohttp_polls/templates/questions.html')
async def questions_handler(request):
    questions = []
    async with request.app['db'].acquire() as conn:
        async for row in conn.execute(question.select()):
            questions.append(row)
    return {'questions': questions}


@aiohttp_jinja2.template('aiohttp_polls/templates/choices.html')
async def choices_handler(request):
    choices = []
    async with request.app['db'].acquire() as conn:
        async for row in conn.execute(choice.select()):
            choices.append(row)
    return {'choices': choices}
