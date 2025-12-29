from pydantic import BaseModel

class CreateUser(BaseModel):
    username:str
    age:int

class UpdateUser(BaseModel):
    username:str
    age:int
