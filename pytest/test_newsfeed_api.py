import pytest
from httpx import AsyncClient
from main import app
import sys
import asyncio
import pytest

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@pytest.fixture
def anyio_backend():
    return 'asyncio'

@pytest.mark.asyncio
async def test_add_newsfeed():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/test/newsfeed/add", json={
            "newsfeed_id": 1,
            "author": "test newsfeed",
            "headline": "this is the test",
            "summary": "This is the test of newsfeed's summary",
            "media": "http://127.0.0.1:8000/docs#/Newsfeed/add_newsfeed_test_newsfeed_add_post",
            "publish_date": "2024-05-12",
            "category": "veteran",
            "author_id": 1,
        })
    assert response.status_code == 200
    assert response.json() == {
        "newsfeed_id": 1,
        "author": "test newsfeed",
        "headline": "this is the test",
        "summary": "This is the test of newsfeed's summary",
        "media": "http://127.0.0.1:8000/docs#/Newsfeed/add_newsfeed_test_newsfeed_add_post",
        "publish_date": "2024-05-12",
        "category": "veteran",
        "author_id": 1,
    }

@pytest.mark.asyncio
async def test_update_newsfeed():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.patch("/test/newsfeed/update/1", json={
            "newsfeed_id": 1,
            "author": "test update newsfeed",
            "headline": "this is the test of update newsfeed",
            "summary": "This is the test of update newsfeed's summary",
            "media": "http://127.0.0.1:8000/docs#/Newsfeed/add_newsfeed_test_newsfeed_add_post",
            "publish_date": "2024-05-13",
            "category": "children",
            "author_id": 1,
        })
    assert response.status_code == 200
    assert response.json() == {
        "newsfeed_id": 1,
        "author": "test update newsfeed",
        "headline": "this is the test of update newsfeed",
        "summary": "This is the test of update newsfeed's summary",
        "media": "http://127.0.0.1:8000/docs#/Newsfeed/add_newsfeed_test_newsfeed_add_post",
        "publish_date": "2024-05-13",
        "category": "children",
        "author_id": 1,
    }

@pytest.mark.asyncio
async def test_delete_newsfeed():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/test/newsfeed/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Newsfeed deleted successfully"}

@pytest.mark.asyncio
async def test_list_newsfeed():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test/newsfeed/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)