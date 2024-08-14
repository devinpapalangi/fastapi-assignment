import abc
from typing import List

from fastapi import Request

from src.model.request.user_request import UpsertUserRequest
from src.model.response.user_response import SingleUserResponse, UserResponse
from src.shared.response.single_message_response import SingleMessageResponse




class IUserRepository:
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
    def update_user(self, request: Request, user_id: int, update_user_request: UpsertUserRequest) -> SingleMessageResponse:
        pass
    @abc.abstractmethod
    def delete_user(self, request: Request, user_id: int) -> SingleMessageResponse:
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
    def update_user(self, request: Request, user_id: int, update_user_request: UpsertUserRequest) -> SingleMessageResponse:
        pass
    @abc.abstractmethod
    def delete_user(self, request: Request, user_id: int) -> SingleMessageResponse:
        pass