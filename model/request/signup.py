from pydantic import BaseModel


class SignupReq(BaseModel): 
    id : int 
    username: str 
    password: str 
    email: str
    first_name: str
    last_name: str
    role: str
    
    class Config:
        orm_mode = True