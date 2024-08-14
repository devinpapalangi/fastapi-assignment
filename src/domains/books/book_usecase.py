from typing import List
from fastapi import Depends, Request
from src.domains.books.books_interface import IBookRepository, IBookUsecase
from src.domains.books.books_repository import BookRepository
from src.model.request.book_request import BookQueryParams, UpsertBookRequest
from src.model.response.book_response import BookResponse


class BookUsecase(IBookUsecase):

    def __init__(self, book_repository: IBookRepository = Depends(BookRepository)):
        self.book_repository = book_repository

    def create_book(self, request: Request,create_order_request: UpsertBookRequest) -> BookResponse:
        return self.book_repository.create_book(request,create_order_request)
    
    
    def get_books(self, request: Request, params: BookQueryParams) -> List[BookResponse]:
        return self.book_repository.get_books(request, params)
    
    def get_book_by_id(self, request: Request, book_id: int) -> BookResponse:
        return self.book_repository.get_book_by_id(request, book_id)
    
    def update_book(self, request: Request, book_id: int, update_book_request: UpsertBookRequest) -> str:
        return self.book_repository.update_book(request, book_id, update_book_request)
    
    def delete_book(self, request: Request, book_id: int) -> str:
        return self.book_repository.delete_book(request, book_id)