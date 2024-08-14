from typing import List, Optional
from pydantic import BaseModel



class BookResponse(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    
class SingleBookResponse(BaseModel):
    message: Optional[str] = None
    data: Optional[BookResponse] = None
    
class MultipleBookResponse(BaseModel):
    message: Optional[str] = None
    data: Optional[List[BookResponse]] = None
    