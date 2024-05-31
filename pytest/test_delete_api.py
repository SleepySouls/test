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
async def test_delete_donation():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/test/donation/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Donation deleted successfully"}

@pytest.mark.asyncio
async def test_delete_newsfeed():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/test/newsfeed/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Newsfeed deleted successfully"}

@pytest.mark.asyncio
async def test_delete_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/test/user/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted successfully"}

@pytest.mark.asyncio
async def test_delete_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/test/login_user/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Profile deleted successfully"}

@pytest.mark.asyncio
async def test_delete_signup():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/test/signup/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Profile deleted successfully"}