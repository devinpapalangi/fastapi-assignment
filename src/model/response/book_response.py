from typing import Optional
from pydantic import BaseModel



class BookResponse(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
class UpsertBookResponse(BaseModel):
    message: Optional[str] = None
    data: Optional[BookResponse] = None