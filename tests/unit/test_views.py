"""Unit Tests"""

from polls.main import create_app


async def test_home_view(loop, test_client):

    app = create_app()

    client = await test_client(app)

    resp = await client.get("/")

    assert 200 == resp.status
    text = await resp.text()
    assert "How is there?" in text


async def test_questions_view(loop, test_client):

    app = create_app()

    client = await test_client(app)

    resp = await client.get("/questions")

    assert 200 == resp.status
    text = await resp.text()
    assert "Question Text" in text
    assert "Publication Date" in text


async def test_chices_view(loop, test_client):

    app = create_app()

    client = await test_client(app)

    resp = await client.get("/choices")

    assert 200 == resp.status
    text = await resp.text()
    assert "Question ID" in text
    assert "Choice Text" in text
    assert "Votes" in text
