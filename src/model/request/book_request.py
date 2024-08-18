from pydantic import BaseModel, field_validator, validator, ValidationError
from typing import Union
from typing import Union
from pydantic import BaseModel, Field


class UpsertBookRequest(BaseModel):
    name: str = Field(title='Name', description='The name of the book',)
    author: str = Field(description='The author of the book')
    isbn: str = Field(description='The ISBN of the book')
    
    
class SQLInjectionError(Exception):
    pass

class BookQueryParams(BaseModel):
    name: Union[str, None] = None
    author: Union[str, None] = None
    isbn: Union[str, None] = None

    @field_validator('*')
    def clean_input(cls, v):
        if isinstance(v, str):
            # Detect common SQL injection patterns
            lower_v = v.lower()
            if any(keyword in lower_v for keyword in ["'", "--", ";", "1=1", "or", "drop", "select", "insert", "delete", "update"]):
                raise SQLInjectionError("jangan inject aku bang~")

            # Replace single quotes with escaped quotes
            v = v.replace("'", "''")
        return v


    
    