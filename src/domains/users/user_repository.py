from typing import List
from fastapi import Depends, HTTPException, Request
from src.depedencies.database_depedency import get_db
from src.domains.users.entities.users import User
from src.domains.users.user_interface import IUserRepository
from sqlalchemy.orm import Session

from src.model.request.user_request import UpsertUserRequest
from src.model.response.user_response import UserResponse
from src.shared.response.single_message_response import SingleMessageResponse
from src.utils.password_hashing import get_password_hash


class UserRepository(IUserRepository):
    def __init__(self, db: Session = Depends(get_db), ):
        self.db = db
        
    def create_user(self, request: Request,create_user_request: UpsertUserRequest) -> UserResponse:
        password_hash = get_password_hash(create_user_request.password)
        new_user = User(
            name= create_user_request.name,
            email=create_user_request.email,
            hashed_password = password_hash
        )
        user_response = UserResponse(
            id=new_user.id,
            name=new_user.name,
            email=new_user.email
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return user_response
    
    def get_users(self, request: Request) -> List[UserResponse]:
        users_response = []
        users = self.db.query(User).all()
        
        for user in users:
            user_response = UserResponse(
                id = user.id,
                name = user.name,
                email = user.email
            )
            users_response.append(user_response)
        
        return users_response
    
    def get_user_by_id(self, request: Request, user_id: int) -> UserResponse:
        user = self.db.query(User).filter(User.id == user_id).first()
        
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        user_response = UserResponse(
            id = user.id,
            name = user.name,
            email = user.email
        )
        
        return user_response
    
    def update_user(self, request: Request, user_id: int, update_user_request: UpsertUserRequest) -> SingleMessageResponse:
        user = self.db.query(User).filter(User.id == user_id).first()
        
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        user.name = update_user_request.name
        user.email = update_user_request.email
        self.db.commit()
        
        return SingleMessageResponse(message='Succesfully updated user!')
    
    def delete_user(self, request: Request, user_id: int) -> SingleMessageResponse:
        user = self.db.query(User).filter(User.id == user_id).first()
        
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        self.db.delete(user)
        self.db.commit()
        
        return SingleMessageResponse(message='Succesfully deleted user!')