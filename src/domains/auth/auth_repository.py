from fastapi import Depends, HTTPException, Request
from src.domains.auth.auth_interface import IAuthRepository
from src.domains.users.user_interface import IUserRepository
from src.domains.users.user_repository import UserRepository
from src.model.request.auth_request import LoginRequest
from src.model.response.auth_response import TokenData
from src.utils.jwt import create_access_token
from src.utils.password_hashing import verify_password


class AuthRepository(IAuthRepository):
    def __init__(self, user_repository: IUserRepository = Depends(UserRepository)):
        self.user_repository = user_repository
        
    def login(self, request: Request, login_request: LoginRequest) -> TokenData:
        user = self.user_repository.get_user_by_email(request, login_request.email)
        
        is_valid_password = verify_password(login_request.password, user.hashed_password)
        if not is_valid_password:
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        
        token = create_access_token(user.id)
        
        return TokenData(access_token=token, token_type='Bearer')