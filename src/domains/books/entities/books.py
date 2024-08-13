from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.shared.entities.base_model import BaseModel

class Book(BaseModel):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    author: Mapped[str] = mapped_column(String(255),nullable=False)
    isbn: Mapped[str] = mapped_column(String(255),nullable=False)
    
    def __repr__(self):
        return f"Book(id={self.id!r}, name={self.name!r}, author={self.author!r}, isbn={self.isbn!r})"
    