from fastapi import Depends, Request
from src.depedencies.database_depedency import get_db
from src.domains.users.entities.users import User
from src.domains.users.user_interface import IUserRepository
from sqlalchemy.orm import Session

from src.model.request.user_request import UpsertUserRequest
from src.model.response.user_response import UserResponse
from src.utils.password_hashing import get_password_hash


class UserRepository(IUserRepository):
    def __init__(self, db: Session = Depends(get_db), ):
        self.db = db
        
    def create_user(self, request: Request,create_user_request: UpsertUserRequest) -> UserResponse:
        print(f'create_user_request in repo: ${create_user_request}')
        password_hash = get_password_hash(create_user_request.password)
        print(f'hashed password in repo: ${password_hash}')
        new_user = User(
            name= create_user_request.name,
            email=create_user_request.email,
            hashed_password = password_hash
        )
        
        print("database object generated in repo: ", new_user)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user