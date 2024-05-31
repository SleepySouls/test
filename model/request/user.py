from pydantic import BaseModel

class UserReq(BaseModel): 
    user_id : int
    email: str 
    first_name: str 
    last_name: str 
    role: str

    class Config:
        orm_mode = True

