#!/usr/bin/ python3

import asyncio

from polls.aiohttp_polls.main import create_app, conf

loop = asyncio.get_event_loop()
app = create_app(conf, loop=loop)
