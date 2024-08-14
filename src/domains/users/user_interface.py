import abc

from fastapi import Request

from src.model.request.user_request import UpsertUserRequest
from src.model.response.user_response import UserResponse




class IUserRepository:
    @abc.abstractmethod
    def create_user(self, request: Request,create_user_request: UpsertUserRequest) -> UserResponse:
        pass

class IUserUsecase:
    @abc.abstractmethod
    def create_user(self, request: Request,create_user_request: UpsertUserRequest) -> UserResponse:
        pass