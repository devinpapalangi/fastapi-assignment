from pydantic import BaseModel


class SingleMessageResponse(BaseModel):
    message: str