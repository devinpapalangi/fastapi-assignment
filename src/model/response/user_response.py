from typing import List, Optional
from pydantic import BaseModel



class UserResponse(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None

class SingleUserResponse(BaseModel):
    message: Optional[str] = None
    data: Optional[UserResponse] = None
    
class MultipleUserResponse(BaseModel):
    message: Optional[str] = None
    data: Optional[List[UserResponse]] = None