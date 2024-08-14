
from typing import List
from fastapi import Depends, HTTPException, Request
from src.depedencies.database_depedency import get_db
from src.domains.books.books_interface import IBookRepository
from sqlalchemy.orm import Session

from src.domains.books.entities.books import Book
from src.domains.outbounds.outbound_interface import IOutboundRepository
from src.domains.outbounds.outbount_repository import OutboundRepository
from src.model.request.book_request import UpsertBookRequest
from src.model.response.book_response import BookResponse



class BookRepository(IBookRepository):
    def __init__(self, db:Session = Depends(get_db), outbound_repository:IOutboundRepository = Depends(OutboundRepository)):
        self.db = db
        self.outbound_repository = outbound_repository
   
    
    def create_book(self, request: Request,create_book_request: UpsertBookRequest) -> BookResponse:
        isbn_count = self.db.query(Book).filter(Book.isbn == create_book_request.isbn).count()
        if isbn_count > 0:
            raise HTTPException(status_code=400, detail="Book with this ISBN already exists")
        
        is_valid_isbn = self.outbound_repository.is_isbn_exist(request, create_book_request.isbn)
        
        if not is_valid_isbn:
            raise HTTPException(status_code=400, detail="ISBN Not Found/Not Registered in Google Book")
        
        new_book = Book(**create_book_request.model_dump())
        self.db.add(new_book)
        self.db.commit()
        
        book_response = BookResponse(
            id = new_book.id,
            name = new_book.name,
            author = new_book.author,
            isbn = new_book.isbn
        )
        return book_response 
    
    def get_books(self, request: Request) -> List[BookResponse]:
        books_response = []
        books = self.db.query(Book).all()
        
        for book in books:
            book_response = BookResponse(
                id = book.id,
                name = book.name,
                author = book.author,
                isbn = book.isbn
            )
            books_response.append(book_response)
        
        return books_response
    
    def get_book_by_id(self, request: Request, book_id: int) -> BookResponse:
        book = self.db.query(Book).filter(Book.id == book_id).first()
        
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        
        book_response = BookResponse(
            id = book.id,
            name = book.name,
            author = book.author,
            isbn = book.isbn
        )
        
        return book_response
    
    def update_book(self, request: Request, book_id: int, update_book_request: UpsertBookRequest) -> str:
        book = self.db.query(Book).filter(Book.id == book_id).first()
        
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        
        book.name = update_book_request.name
        book.author = update_book_request.author
        book.isbn = update_book_request.isbn
        self.db.commit()
        
        return 'Succesfully updated book!'
    
    def delete_book(self, request: Request, book_id: int) -> str:
        book = self.db.query(Book).filter(Book.id == book_id).first()
        
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        
        self.db.delete(book)
        self.db.commit()
        
        return 'Succesfully deleted book!'
        
        
        
        