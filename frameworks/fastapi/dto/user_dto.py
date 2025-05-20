# File: frameworks/fastapi/dto/user_dto.py

from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):
    username: str
    password: str
    email: EmailStr
