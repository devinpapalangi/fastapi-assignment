import abc
from typing import List

from fastapi import Request

from src.domains.books.entities.books import Book
from src.model.request.book_request import BookQueryParams, UpsertBookRequest
from src.model.response.book_response import BookResponse
from src.shared.response.single_message_response import SingleMessageResponse

class IBookRepository:
    @abc.abstractmethod
    def create_book(self, request: Request,book: Book) -> Book:
        pass
    @abc.abstractmethod
    def get_books(self, request: Request, params: BookQueryParams) -> List[Book]:
        pass
    @abc.abstractmethod
    def get_book_by_id(self, request: Request, book_id: int) -> Book:
        pass
    @abc.abstractmethod
    def update_book(self, request: Request, update_book_request: UpsertBookRequest, book: Book) -> Book:
        pass
    @abc.abstractmethod
    def delete_book(self, request: Request, Book: Book) -> str:
        pass
    
    @abc.abstractmethod
    def is_duplicate_isbn(self, request: Request, isbn: str) -> bool:
        pass
    
class IBookUsecase:
    @abc.abstractmethod
    def create_book(self, request: Request,create_order_request: UpsertBookRequest) -> BookResponse:
        pass
    @abc.abstractmethod
    def get_books(self, request: Request, params: BookQueryParams) -> List[BookResponse]:
        pass
    
    @abc.abstractmethod
    def get_book_by_id(self, request: Request, book_id: int) -> BookResponse:
        pass
    @abc.abstractmethod
    def update_book(self, request: Request, book_id: int, update_book_request: UpsertBookRequest) -> BookResponse:
        pass
    @abc.abstractmethod
    def delete_book(self, request: Request, book_id: int) -> str:
        pass
    
    