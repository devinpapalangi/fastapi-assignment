
from fastapi import Depends, Request
from src.depedencies.database_depedency import get_db
from src.domains.books.books_interface import IBookRepository
from sqlalchemy.orm import Session

from src.domains.books.entities.books import Book
from src.model.request.book_request import UpsertBookRequest
from src.model.response.book_response import BookResponse



class BookRepository(IBookRepository):
    def __init__(self, db:Session = Depends(get_db)):
        self.db = db
        
   
    
    def create_book(self, request: Request,create_book_request: UpsertBookRequest) -> BookResponse:
        new_book = Book(**create_book_request.model_dump())
        print(new_book)
        self.db.add(new_book)
        self.db.commit()
        return create_book_request 
        
        
        