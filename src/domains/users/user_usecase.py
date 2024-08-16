from typing import List
from fastapi import Depends, HTTPException, Request
from src.domains.users.entities.users import User
from src.domains.users.user_interface import IUserRepository, IUserUsecase
from src.domains.users.user_repository import UserRepository
from src.model.request.user_request import UpsertUserRequest
from src.model.response.user_response import MultipleUserResponse, SingleUserResponse, UserResponse
from src.shared.response.single_message_response import SingleMessageResponse
from src.utils.database_utils import begin_transaction, commit
from src.utils.password_hashing import get_password_hash


class UserUsecase(IUserUsecase):
    def __init__(self, user_repository: IUserRepository = Depends(UserRepository)):
        self.user_repository = user_repository
        
    def create_user(self, request: Request,create_user_request: UpsertUserRequest) -> UserResponse:
        begin_transaction(request)
        hashed_password = get_password_hash(create_user_request.password)
    
        new_user = User(
            name= create_user_request.name,
            email=create_user_request.email,
            hashed_password = hashed_password
        )
        self.user_repository.create_user(request,user=new_user)
        
        commit(request)
        
        return UserResponse(
            id=new_user.id,
            name=new_user.name,
            email=new_user.email
        )
    
    def get_users(self, request: Request) -> List[UserResponse]:
        users = self.user_repository.get_users(request)
        
        res = []
        for user in users:
            res.append(UserResponse(
                id=user.id,
                name=user.name,
                email=user.email
            ))
            
        return res
    
    def get_user_by_id(self, request: Request, user_id: int) -> UserResponse:
        user = self.user_repository.get_user_by_id(request, user_id)
        
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email
        )
    
    def update_user(self, request: Request, user_id: int, update_user_request: UpsertUserRequest) -> UserResponse:
        begin_transaction(request)

        user = self.user_repository.get_user_by_id(request, user_id)
        
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        check_email = self.user_repository.get_user_by_email(request, update_user_request.email)
        
        if check_email is not None and check_email.id != user_id:
            raise HTTPException(status_code=400, detail="Email already exists")
        
        
        updated_user = self.user_repository.update_user(request,   update_user_request,user,)
        
        commit(request)
        
        return UserResponse(
            id=updated_user.id,
            name=updated_user.name,
            email=updated_user.email
        )
    
    def delete_user(self, request: Request, user_id: int) -> str:
        begin_transaction(request)
        user = self.user_repository.get_user_by_id(request, user_id)
        
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        res = self.user_repository.delete_user(request, user)
        
        commit(request)
        return res