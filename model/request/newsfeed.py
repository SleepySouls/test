from pydantic import BaseModel
from datetime import date

class NewsfeedReq(BaseModel): 
    newsfeed_id : int
    author: str
    headline: str
    summary: str
    media: bytes 
    publish_date: date 
    category: str
    author_id: int
    
    class Config:
        orm_mode = True

