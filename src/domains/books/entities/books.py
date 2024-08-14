from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domains.users.entities.users import User
from src.shared.entities.base_model import BaseModel

class Book(BaseModel):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    author: Mapped[str] = mapped_column(String(255),nullable=False, index=True)
    isbn: Mapped[str] = mapped_column(String(255),nullable=False, unique=True, index=True)
    
    created_by: Mapped[int] = mapped_column(ForeignKey('users.id'), index=True)
    def __repr__(self):
        return f"Book(id={self.id!r}, name={self.name!r}, author={self.author!r}, isbn={self.isbn!r})"
    