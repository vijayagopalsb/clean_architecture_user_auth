# File: use_cases/register_user.py

from domain.entities.user import User
from adapters.repositories.user_repository import UserRepository
from adapters.hashing.hasher import Hasher

class RegisterUserUseCase:

    def __init__(self, user_repository: UserRepository, hasher: Hasher):
        self.user_repository = user_repository
        self.hasher = hasher

    def execute(self, user: User):
        if self.user_repository.get_by_username(username=user.username):
            raise ValueError("User already exists")

        hashed_password = self.hasher.hash(password=user.password)
        user.password = hashed_password
        self.user_repository.save(user)
        return {"message": "User registered successfully"}

