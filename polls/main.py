
from aiohttp import web
import asyncio

from .routes import setup_routes
from .db import setup_db
from .jinja_cfg import setup_jinja


def create_app(_conf, loop=None):

    if not loop:
        loop = asyncio.get_event_loop()

    app = web.Application(loop=loop)

    app["config"] = _conf
    setup_jinja(app)
    setup_db(app)
    setup_routes(app)

    return app
