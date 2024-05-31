from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db_config.gino_connect import sess_db
from model.request.newsfeed import NewsfeedReq
from cqrs.newsfeed.commands.update_handlers import UpdateNewsfeedCommandHandler
from cqrs.newsfeed.commands.create_handlers import AddNewsfeedCommandHandler
from cqrs.newsfeed.commands.delete_handlers import DeleteNewsfeedCommandHandler
from cqrs.newsfeed.query.query_handlers import ListNewsfeedQueryHandler
from cqrs.newsfeed.command import NewsfeedCommand
from cqrs.newsfeed.queries import NewsfeedListQuery


router = APIRouter(dependencies=[Depends(sess_db)])


@router.post("/newsfeed/add", tags=['Newsfeed'])
async def add_newsfeed(req: NewsfeedReq): 
    handler = AddNewsfeedCommandHandler()
    newsfeed_profile = dict()
    newsfeed_profile["newsfeed_id"] = req.newsfeed_id
    newsfeed_profile["author"] = req.author
    newsfeed_profile["headline"] = req.headline
    newsfeed_profile["summary"] = req.summary
    newsfeed_profile["media"] = req.media
    newsfeed_profile["publish_date"] = req.publish_date
    newsfeed_profile["category"] = req.category
    newsfeed_profile["author_id"] = req.author_id
    command = NewsfeedCommand()
    command.details = newsfeed_profile
    result = await handler.handle(command)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'create newsfeed problem encountered'}, status_code=500) 

@router.patch("/newsfeed/update/{id}", tags=['Newsfeed'])
async def update_newsfeed(id: int, req: NewsfeedReq):
    newsfeed_dict = req.dict(exclude_unset=True)
    command = NewsfeedCommand()
    command.details = {'id': id, **newsfeed_dict}
    handler = UpdateNewsfeedCommandHandler()
    result = await handler.handle(command)
    if result:
        return req
    else:
        return JSONResponse(status_code=500, content="Update newsfeed problem encountered")

@router.delete("/newsfeed/delete/{id}", tags=['Newsfeed'])
async def delete_newsfeed(id: int):
    command = NewsfeedCommand()
    handler = DeleteNewsfeedCommandHandler()
    command.details = {'id' : id}
    result = await handler.handle(command)
    if result:
        return {"message": "Newsfeed deleted successfully"}
    else:
        return JSONResponse(status_code=500, content="Delete newsfeed error")

@router.get("/newsfeed/list", tags=['Newsfeed'])
async def list_newsfeeds(): 
    handler = ListNewsfeedQueryHandler()
    query:NewsfeedListQuery = await handler.handle() 
    return query.records

