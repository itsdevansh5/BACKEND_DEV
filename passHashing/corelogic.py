from passlib.context import CryptContext

pwd=CryptContext(schemes=["bcrypt"],deprecated="auto")


