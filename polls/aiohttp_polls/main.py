
import os

import aiohttp_jinja2
from aiohttp import web
import jinja2

from .routes import setup_routes
from .db import setup_db
from ..libs.yaml_reader import YamlReader


conf_path = os.path.join(os.path.dirname(__file__), "../config/polls.yaml")
conf = YamlReader(conf_path)


def create_app(_conf, loop=None):

    app = web.Application(loop=loop)

    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader("polls/aiohttp_polls/templates/")
    )

    app["config"] = _conf
    setup_db(app)
    setup_routes(app)

    return app
