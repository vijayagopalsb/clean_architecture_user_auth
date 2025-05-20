# File: frameworks/fastapi/routes/auth_routes.py

from fastapi import APIRouter, HTTPException
from frameworks.fastapi.dto.user_dto import UserModel
from use_cases.register_user import RegisterUserUseCase
from adapters.repositories.user_repository_impl import UserRepositoryImpl
from adapters.hashing.bcrypt_adapter import BcryptHasher
from domain.entities.user import User


router = APIRouter()

@router.post("/register")
def register_user(user_input: UserModel):

    use_case = RegisterUserUseCase(UserRepositoryImpl(), BcryptHasher())
    # Convert DTO to domain User
    user_entity = User(
        username=user_input.username,
        password=user_input.password,
        email=user_input.email
    )

    try:
        return use_case.execute(user_entity)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
