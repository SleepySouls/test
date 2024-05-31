from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db_config.gino_connect import sess_db
from model.request.campaign import CampaignReq
from cqrs.campaign.commands.update_handlers import UpdateCampaignCommandHandler
from cqrs.campaign.commands.create_handlers import AddCampaignCommandHandler
from cqrs.campaign.commands.delete_handlers import DeleteCampaignCommandHandler
from cqrs.campaign.query.query_handlers import ListCampaignQueryHandler
from cqrs.campaign.command import CampaignCommand
from cqrs.campaign.queries import CampaignListQuery
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.secure import oauth2_scheme, get_current_user
    
router = APIRouter(dependencies=[Depends(sess_db)])


@router.post("/campaign/add", tags = ['Campaign'])
async def add_campaign(req: CampaignReq): 
    handler = AddCampaignCommandHandler()
    campaign_profile = dict()
    campaign_profile["campaign_id"] = req.campaign_id
    campaign_profile["title"] = req.title
    campaign_profile["description"] = req.description
    campaign_profile["goal_amount"] = req.goal_amount
    campaign_profile["raised_amount"] = req.raised_amount
    campaign_profile["start_date"] = req.start_date
    campaign_profile["end_date"] = req.end_date
    campaign_profile["category"] = req.category
    campaign_profile["media"] = req.media
    campaign_profile["status"] = req.status
    command = CampaignCommand()
    command.details = campaign_profile
    result = await handler.handle(command)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'Create campaign profile problem encountered'}, status_code=500) 

@router.patch("/campaign/update/{id}", tags = ['Campaign'])
async def update_campaign(id: int, req: CampaignReq):
    campaign_dict = req.dict(exclude_unset=True)
    command = CampaignCommand()
    command.details = {'id': id, **campaign_dict}
    handler = UpdateCampaignCommandHandler()
    result = await handler.handle(command)
    if result:
        return req
    else:
        return JSONResponse(status_code=500, content="Update campaign profile problem encountered")

@router.delete("/campaign/delete/{id}", tags = ['Campaign'])
async def delete_campaign(id: int):
    command = CampaignCommand()
    handler = DeleteCampaignCommandHandler()
    command.details = {'id' : id}
    result = await handler.handle(command)
    if result:
        return {"message": "Campaign deleted successfully"}
    else:
        return JSONResponse(status_code=500, content="Delete campaign error")

@router.get("/campaign/list", tags = ['Campaign'])
async def list_campaigns(): 
    handler = ListCampaignQueryHandler()
    query:CampaignListQuery = await handler.handle() 
    return query.records