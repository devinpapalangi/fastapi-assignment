from pydantic import BaseModel, Field


class UpsertUserRequest(BaseModel):
    name: str = Field(title='Name', description='The name of the user', strip_whitespace=True)
    email: str = Field(description='The email of the user', strip_whitespace=True)
    password: str = Field(description='The password of the user',strip_whitespace=True)
    
