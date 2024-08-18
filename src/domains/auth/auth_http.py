

from fastapi import APIRouter, Depends, Request

from src.domains.auth.auth_interface import IAuthUsecase
from src.domains.auth.auth_usecase import AuthUsecase
from src.model.request.auth_request import LoginRequest
from src.model.request.user_request import UpsertUserRequest
from src.model.response.auth_response import TokenData
from src.model.response.user_response import SingleUserResponse
from src.shared.response.single_message_response import SingleMessageResponse


router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/login', response_model=TokenData)
def login(request: Request, login_request: LoginRequest, auth_usecase: IAuthUsecase= Depends(AuthUsecase)) -> TokenData:
    token = auth_usecase.login(request, login_request)

    return TokenData(access_token=token)
    
    
@router.post('/register', response_model=SingleMessageResponse)
def register(request: Request,create_user_request: UpsertUserRequest, auth_usecase: IAuthUsecase= Depends(AuthUsecase)) -> SingleUserResponse:
    message = auth_usecase.register(request,create_user_request)
    
    return SingleMessageResponse(message=message)