from fastapi import FastAPI
from fastapi import HTTPException
from schemas import UserCreate,ReturnUser
from fastapi import Depends
from sqlalchemy.orm import Session
from models import Users
from database import get_db,Base,engine

app = FastAPI()
Base.metadata.create_all(bind=engine)
#endpoints

@app.post("/users",response_model=ReturnUser,status_code=201)
def create(newu:UserCreate,db:Session=Depends(get_db)):
    db_user=Users(username=newu.username,age=newu.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


