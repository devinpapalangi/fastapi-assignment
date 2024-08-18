from fastapi import Depends, HTTPException, Request
from src.domains.auth.auth_interface import  IAuthUsecase
from src.domains.users.entities.users import User
from src.domains.users.user_interface import IUserRepository
from src.domains.users.user_repository import UserRepository
from src.model.request.auth_request import LoginRequest
from src.model.request.user_request import UpsertUserRequest
from src.model.response.auth_response import TokenData
from src.model.response.user_response import UserResponse
from src.utils.database_utils import begin_transaction, commit
from src.utils.jwt import create_access_token
from src.utils.password_hashing import get_password_hash, verify_password


class AuthUsecase(IAuthUsecase):
    def __init__(self, user_repository: IUserRepository = Depends(UserRepository)):
        self.user_repository = user_repository
        
    def login(self, request: Request, login_request: LoginRequest) -> str:
        user = self.user_repository.get_user_by_email(request, login_request.email)
        
        if user is None:
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        
        
        is_valid_password = verify_password(login_request.password, user.hashed_password)
        if not is_valid_password:
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        
        token = create_access_token(user.id)
        return token
    
    def register(self, request: Request,create_user_request: UpsertUserRequest) -> str:
        begin_transaction(request)
        hashed_password = get_password_hash(create_user_request.password)
    
        new_user = User(
            name= create_user_request.name,
            email=create_user_request.email,
            hashed_password = hashed_password
        )
        res = self.user_repository.create_user(request,user=new_user)
        
        commit(request)
        
        return res