from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from db_config.gino_connect import sess_db
from model.request.signin import SigninReq
from cqrs.signin.commands.update_handlers import UpdateSigninCommandHandler
from cqrs.signin.commands.create_handlers import AddSigninCommandHandler
from cqrs.signin.commands.delete_handlers import DeleteSigninCommandHandler
from cqrs.signin.query.query_handlers import ListSigninQueryHandler
from cqrs.signin.command import SigninCommand
from cqrs.signin.queries import SigninListQuery
from fastapi.security import OAuth2PasswordRequestForm
from jwt.secure import authenticate, create_access_token, get_current_user, get_password_hash
from datetime import timedelta
from model.request.tokens import Token

router = APIRouter(dependencies=[Depends(sess_db)])


# @router.post("/login_user/login", tags=['Login'] )
async def add_login_user(req: SigninReq): 
    handler = AddSigninCommandHandler()
    login_user_profile = dict()
    login_user_profile["username"] = req.username
    login_user_profile["password"] = req.password
    command = SigninCommand()
    command.details = login_user_profile
    result = await handler.handle(command)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'create login user profile problem encountered'}, status_code=500) 

# # @router.patch("/login_user/update/{username}", tags=['Login'])
# # async def update_user(username: str, req: SigninReq):
# #     login_user_dict = req.dict(exclude_unset=True)
# #     command = SigninCommand()
# #     command.details = {'username': username, **login_user_dict}
# #     handler = UpdateSigninCommandHandler()
# #     result = await handler.handle(command)
# #     if result:
# #         return req
# #     else:
# #         return JSONResponse(status_code=500, content="Update login user profile problem encountered")

# # @router.delete("/login_user/delete/{username}", tags=['Login'])
# # async def delete_user(username: str):
# #     command = SigninCommand()
# #     handler = DeleteSigninCommandHandler()
# #     command.details = {'username' : username}
# #     result = await handler.handle(command)
# #     if result:
# #         return {"message": "Profile deleted successfully"}
# #     else:
# #         return JSONResponse(status_code=500, content="Delete profile error")

# # @router.get("/login_user/list", tags=['Login'])
# # async def list_users(): 
# #     handler = ListSigninQueryHandler()
# #     query:SigninListQuery = await handler.handle() 
# #     return query.records

@router.post("/login_user/login_test", response_model=Token ,tags=['Login'] )
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    if await authenticate(username, password) == True:
        access_token = create_access_token(data={"sub": username}, expires_after=timedelta(minutes=20))
        signin_req = SigninReq(username=username, password=get_password_hash(password))
        await add_login_user(signin_req)
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password or you are not a registered user")

@router.get("/login_user/list_logon_users", tags=['Login'])
async def list_logon_users(current_user: dict = Depends(get_current_user)):
    handler = ListSigninQueryHandler()
    query: SigninListQuery = await handler.handle() 
    records = query.records
    return records

@router.get("/login_user/get_current_user", tags=['Login'])
async def get_current_user(current_user: dict = Depends(get_current_user)):
    return current_user
