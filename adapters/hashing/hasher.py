# File: adapters/hashing/hasher.py

from abc import ABC, abstractmethod

class Hasher(ABC):

    @abstractmethod
    def hash(self, password: str) -> str:
        pass

    @abstractmethod
    def verify(self, plain_password: str, hashed_password: str) -> bool:
        pass
