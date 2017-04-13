"""Test Db"""
from datetime import datetime, timedelta
from aiohttp.test_utils import unittest_run_loop

from tests.integration.utils import MetaServerTestCases

import polls


class DbTestCases(MetaServerTestCases):

    @unittest_run_loop
    async def test_question_select(self):
        """Check Question Table SELECT"""
        s = polls.db.Session()
        q = s.query(polls.models.Question)
        penault_question = q.get(5)
        self.assertIsNotNone(penault_question)

    @unittest_run_loop
    async def test_choice_select(self):
        """Check Choice Table SELECT"""
        s = polls.db.Session()
        c = s.query(polls.models.Choice)
        penault_choice = c.get(3)
        self.assertIsNotNone(penault_choice)

    @unittest_run_loop
    async def test_question_insert(self):
        """Check Question Table Writing"""
        s = polls.db.Session()
        q = s.query(polls.models.Question)
        q_before = q.count()
        s.add(polls.models.Question(
            question_text="Self Written",
            pub_date=datetime.now() - timedelta(days=15)
        ))
        s.commit()

        q_after = q.count()
        self.assertGreater(q_after, q_before)

    @unittest_run_loop
    async def test_choice_insert(self):
        """Check Choice Table Writing"""
        s = polls.db.Session()
        c = s.query(polls.models.Choice)
        c_before = c.count()
        s.add(polls.models.Choice(
            question_id=1,
            choice_text="Self Written",
            votes=90
        ))
        s.commit()

        c_after = c.count()
        self.assertGreater(c_after, c_before)
