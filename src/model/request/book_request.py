
from typing import Union
from pydantic import BaseModel, Field


class UpsertBookRequest(BaseModel):
    name: str = Field(title='Name', description='The name of the book',)
    author: str = Field(description='The author of the book')
    isbn: str = Field(description='The ISBN of the book')
    created_by: int = Field(description='The created by (user id) of the book')