# File: adapters/hashing/bcrypt_hasher.py

from passlib.context import CryptContext
from adapters.hashing.hasher import Hasher

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class BcryptHasher(Hasher):

    def hash(self, password):
        return pwd_context.hash(password)

    def verify(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
