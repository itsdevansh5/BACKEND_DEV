from fastapi import FastAPI,HTTPException
from models import CreateUser,UpdateUser
from storage import users
app = FastAPI()

#endpoints

@app.get("/")
def hello():
    return {"welcome":"user management API"}

@app.get("/users")
def fetchall():
    return users

@app.post("/users",status_code=201)
def create(newuser:CreateUser):
    newu={"username":newuser.username,"age":newuser.age}
    if len(users)==0:
        newu["id"]=1
    else:
        newu["id"]=max(user["id"] for user in users)+1
    users.append(newu)
    return newu

@app.get("/users/{id}")
def fetch(id:int):
    for i in users:
        if i["id"]==id:
            return i
    raise HTTPException(status_code=404,detail="user not found")    

@app.put("/users/{id}")
def update(id:int,upuser:UpdateUser):
    for i in users:
        if i["id"]==id:
            i["username"]=upuser.username
            i["age"]=upuser.age
            return i
    raise HTTPException(status_code=404,detail="user not found")

@app.delete("/users/{id}")
def delete(id:int):
    for i in users:
        if i["id"]==id:
            users.remove(i)
            return {"sucess":"deleted"}
    raise HTTPException(status_code=404,detail="user not found")

