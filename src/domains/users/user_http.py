

from fastapi import APIRouter, Depends, Request

from src.domains.users.user_usecase import UserUsecase
from src.domains.users.user_interface import IUserUsecase
from src.model.request.user_request import UpsertUserRequest
from src.model.response.user_response import MultipleUserResponse, SingleUserResponse,  UserResponse
from src.shared.response.single_message_response import SingleMessageResponse


router = APIRouter(prefix='/api/v1/users', tags=['Users'])


@router.post('/', response_model=SingleUserResponse)
def create_user(request: Request,create_user_request: UpsertUserRequest, user_usecase: IUserUsecase= Depends(UserUsecase)) -> SingleUserResponse:
    new_user = user_usecase.create_user(request,create_user_request)
    
    return SingleUserResponse(data=new_user, message='Succesfully created user!')

@router.get('/', response_model=MultipleUserResponse)
def get_users(request: Request, user_usecase: IUserUsecase= Depends(UserUsecase)) -> MultipleUserResponse:
    users = user_usecase.get_users(request)
    
    return MultipleUserResponse(data=users, message='Succesfully retrieved users!')

@router.get('/{user_id}', response_model=SingleUserResponse)
def get_user_by_id(request: Request, user_id: int, user_usecase: IUserUsecase= Depends(UserUsecase)) -> SingleUserResponse:
    user = user_usecase.get_user_by_id(request, user_id)
    
    return SingleUserResponse(data=user, message='Succesfully retrieved user!')

@router.put('/{user_id}', response_model=SingleUserResponse)
def update_user(request: Request, user_id: int, update_user_request: UpsertUserRequest, user_usecase: IUserUsecase= Depends(UserUsecase)) -> SingleUserResponse:
    new_user_Data = user_usecase.update_user(request, user_id, update_user_request)
    
    return SingleUserResponse(data=new_user_Data, message='Succesfully updated user!')

@router.delete('/{user_id}', response_model=SingleMessageResponse)
def delete_user(request: Request, user_id: int, user_usecase: IUserUsecase= Depends(UserUsecase)) -> SingleMessageResponse:
    message = user_usecase.delete_user(request, user_id)
    
    return SingleMessageResponse(message=message)

