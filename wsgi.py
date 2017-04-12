#!/usr/bin/ python3

import asyncio

from polls.main import create_app
from settings import conf

loop = asyncio.get_event_loop()
app = create_app(conf, loop=loop)
