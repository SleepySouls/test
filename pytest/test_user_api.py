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
async def test_add_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/test/user/add", json={
            "user_id": 1,
            "email": "liberosis123@gmail.com",
            "first_name": "liberosis",
            "last_name": "silent",
            "role": "donator"
        })
    assert response.status_code == 200
    assert response.json() == {
        "user_id": 1,
        "email": "liberosis123@gmail.com",
        "first_name": "liberosis",
        "last_name": "silent",
        "role": "donator"
    }

@pytest.mark.asyncio
async def test_update_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.patch("/test/user/update/1", json={
            "user_id": 1,
            "email": "silent123@gmail.com",
            "first_name": "silent liberosis",
            "last_name": "liberosis silent",
            "role": "user"
        })
    assert response.status_code == 200
    assert response.json() == {
        "user_id": 1,
        "email": "silent123@gmail.com",
        "first_name": "silent liberosis",
        "last_name": "liberosis silent",
        "role": "user"
    }

@pytest.mark.asyncio
async def test_delete_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/test/user/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted successfully"}

@pytest.mark.asyncio
async def test_list_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test/user/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)