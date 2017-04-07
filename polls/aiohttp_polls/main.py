
import os

from aiohttp import web

from .routes import setup_routes
from .db import setup_db
from .jinja_cfg import setup_jinja
from ..libs.yaml_reader import YamlReader


conf_path = os.path.join(os.path.dirname(__file__), "../config/polls.yaml")
conf = YamlReader(conf_path)


def create_app(_conf, loop=None):

    app = web.Application(loop=loop)

    app["config"] = _conf
    setup_jinja(app)
    setup_db(app)
    setup_routes(app)

    return app
