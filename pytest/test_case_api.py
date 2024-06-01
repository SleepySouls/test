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

#create signup
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

#list signup
@pytest.mark.asyncio
async def test_list_signup():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test/signup/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

#update signup
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

#create login
@pytest.mark.asyncio
async def test_add_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/test/login_user/add", json={
            "username": "testuser",
            "password": "testpass"
        })
    assert response.status_code == 200
    assert response.json() == {
        "username": "testuser",
        "password": "testpass"
    }

#list login
@pytest.mark.asyncio
async def test_list_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test/login_user/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


#update login
@pytest.mark.asyncio
async def test_update_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.patch("/test/login_user/update/1", json={
            "username": "updateduser",
            "password": "updatedpass"
        })
    assert response.status_code == 200
    assert response.json() == {
        "username": "updateduser",
        "password": "updatedpass"
    }

#create user
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

#list user
@pytest.mark.asyncio
async def test_list_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test/user/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

#update user
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

#create newsfeed
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

#update newsfeed
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

#list newsfeed
@pytest.mark.asyncio
async def test_list_newsfeed():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test/newsfeed/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

#create campaign
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

#update campaign
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

#list campaign
@pytest.mark.asyncio
async def test_list_campaign():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test/campaign/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

#create donation
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

#update donation
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

#list donation
@pytest.mark.asyncio
async def test_list_donation():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test/donation/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

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