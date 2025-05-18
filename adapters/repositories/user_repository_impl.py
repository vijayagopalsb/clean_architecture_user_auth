# File: adapters/repositories/user_repository_impl.py

from domain.entities.user import User
from adapters.repositories.user_repository import UserRepository

user_db = {}

class UserRepositoryImpl(UserRepository):

    def get_by_username(self, username):
        return user_db.get(username)
    
    def save(self, user: User) -> None:
        user_db[user.username] = user
        