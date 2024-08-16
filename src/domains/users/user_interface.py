import abc
from typing import List

from fastapi import Request

from src.domains.users.entities.users import User
from src.model.request.user_request import UpsertUserRequest
from src.model.response.user_response import UserResponse
from src.shared.response.single_message_response import SingleMessageResponse




class IUserRepository:
    @abc.abstractmethod
    def create_user(self, request: Request,user: User) -> User:
        pass
    
    @abc.abstractmethod
    def get_users(self, request: Request) -> List[User]:
        pass
    @abc.abstractmethod
    def get_user_by_id(self, request: Request, user_id: int) -> User:
        pass
    @abc.abstractmethod
    def update_user(self, request: Request, update_user_request: UpsertUserRequest, user: User) -> User:
        pass
    @abc.abstractmethod
    def delete_user(self, request: Request, user: User) -> str:
        pass
    
    @abc.abstractmethod
    def get_user_by_email(self, request: Request, email: str) -> User:
        pass

class IUserUsecase:
    @abc.abstractmethod
    def create_user(self, request: Request,create_user_request: UpsertUserRequest) -> UserResponse:
        pass
    @abc.abstractmethod
    def get_users(self, request: Request) -> List[UserResponse]:
        pass
    @abc.abstractmethod
    def get_user_by_id(self, request: Request, user_id: int) -> UserResponse:
        pass
    @abc.abstractmethod
    def update_user(self, request: Request ,update_user_request: UpsertUserRequest) -> str:
        pass
    @abc.abstractmethod
    def delete_user(self, request: Request, user_id: int) -> str:
        pass
   