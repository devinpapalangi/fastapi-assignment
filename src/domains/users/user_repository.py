from typing import List
from fastapi import Depends, HTTPException, Request
from src.depedencies.database_depedency import get_db
from src.domains.users.entities.users import User
from src.domains.users.user_interface import IUserRepository
from sqlalchemy.orm import Session

from src.model.request.user_request import UpsertUserRequest
from src.utils.password_hashing import get_password_hash


class UserRepository(IUserRepository):
    def __init__(self, db: Session = Depends(get_db), ):
        self.db = db
        
    def get_db(self, request: Request) -> Session:
        return (
            request.state.db
            if hasattr(request.state, "db") and request.state.db is not None
            else self.db
        )
        
    def create_user(self, request: Request,user: User) -> str:
        self.get_db(request).add(user)
        self.get_db(request).flush()
        return 'Succesfully created user!'
    
    def get_users(self, request: Request) -> List[User]:
        users = self.get_db(request).query(User).all()
        
        return users
    
    def get_user_by_id(self, request: Request, user_id: int) -> User:
        user = self.get_db(request).query(User).filter(User.id == user_id).first()
        
        return user
    
    def update_user(self, request: Request, update_user_request: UpsertUserRequest, user: User) -> User:
        user.name = update_user_request.name
        user.email = update_user_request.email
        user.hashed_password = get_password_hash(update_user_request.password)
        self.get_db(request).flush()
        return user
        
    def delete_user(self, request: Request, user: User) -> str:
        
        self.get_db(request).delete(user)
        self.get_db(request).flush()
        
        return 'Succesfully deleted user!'
    
    def get_user_by_email(self, request: Request, email: str) -> User:
        user = self.get_db(request).query(User).filter(User.email == email).first()
        
        return user