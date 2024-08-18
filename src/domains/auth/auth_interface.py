import abc

from fastapi import Request

from src.model.request.auth_request import LoginRequest
from src.model.request.user_request import UpsertUserRequest
from src.model.response.auth_response import  TokenData

    
class IAuthUsecase:
    @abc.abstractmethod
    def login(self, request: Request, login_request: LoginRequest) -> tuple[str, int]:
        pass
    
    def register(self, request: Request, register_request: UpsertUserRequest) -> str:
        pass