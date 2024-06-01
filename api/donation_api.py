from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db_config.gino_connect import sess_db
from model.request.donation import DonationReq
from cqrs.donation.commands.update_handlers import UpdateDonationCommandHandler
from cqrs.donation.commands.create_handlers import AddDonationCommandHandler
from cqrs.donation.commands.delete_handlers import DeleteDonationCommandHandler
from cqrs.donation.query.query_handlers import ListDonationQueryHandler
from cqrs.donation.command import DonationCommand
from cqrs.donation.queries import DonationListQuery
from jwt.secure import get_current_user

router = APIRouter(dependencies=[Depends(sess_db)])


@router.post("/donation/add", tags=['Donation'])
async def add_donation(req: DonationReq, current_user: dict = Depends(get_current_user)): 
    handler = AddDonationCommandHandler()
    donation_profile = dict()
    donation_profile["donation_id"] = req.donation_id
    donation_profile["campaign_id"] = req.campaign_id
    donation_profile["donator_id"] = req.donator_id
    donation_profile["donation_amount"] = req.donation_amount
    donation_profile["donation_date"] = req.donation_date
    donation_profile["message_leaving"] = req.message_leaving
    command = DonationCommand()
    command.details = donation_profile
    result = await handler.handle(command)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'create donation profile problem encountered'}, status_code=500) 

@router.patch("/donation/update/{id}", tags=['Donation'])
async def update_donation(id: int, req: DonationReq, current_user: dict = Depends(get_current_user)):
    campaign_dict = req.dict(exclude_unset=True)
    command = DonationCommand()
    command.details = {'id': id, **campaign_dict}
    handler = UpdateDonationCommandHandler()
    result = await handler.handle(command)
    if result:
        return req
    else:
        return JSONResponse(status_code=500, content="Update donation profile problem encountered")

@router.delete("/donation/delete/{id}", tags=['Donation'])
async def delete_donation(id: int, current_user: dict = Depends(get_current_user)):
    command = DonationCommand()
    handler = DeleteDonationCommandHandler()
    command.details = {'id' : id}
    result = await handler.handle(command)
    if result:
        return {"message": "Donation deleted successfully"}
    else:
        return JSONResponse(status_code=500, content="Delete donation error")

@router.get("/donation/list", tags=['Donation'])
async def list_donations(current_user: dict = Depends(get_current_user)): 
    handler = ListDonationQueryHandler()
    query:DonationListQuery = await handler.handle() 
    return query.records

