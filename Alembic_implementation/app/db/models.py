from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base
from .database import engine
Base=declarative_base()

class Users(Base):
    __tablename__="users"


    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    age=Column(Integer)
    Email=Column(String)


