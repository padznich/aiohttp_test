"""Test rendered views"""

import asyncio

import jinja2
import pytest
from aiohttp import web
from aiohttp.test_utils import make_mocked_request
import aiohttp_jinja2

from ..main import create_app, conf


async def test_home_view(loop, test_client):

    app = create_app(conf, loop)

    client = await test_client(app)

    resp = await client.get("/")

    assert 200 == resp.status
    text = await resp.text()
    assert "How is there?" in text


async def test_questions_view(loop, test_client):

    app = create_app(conf, loop)

    client = await test_client(app)

    resp = await client.get("/questions")

    assert 200 == resp.status
    text = await resp.text()
    # assert "How is there?" in text
