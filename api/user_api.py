from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db_config.gino_connect import sess_db
from model.request.user import UserReq
from cqrs.user.commands.update_handlers import UpdateUserCommandHandler
from cqrs.user.commands.create_handlers import AddUserCommandHandler
from cqrs.user.commands.delete_handlers import DeleteUserCommandHandler
from cqrs.user.query.query_handlers import ListUserQueryHandler
from cqrs.user.command import UserCommand
from cqrs.user.queries import UserListQuery
from jwt.secure import get_current_user
    
router = APIRouter(dependencies=[Depends(sess_db)])


@router.post("/user/add", tags=['User'] )
async def add_user(req: UserReq, current_user: dict = Depends(get_current_user)): 
    handler = AddUserCommandHandler()
    user_profile = dict()
    user_profile["user_id"] = req.user_id
    user_profile["email"] = req.email
    user_profile["first_name"] = req.first_name
    user_profile["last_name"] = req.last_name
    user_profile["role"] = req.role
    command = UserCommand()
    command.details = user_profile
    result = await handler.handle(command)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'create trainer profile problem encountered'}, status_code=500) 

@router.patch("/user/update/{id}", tags=['User'])
async def update_user(id: int, req: UserReq, current_user: dict = Depends(get_current_user)):
    user_dict = req.dict(exclude_unset=True)
    command = UserCommand()
    command.details = {'id': id, **user_dict}
    handler = UpdateUserCommandHandler()
    result = await handler.handle(command)
    if result:
        return req
    else:
        return JSONResponse(status_code=500, content="Update trainer profile problem encountered")

@router.delete("/user/delete/{id}", tags=['User'])
async def delete_user(id: int, current_user: dict = Depends(get_current_user)):
    command = UserCommand()
    handler = DeleteUserCommandHandler()
    command.details = {'id' : id}
    result = await handler.handle(command)
    if result:
        return {"message": "User deleted successfully"}
    else:
        return JSONResponse(status_code=500, content="Delete profile error")

@router.get("/user/list", tags=['User'])
async def list_users(current_user: dict = Depends(get_current_user)): 
    handler = ListUserQueryHandler()
    query:UserListQuery = await handler.handle() 
    return query.records

