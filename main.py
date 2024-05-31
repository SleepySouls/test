from fastapi import FastAPI
from api import signin_api, campaign_api, donation_api, user_api, newsfeed_api, signup_api

app = FastAPI()


app.include_router(signin_api.router, prefix='/test')
app.include_router(signup_api.router, prefix='/test')
# app.include_router(campaign_api.router, prefix='/test')
# app.include_router(donation_api.router, prefix='/test')
# app.include_router(user_api.router, prefix='/test')
# app.include_router(newsfeed_api.router, prefix='/test')