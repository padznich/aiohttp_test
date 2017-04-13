
from aiohttp import web

from .routes import setup_routes
from .db import setup_db
from .jinja_cfg import setup_jinja
from settings import conf


def create_app(**kwargs):

    app = web.Application(**kwargs)

    app["config"] = conf
    setup_jinja(app)
    setup_db(app)
    setup_routes(app)

    return app
