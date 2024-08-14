

from fastapi import APIRouter, Depends, Request

from src.domains.books.book_usecase import BookUsecase
from src.domains.books.books_interface import IBookUsecase
from src.model.request.book_request import UpsertBookRequest
from src.model.response.book_response import UpsertBookResponse


router  = APIRouter(prefix='/api/v1/books', tags=['Books'])

@router.post('/')
def create_book(request: Request,create_order_request: UpsertBookRequest, book_usecase: IBookUsecase= Depends(BookUsecase)) -> UpsertBookResponse:
    new_book = book_usecase.create_book(request,create_order_request)
    
    return UpsertBookResponse(data=new_book, message='Succesfully created book!')
    