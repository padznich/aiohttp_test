"""Test Fake Db"""
from aiohttp.test_utils import unittest_run_loop

from tests.integration.utils import MetaServerTestCases

import polls


class FakeDbTestCases(MetaServerTestCases):

    @unittest_run_loop
    async def test_db_question(self):
        db = polls.db.Session()
        q = db.query(polls.models.Question)
        penault_question = q.get(5)
        assert penault_question

    @unittest_run_loop
    async def test_db_choice(self):
        db = polls.db.Session()
        c = db.query(polls.models.Choice)
        penault_choice = c.get(3)
        assert penault_choice
