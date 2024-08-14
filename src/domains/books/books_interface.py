import abc
from typing import List

from fastapi import Request

from src.model.request.book_request import UpsertBookRequest
from src.model.response.book_response import BookResponse, MultipleBookResponse
from src.shared.response.single_message_response import SingleMessageResponse

class IBookRepository:
    @abc.abstractmethod
    def create_book(self, request: Request,create_order_request: UpsertBookRequest) -> BookResponse:
        pass
    @abc.abstractmethod
    def get_books(self, request: Request) -> List[BookResponse]:
        pass
    @abc.abstractmethod
    def get_book_by_id(self, request: Request, book_id: int) -> BookResponse:
        pass
    @abc.abstractmethod
    def update_book(self, request: Request, book_id: int, update_book_request: UpsertBookRequest) -> SingleMessageResponse:
        pass
    @abc.abstractmethod
    def delete_book(self, request: Request, book_id: int) -> SingleMessageResponse:
        pass
    
class IBookUsecase:
    @abc.abstractmethod
    def create_book(self, request: Request,create_order_request: UpsertBookRequest) -> BookResponse:
        pass
    
    def get_books(self, request: Request) -> MultipleBookResponse:
        pass
    
    def get_book_by_id(self, request: Request, book_id: int) -> BookResponse:
        pass
    
    def update_book(self, request: Request, book_id: int, update_book_request: UpsertBookRequest) -> SingleMessageResponse:
        pass
    
    def delete_book(self, request: Request, book_id: int) -> SingleMessageResponse:
        pass