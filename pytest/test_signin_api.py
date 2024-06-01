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
async def test_add_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/test/login_user/login", json={
            "username": "testuser",
            "password": "testpass"
        })
    assert response.status_code == 200
    assert response.json() == {
        "username": "testuser",
        "password": "testpass"
    }

@pytest.mark.asyncio
async def test_update_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.patch("/test/login_user/update/testuser", json={
            "username": "testuser",
            "password": "updatedpass"
        })
    assert response.status_code == 200
    assert response.json() == {
        "username": "testuser",
        "password": "updatedpass"
    }

@pytest.mark.asyncio
async def test_delete_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/test/login_user/delete/testuser")
    assert response.status_code == 200
    assert response.json() == {"message": "Profile deleted successfully"}

@pytest.mark.asyncio
async def test_list_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test/login_user/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
