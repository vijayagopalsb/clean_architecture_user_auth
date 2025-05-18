# File: frameworks/fastapi/routes/auth_routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from adapters.repositories.user_repository_impl import UserRepositoryImpl
from adapters.hashing.bcrypt_adapter import BcryptHasher
from use_cases.register_user import RegisterUserUseCase

router = APIRouter()

class RegisterRequest(BaseModel):
    username: str
    password: str
    email: str

@router.post("/register")
def register_user(request: RegisterRequest):
    
    use_case = RegisterUserUseCase(UserRepositoryImpl(), BcryptHasher())
    try:
        return use_case.execute(request.username, request.password, request.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
