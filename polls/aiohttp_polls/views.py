
from aiohttp import web
import aiohttp_jinja2

from .db import question, choice


class Home(web.View):

    async def get(self):
        context = {}
        return aiohttp_jinja2.render_template("home.html",
                                              self.request,
                                              context)


class Question(web.View):

    async def get(self):
        questions = []
        async with self.request.app["db"].acquire() as conn:
            async for row in conn.execute(question.select()):
                questions.append(row)
        context = {"questions": questions}
        return aiohttp_jinja2.render_template("questions.html",
                                              self.request,
                                              context)


class Choice(web.View):

    async def get(self):
        choices = []
        async with self.request.app["db"].acquire() as conn:
            async for row in conn.execute(choice.select()):
                choices.append(row)
        context = {"choices": choices}
        return aiohttp_jinja2.render_template("choices.html",
                                              self.request,
                                              context)
