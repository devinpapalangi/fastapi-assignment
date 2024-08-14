

from fastapi import APIRouter, Depends, Request

from src.domains.users.user_usecase import UserUsecase
from src.domains.users.user_interface import IUserUsecase
from src.model.request.user_request import UpsertUserRequest
from src.model.response.user_response import UpsertUserResponse, UserResponse


router = APIRouter(prefix='/api/v1/users', tags=['Users'])


@router.post('/', response_model=UpsertUserResponse)
def create_user(request: Request,create_user_request: UpsertUserRequest, user_usecase: IUserUsecase= Depends(UserUsecase)) -> UpsertUserResponse:
    new_user = user_usecase.create_user(request,create_user_request)
    
    return UpsertUserResponse(data=UserResponse(id=new_user.id, name=new_user.name, email=new_user.email), message='Succesfully created user!')