from typing import List
from fastapi import Depends, Request
from src.domains.users.user_interface import IUserRepository, IUserUsecase
from src.domains.users.user_repository import UserRepository
from src.model.request.user_request import UpsertUserRequest
from src.model.response.user_response import MultipleUserResponse, UserResponse
from src.shared.response.single_message_response import SingleMessageResponse


class UserUsecase(IUserUsecase):
    def __init__(self, user_repository: IUserRepository = Depends(UserRepository)):
        self.user_repository = user_repository
        
    def create_user(self, request: Request,create_user_request: UpsertUserRequest) -> UserResponse:
        return self.user_repository.create_user(request,create_user_request)
    
    def get_users(self, request: Request) -> List[UserResponse]:
        return self.user_repository.get_users(request)
    
    def get_user_by_id(self, request: Request, user_id: int) -> UserResponse:
        return self.user_repository.get_user_by_id(request, user_id)
    
    def update_user(self, request: Request, user_id: int, update_user_request: UpsertUserRequest) -> SingleMessageResponse:
        return self.user_repository.update_user(request, user_id, update_user_request)
    
    def delete_user(self, request: Request, user_id: int) -> SingleMessageResponse:
        return self.user_repository.delete_user(request, user_id)