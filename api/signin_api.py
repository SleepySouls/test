from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from db_config.gino_connect import sess_db
from model.request.signin import SigninReq
from sqlalchemy.orm import Session
from cqrs.signin.commands.update_handlers import UpdateSigninCommandHandler
from cqrs.signin.commands.create_handlers import AddSigninCommandHandler
from cqrs.signin.commands.delete_handlers import DeleteSigninCommandHandler
from cqrs.signin.query.query_handlers import ListSigninQueryHandler
from cqrs.signin.command import SigninCommand
from cqrs.signin.queries import SigninListQuery
from fastapi.security import OAuth2PasswordRequestForm
from repository.signup_repo import SignupRepository
from jwt.secure import authenticate, create_access_token, get_current_user, get_password_hash
from datetime import timedelta
from cqrs.signup.query.query_handlers import ListSignupQueryHandler
from cqrs.signup.queries import SignupListQuery

router = APIRouter(dependencies=[Depends(sess_db)])


@router.post("/login_user/login", tags=['Login'] )
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

# @router.patch("/login_user/update/{id}", tags=['Login'])
# async def update_user(id: int, req: SigninReq):
#     login_user_dict = req.dict(exclude_unset=True)
#     command = SigninCommand()
#     command.details = {'id': id, **login_user_dict}
#     handler = UpdateSigninCommandHandler()
#     result = await handler.handle(command)
#     if result:
#         return req
#     else:
#         return JSONResponse(status_code=500, content="Update login user profile problem encountered")

# @router.delete("/login_user/delete/{id}", tags=['Login'])
# async def delete_user(id: int):
#     command = SigninCommand()
#     handler = DeleteSigninCommandHandler()
#     command.details = {'id' : id}
#     result = await handler.handle(command)
#     if result:
#         return {"message": "Profile deleted successfully"}
#     else:
#         return JSONResponse(status_code=500, content="Delete profile error")

# @router.get("/login_user/list", tags=['Login'])
# async def list_users(): 
#     handler = ListSigninQueryHandler()
#     query:SigninListQuery = await handler.handle() 
#     return query.records

@router.post("/login_user/login_test", tags=['Login'] )
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


# @router.post("/login_user/add", tags=['Login'])
# async def add_user(req: SigninReq): 
#     handler = AddSigninCommandHandler()
#     login_user_profile = {
#         # "id": req.id,
#         "username": req.username,
#         "password": get_password_hash(req.password)  # Hash the password before storing it
#     }
#     command = SigninCommand()
#     command.details = login_user_profile
#     result = await handler.handle(command)
#     if result:
#         # Create JWT token for the new user
#         access_token_expires = timedelta(minutes=30)
#         access_token = create_access_token(
#             data={"sub": req.username}, expires_after=access_token_expires
#         )
#         return {"access_token": access_token, "token_type": "bearer"}
#     else:
#         return JSONResponse(content={'message': 'Create login user profile problem encountered'}, status_code=500)

# @router.patch("/login_user/update/{id}", tags=['Login'])
# async def update_user(id: int, req: SigninReq, current_user: SigninReq = Depends(get_current_user)):
#     login_user_dict = req.dict(exclude_unset=True)
#     command = SigninCommand()
#     command.details = {'id': id, **login_user_dict}
#     handler = UpdateSigninCommandHandler()
#     result = await handler.handle(command)
#     if result:
#         return req
#     else:
#         return JSONResponse(status_code=500, content="Update login user profile problem encountered")

# @router.delete("/login_user/delete/{id}", tags=['Login'])
# async def delete_user(id: int, current_user: SigninReq = Depends(get_current_user)):
#     command = SigninCommand()
#     handler = DeleteSigninCommandHandler()
#     command.details = {'id': id}
#     result = await handler.handle(command)
#     if result:
#         return {"message": "Profile deleted successfully"}
#     else:
#         return JSONResponse(status_code=500, content="Delete profile error")

# @router.get("/login_user/list", tags=['Login'])
# async def list_users(current_user: SigninReq = Depends(get_current_user)):
#     handler = ListSigninQueryHandler()
#     query: SigninListQuery = await handler.handle()
#     return query.records

@router.get("/login_user/list", tags=['Login'])
async def list_users(current_user: SigninReq = Depends(get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    handler = ListSigninQueryHandler()
    query: SigninListQuery = await handler.handle()
    return query.records