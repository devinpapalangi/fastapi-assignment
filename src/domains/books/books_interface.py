import abc

from fastapi import Request

from src.model.request.book_request import UpsertBookRequest
from src.model.response.book_response import BookResponse, UpsertBookResponse

class IBookRepository:
    @abc.abstractmethod
    def create_book(self, request: Request,create_order_request: UpsertBookRequest) -> BookResponse:
        pass
    
class IBookUsecase:
    @abc.abstractmethod
    def create_book(self, request: Request,create_order_request: UpsertBookRequest) -> UpsertBookResponse:
        pass