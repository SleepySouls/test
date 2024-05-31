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
async def test_add_donation():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/test/donation/add", json={
            "donation_id": 1,
            "campaign_id": 1, 
            "donator_id": 1,
            "donation_amount": 100000,
            "donation_date": "2024-05-12",
            "message_leaving": "Hope you will have a good test"
        })
    assert response.status_code == 200
    assert response.json() == {
        "donation_id": 1,
        "campaign_id": 1, 
        "donator_id": 1,
        "donation_amount": 100000,
        "donation_date": "2024-05-12",
        "message_leaving": "Hope you will have a good test"
    }

@pytest.mark.asyncio
async def test_update_donation():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.patch("/test/donation/update/1", json={
            "donation_id": 1,
            "campaign_id": 1, 
            "donator_id": 1,
            "donation_amount": 200000,
            "donation_date": "2024-05-13",
            "message_leaving": "Hope you will have a good update test"
        })
    assert response.status_code == 200
    assert response.json() == {
        "donation_id": 1,
        "campaign_id": 1, 
        "donator_id": 1,
        "donation_amount": 200000,
        "donation_date": "2024-05-13",
        "message_leaving": "Hope you will have a good update test"
    }

@pytest.mark.asyncio
async def test_delete_donation():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/test/donation/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Donation deleted successfully"}

@pytest.mark.asyncio
async def test_list_donation():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test/donation/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)