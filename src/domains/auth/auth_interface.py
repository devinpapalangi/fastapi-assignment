import abc

from fastapi import Request

from src.model.request.auth_request import LoginRequest
from src.model.response.auth_response import  TokenData
class IAuthRepository:
    @abc.abstractmethod
    def login(self, request: Request, login_request: LoginRequest) -> TokenData:
        pass
    
class IAuthUsecase:
    @abc.abstractmethod
    def login(self, request: Request, login_request: LoginRequest) -> TokenData:
        pass