from corelogic import pwd

def hashpass(plainp:str)-> str:
    return pwd.hash(plainp)


