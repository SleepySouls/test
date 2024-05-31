from pydantic import BaseModel
from datetime import date

class CampaignReq(BaseModel):
    campaign_id: int
    title: str
    description: str
    goal_amount: float
    raised_amount: float
    start_date: date
    end_date: date
    category: str
    media: bytes
    status: str

    class Config:
        orm_mode = True