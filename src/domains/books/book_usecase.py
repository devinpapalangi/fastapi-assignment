from fastapi import Depends, Request
from src.domains.books.books_interface import IBookRepository, IBookUsecase
from src.domains.books.books_repository import BookRepository
from src.model.request.book_request import UpsertBookRequest
from src.model.response.book_response import UpsertBookResponse


class BookUsecase(IBookUsecase):

    def __init__(self, book_repository: IBookRepository = Depends(BookRepository)):
        self.book_repository = book_repository

    def create_book(self, request: Request,create_order_request: UpsertBookRequest) -> UpsertBookResponse:
        print
        return self.book_repository.create_book(request,create_order_request)