"""Test Client"""
from datetime import datetime, timedelta

from aiohttp.test_utils import unittest_run_loop

from tests.integration.utils import MetaServerTestCases


class ClientTestCases(MetaServerTestCases):

    @unittest_run_loop
    async def test_client_home(self):

        resp = await self.client.get("/")

        assert 200 == resp.status
        text = await resp.text()
        assert "How is there?" in text

    @unittest_run_loop
    async def test_client_questions_page(self):

        resp = await self.client.get("/questions")

        assert 200 == resp.status
        text = await resp.text()
        # Check header
        assert "Question Text" in text
        assert "Publication Date" in text
        # Check fake content
        assert "Mega Psam" in text           # Text on the page
        assert "Mega Psam 1" not in text     # Text not on the page
        date_on_page = (
            datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
        date_not_on_page = (
            datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        assert date_on_page in text
        assert date_not_on_page not in text

    @unittest_run_loop
    async def test_client_choices_page(self):

        resp = await self.client.get("/choices")

        assert 200 == resp.status
        text = await resp.text()
        # Check header
        assert "Question ID" in text
        assert "Choice Text" in text
        assert "Votes" in text
        # Check fake content
        assert "Spam_Choice_789" in text        # Text on the page
        assert "Spam_Choice_788" not in text    # Text not on the page
