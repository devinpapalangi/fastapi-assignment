from fastapi import Depends, Request
from src.domains.auth.auth_interface import IAuthRepository, IAuthUsecase
from src.domains.auth.auth_repository import AuthRepository
from src.model.request.auth_request import LoginRequest
from src.model.response.auth_response import TokenData


class AuthUsecase(IAuthUsecase):
    def __init__(self, auth_repository: IAuthRepository = Depends(AuthRepository)):
        self.auth_repository = auth_repository
        
    def login(self, request: Request, login_request: LoginRequest) -> TokenData:
        return self.auth_repository.login(request, login_request)