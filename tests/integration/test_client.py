"""Test Client"""
from datetime import datetime, timedelta

from aiohttp.test_utils import unittest_run_loop

from tests.integration.utils import MetaServerTestCases


class ClientTestCases(MetaServerTestCases):

    @unittest_run_loop
    async def test_client_home(self):
        """Check Home Page"""
        resp = await self.client.get("/")

        self.assertEqual(200, resp.status)
        text = await resp.text()
        self.assertIn("How is there?", text)

    @unittest_run_loop
    async def test_client_questions_page(self):
        """Check Questions Page"""
        resp = await self.client.get("/questions")

        self.assertEqual(200, resp.status)
        text = await resp.text()
        # Check header
        self.assertIn("Question Text", text)
        self.assertIn("Publication Date", text)
        # Check fake content
        self.assertIn("Mega Psam", text)            # Text on the page
        self.assertNotIn("Mega Psam 1", text)       # Text not on the page
        date_on_page = (
            datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
        date_not_on_page = (
            datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        self.assertIn(date_on_page, text)
        self.assertNotIn(date_not_on_page, text)

    @unittest_run_loop
    async def test_client_choices_page(self):
        """Check Choices Page"""
        resp = await self.client.get("/choices")

        self.assertEqual(200, resp.status)
        text = await resp.text()
        # Check header
        self.assertIn("Question ID", text)
        self.assertIn("Choice Text", text)
        self.assertIn("Votes", text)
        # Check fake content
        self.assertIn("Spam_Choice_789", text)      # Text on the page
        self.assertNotIn("Spam_Choice_788", text)   # Text not on the page
