# File: adapters/repositories/user_repository.py

from abc import ABC, abstractmethod
from domain.entities.user import User

class UserRepository(ABC):

    @abstractmethod
    def get_by_username(slef, username: str) -> User | None:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass

