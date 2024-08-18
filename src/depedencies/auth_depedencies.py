from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt

from src.config.config import get_config
from src.domains.users.user_interface import IUserRepository
from src.domains.users.user_repository import UserRepository

http_bearer = HTTPBearer()


def bearer_auth(request: Request, auth: HTTPAuthorizationCredentials = Depends(http_bearer), user_repository: IUserRepository = Depends(UserRepository)):
    config = get_config()
    header = request.headers['Authorization'].removeprefix('Bearer ')
    payload = jwt.decode(header, config.JWT_SECRET_KEY, algorithms=[config.JWT_HASHING_ALGORITHM])
    
    user_id = payload.get('sub')
    
    user = user_repository.get_user_by_id(request, user_id)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    request.state.user = user
    
    return user
    
    
    