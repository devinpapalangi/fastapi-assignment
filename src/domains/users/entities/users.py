from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String


from src.shared.entities.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255),nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255),nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"