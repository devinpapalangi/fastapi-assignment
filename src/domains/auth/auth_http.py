

from fastapi import APIRouter, Depends, Request

from src.domains.auth.auth_interface import IAuthUsecase
from src.domains.auth.auth_usecase import AuthUsecase
from src.model.request.auth_request import LoginRequest


router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/login')
def login(request: Request, login_request: LoginRequest, auth_usecase: IAuthUsecase= Depends(AuthUsecase)):
    return auth_usecase.login(request, login_request)
    