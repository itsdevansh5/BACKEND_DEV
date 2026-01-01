from fastapi import FastAPI
from fastapi import HTTPException
from schemas import UserCreate
from fastapi import Depends
from sqlalchemy.orm import Session
from models import users
from database import get_db
app = FastAPI()

#endpoints

@app.post("/users")
def create(newu:UserCreate,db:Session=Depends(get_db)):
    db_user=users(username=newu.username,age=newu.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user




