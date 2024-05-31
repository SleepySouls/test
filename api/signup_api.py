from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db_config.gino_connect import sess_db
from model.request.signup import SignupReq
from cqrs.signup.commands.update_handlers import UpdateSignupCommandHandler
from cqrs.signup.commands.create_handlers import AddSignupCommandHandler
from cqrs.signup.commands.delete_handlers import DeleteSignupCommandHandler
from cqrs.signup.query.query_handlers import ListSignupQueryHandler
from cqrs.signup.command import SignupCommand
from cqrs.signup.queries import SignupListQuery
from jwt.secure import get_password_hash

    
router = APIRouter(dependencies=[Depends(sess_db)])


@router.post("/signup/add", tags=['Signup'] )
async def add_signup_user(req: SignupReq): 
    handler = AddSignupCommandHandler()
    signup_user_profile = dict()
    signup_user_profile["id"] = req.id
    signup_user_profile["username"] = req.username
    signup_user_profile["password"] = get_password_hash(req.password)
    signup_user_profile["email"] = req.email
    signup_user_profile["first_name"] = req.first_name
    signup_user_profile["last_name"] = req.last_name
    signup_user_profile["role"] = req.role
    command = SignupCommand()
    command.details = signup_user_profile
    result = await handler.handle(command)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'create signup user profile problem encountered'}, status_code=500) 

@router.patch("/signup/update/{id}", tags=['Signup'])
async def update_signup_user(id: int, req: SignupReq):
    login_user_dict = req.dict(exclude_unset=True)
    command = SignupCommand()
    command.details = {'id': id, **login_user_dict}
    handler = UpdateSignupCommandHandler()
    result = await handler.handle(command)
    if result:
        return req
    else:
        return JSONResponse(status_code=500, content="Update signup user profile problem encountered")

@router.delete("/signup/delete/{id}", tags=['Signup'])
async def delete_signup_user(id: int):
    command = SignupCommand()
    handler = DeleteSignupCommandHandler()
    command.details = {'id' : id}
    result = await handler.handle(command)
    if result:
        return {"message": "Profile deleted successfully"}
    else:
        return JSONResponse(status_code=500, content="Delete profile error")

@router.get("/signup/list", tags=['Signup'])
async def list_signup_users(): 
    handler = ListSignupQueryHandler()
    query:SignupListQuery = await handler.handle() 
    return query.records

