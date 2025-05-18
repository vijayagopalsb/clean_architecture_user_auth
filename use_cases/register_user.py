# File: use_cases/register_user.py

from domain.entities.user import User
from adapters.repositories.user_repository import UserRepository
from adapters.hashing.hasher import Hasher

class RegisterUserUseCase:

    def __init__(self, user_repository: UserRepository, hasher: Hasher):
        self.user_repository = user_repository
        self.hasher = hasher

    def execute(self, username: str, password: str, email: str):
        if self.user_repository.get_by_username(username=username):
            raise ValueError("User already exists")

        hashed_password = self.hasher.hash(password=password)
        user = User(Username=username, password=hashed_password, email=email)
        self.user_repository.save(user)
        return {"message": "User registered successfully"}

