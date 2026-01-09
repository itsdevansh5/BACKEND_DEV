from signup import hashpass
from signin import login

a=input()

b=hashpass(a)

print(login(a))

