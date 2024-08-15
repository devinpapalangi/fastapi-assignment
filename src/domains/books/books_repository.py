
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
   
    def is_duplicate_isbn(self, request: Request, isbn: str) -> bool:
        return self.db.query(Book).filter(Book.isbn == isbn).count() > 0
    def create_book(self, request: Request,create_book_request: UpsertBookRequest) -> BookResponse:
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
    
    def get_books(self, request: Request, params: BookQueryParams) -> List[BookResponse]:
        books_response = []
        
        #mending mana? ini atau
        books = self.db.query(Book).filter(
            Book.name.like(f"%{params.name}%") if params.name is not None else True,
            Book.author.like(f"%{params.author}%") if params.author is not None else True,
            Book.isbn.like(f"%{params.isbn}%") if params.isbn is not None else True
        ).all()
        # atau ini?
        # filters = []
        # if params.name is not None:
        #     filters.append(Book.name.like(f"%{params.name}%"))
        # if params.author is not None:
        #     filters.append(Book.author.like(f"%{params.author}%"))
        # if params.isbn is not None:
        #     filters.append(Book.isbn.like(f"%{params.isbn}%"))
            
        #     books = self.db.query(Book).filter(and_(*filters)).all()
        
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
        
        
        
        