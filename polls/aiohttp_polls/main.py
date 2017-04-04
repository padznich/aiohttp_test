
import asyncio
import os
import aiohttp_jinja2
import jinja2

from aiohttp import web

from .routes import setup_routes
from .db import setup_db
from ..libs.yaml_reader import YamlReader


conf_path = os.path.join(os.path.dirname(__file__), "../config/polls.yaml")
conf = YamlReader(conf_path)
project_root = os.path.join(os.path.dirname(__file__), "../")


loop = asyncio.get_event_loop()
app = web.Application(loop=loop)

aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader('polls')
)

app["config"] = conf
setup_db(app)
setup_routes(app)


if __name__ == "__main__":
    web.run_app(app, host='0.0.0.0', port=8080)
