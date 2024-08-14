from fastapi import Depends, Request
from src.domains.users.user_interface import IUserRepository, IUserUsecase
from src.domains.users.user_repository import UserRepository
from src.model.request.user_request import UpsertUserRequest
from src.model.response.user_response import UserResponse


class UserUsecase(IUserUsecase):
    def __init__(self, user_repository: IUserRepository = Depends(UserRepository)):
        self.user_repository = user_repository
        
    def create_user(self, request: Request,create_user_request: UpsertUserRequest) -> UserResponse:
        return self.user_repository.create_user(request,create_user_request)