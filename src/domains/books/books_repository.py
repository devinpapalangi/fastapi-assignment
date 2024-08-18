
from typing import List
from fastapi import Depends, HTTPException, Request
from src.depedencies.database_depedency import get_db
from src.domains.books.books_interface import IBookRepository
from sqlalchemy.orm import Session

from src.domains.books.entities.books import Book
from src.domains.outbounds.outbound_interface import IOutboundRepository
from src.domains.outbounds.outbount_repository import OutboundRepository
from src.model.request.book_request import BookQueryParams, UpsertBookRequest
from src.model.response.book_response import BookResponse



class BookRepository(IBookRepository):
    def __init__(self, db:Session = Depends(get_db), outbound_repository:IOutboundRepository = Depends(OutboundRepository)):
        self.db = db
        self.outbound_repository = outbound_repository
        
    def get_db(self, request: Request) -> Session:
        return (
            request.state.db
            if hasattr(request.state, "db") and request.state.db is not None
            else self.db
        )
   
    def is_duplicate_isbn(self, request: Request, isbn: str) -> bool:
        return self.get_db(request).query(Book).filter(Book.isbn == isbn).count() > 0
    def create_book(self, request: Request,book: Book) -> Book:
        
        self.get_db(request).add(book)
        self.get_db(request).flush()
        return book 
    
    def get_books(self, request: Request, params: BookQueryParams) -> List[BookResponse]:

        #mending mana? ini atau
        books = self.get_db(request).query(Book).filter(
            Book.name.like(f"%{params.name}%") if params.name is not None else True,
            Book.author.like(f"%{params.author}%") if params.author is not None else True,
            Book.isbn.like(f"%{params.isbn}%") if params.isbn is not None else True,
            Book.created_by == request.state.user.id
        ).all()
        
        
        return books
    
    def get_book_by_id(self, request: Request, book_id: int) -> Book:
        book = self.get_db(request).query(Book).filter(Book.id == book_id, Book.created_by != request.state.user.id).first()
        return book
    
    def update_book(self, request: Request, update_book_request: UpsertBookRequest, book: Book) -> Book:
        book.name = update_book_request.name
        book.author = update_book_request.author
        book.isbn = update_book_request.isbn
        book.created_by = update_book_request.created_by
        
        
        self.get_db(request).flush()
        self.get_db(request).refresh(book)
        
        return book
    
    def delete_book(self, request: Request, book: Book) -> str:
        
        self.get_db(request).delete(book)
        self.get_db(request).flush()
        
        return 'Succesfully deleted book!'
        
        
        
        