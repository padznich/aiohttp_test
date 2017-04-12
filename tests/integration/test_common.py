from aiohttp.test_utils import unittest_run_loop

from tests.integration.utils import MetaServerTestCases


class CommonTestCases(MetaServerTestCases):
    @unittest_run_loop
    async def test_home(self):
        """Check / """
        response = await self.client.get(
            "/",
        )
        self.assertEqual(response.status, 200)
