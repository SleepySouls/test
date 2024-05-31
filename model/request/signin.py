from pydantic import BaseModel

class SigninReq(BaseModel): 
    username: str 
    password: str    
    class Config:
        orm_mode = True