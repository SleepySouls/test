from pydantic import BaseModel
from datetime import date

class DonationReq(BaseModel):
    donation_id: int
    campaign_id: int
    donator_id: int
    donation_amount: float
    donation_date: date
    message_leaving: str

    class Config:
        orm_mode = True