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
async def test_add_campaign():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/test/campaign/add", json={
            "campaign_id": 1,
            "title": "test campaign",
            "description": "this is the test",
            "goal_amount": 100000,
            "raised_amount": 12345,
            "start_date": "2024-05-12",
            "end_date": "2024-05-30",
            "category": "veteran",
            "media": "http://127.0.0.1:8000/docs#/Campaign/add_campaign_test_campaign_add_post",
            "status": "incomplete"
        })
    assert response.status_code == 200
    assert response.json() == {
        "campaign_id": 1, 
        "title": "test campaign", 
        "description": "this is the test",
        "goal_amount": 100000,
        "raised_amount": 12345,
        "start_date": "2024-05-12",
        "end_date": "2024-05-30", 
        "category": "veteran",
        "media": "http://127.0.0.1:8000/docs#/Campaign/add_campaign_test_campaign_add_post", 
        "status": "incomplete"
    }

@pytest.mark.asyncio
async def test_update_campaign():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.patch("/test/campaign/update/1", json={
            "campaign_id": 1,
            "title": "test campaign",
            "description": "this is the test of update",
            "goal_amount": 200000,
            "raised_amount": 123456,
            "start_date": "2024-05-12",
            "end_date": "2024-06-01",
            "category": "veteran",
            "media": "http://127.0.0.1:8000/docs#/Campaign/add_campaign_test_campaign_add_post",
            "status": "incomplete"
        })
    assert response.status_code == 200
    assert response.json() == {
        "campaign_id": 1,
            "title": "test campaign",
            "description": "this is the test of update",
            "goal_amount": 200000,
            "raised_amount": 123456,
            "start_date": "2024-05-12",
            "end_date": "2024-06-01",
            "category": "veteran",
            "media": "http://127.0.0.1:8000/docs#/Campaign/add_campaign_test_campaign_add_post",
            "status": "incomplete"
    }

@pytest.mark.asyncio
async def test_delete_campaign():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/test/campaign/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Campaign deleted successfully"}

@pytest.mark.asyncio
async def test_list_campaign():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test/campaign/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)