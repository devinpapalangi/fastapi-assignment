from typing import Optional
from pydantic import BaseModel



class UserResponse(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None

class UpsertUserResponse(BaseModel):
    message: Optional[str] = None
    data: Optional[UserResponse] = None