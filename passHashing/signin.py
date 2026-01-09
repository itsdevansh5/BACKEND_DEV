from corelogic import pwd

def login(plainp:str)-> bool:
    return pwd.verify(plainp,hashed)
