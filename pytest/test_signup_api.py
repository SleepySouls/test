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
async def test_add_signup():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/test/signup/add", json={
            "id": 1,
            "username": "testuser",
            "password": "testpass",
            "email": "liberosis123@gmail.com",
            "first_name": "liberosis",
            "last_name": "silent",
            "role": "donator"
        })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "username": "testuser",
        "password": "testpass",
        "email": "liberosis123@gmail.com",
        "first_name": "liberosis",
        "last_name": "silent",
        "role": "donator"
    }

@pytest.mark.asyncio
async def test_update_signup():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.patch("/test/signup/update/1", json={
            "id": 1,
            "username": "updateuser",
            "password": "updatepass",
            "email": "liberosis123@gmail.com",
            "first_name": "silent liberosis",
            "last_name": "liberosis silent",
            "role": "admin"
        })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "username": "updateuser",
        "password": "updatepass",
        "email": "liberosis123@gmail.com",
        "first_name": "silent liberosis",
        "last_name": "liberosis silent",
        "role": "admin"
    }

@pytest.mark.asyncio
async def test_delete_signup():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/test/signup/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Profile deleted successfully"}

@pytest.mark.asyncio
async def test_list_signup():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test/signup/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)