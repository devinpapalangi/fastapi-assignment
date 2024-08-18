from typing import List
from fastapi import Depends, HTTPException, Request
from src.domains.books.books_interface import IBookRepository, IBookUsecase
from src.domains.books.books_repository import BookRepository
from src.domains.books.entities.books import Book
from src.domains.outbounds.outbound_interface import IOutboundRepository
from src.domains.outbounds.outbount_repository import OutboundRepository
from src.model.request.book_request import BookQueryParams, UpsertBookRequest
from src.model.response.book_response import BookResponse
from src.utils.database_utils import begin_transaction, commit


class BookUsecase(IBookUsecase):

    def __init__(self, book_repository: IBookRepository = Depends(BookRepository), outbound_repository:IOutboundRepository = Depends(OutboundRepository)):
        self.book_repository = book_repository
        self.outbound_repository = outbound_repository
        
    

    def create_book(self, request: Request,create_order_request: UpsertBookRequest) -> BookResponse:
        begin_transaction(request)
        is_isbn_exist =- self.book_repository.is_duplicate_isbn(request, create_order_request.isbn)
        
        if is_isbn_exist:
            raise HTTPException(status_code=400, detail="ISBN Already Exist")
        
        is_valid_isbn = self.outbound_repository.is_isbn_exist(request, create_order_request.isbn)
        
        if not is_valid_isbn:    
            raise HTTPException(status_code=400, detail="ISBN Not Found")
        
            
        new_book = Book(
            name= create_order_request.name,
            author=create_order_request.author,
            isbn=create_order_request.isbn,
            created_by= request.state.user.id
        )
        
        self.book_repository.create_book(request, new_book)
        commit(request)
            
        return BookResponse(
            id = new_book.id,
            name = new_book.name,
            author = new_book.author,
            isbn = new_book.isbn
        )
    
    
    def get_books(self, request: Request, params: BookQueryParams) -> List[BookResponse]:
        books = self.book_repository.get_books(request, params)
        res= []
        for book in books:
            res.append(BookResponse(
                id = book.id,
                name = book.name,
                author = book.author,
                isbn = book.isbn
            ))
        return res
    
    def get_book_by_id(self, request: Request, book_id: int) -> BookResponse:
        book = self.book_repository.get_book_by_id(request, book_id)
        
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        
        res = BookResponse(
            id = book.id,
            name = book.name,
            author = book.author,
            isbn = book.isbn
        )
        return res
    
    def update_book(self, request: Request, book_id: int, update_book_request: UpsertBookRequest) -> BookResponse:
        begin_transaction(request)
        book = self.book_repository.get_book_by_id(request, book_id)
        
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        
        is_isbn_exists = self.book_repository.is_duplicate_isbn(request, update_book_request.isbn)
        
        if is_isbn_exists:
            raise HTTPException(status_code=400, detail="ISBN Already Exist")
        
        is_valid_isbn = self.outbound_repository.is_isbn_exist(request, update_book_request.isbn)
        
        if not is_valid_isbn:    
            raise HTTPException(status_code=400, detail="ISBN Not Found")
        
        
        updated_book = self.book_repository.update_book(request, update_book_request,book)
        
        commit(request)
        
        return BookResponse(
            id = updated_book.id,
            name = updated_book.name,
            author = updated_book.author,
            isbn = updated_book.isbn
        )
        
    
    def delete_book(self, request: Request, book_id: int) -> str:
        begin_transaction(request)
        book_tobedeleted = self.book_repository.get_book_by_id(request, book_id)
        
        res = self.book_repository.delete_book(request, book_tobedeleted)
        commit(request)
        return res
    