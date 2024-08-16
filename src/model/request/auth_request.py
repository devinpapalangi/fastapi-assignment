from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str = Field(description='The email of the user', strip_whitespace=True)
    password: str = Field(description='The email of the user', strip_whitespace=True)