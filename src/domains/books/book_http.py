

from fastapi import APIRouter, Depends, Request

from src.domains.books.book_usecase import BookUsecase
from src.domains.books.books_interface import IBookUsecase
from src.model.request.book_request import UpsertBookRequest
from src.model.response.book_response import MultipleBookResponse, SingleBookResponse
from src.shared.response.single_message_response import SingleMessageResponse


router  = APIRouter(prefix='/api/v1/books', tags=['Books'])

@router.post('/')
def create_book(request: Request,create_order_request: UpsertBookRequest, book_usecase: IBookUsecase= Depends(BookUsecase)) -> SingleBookResponse:
    new_book = book_usecase.create_book(request,create_order_request)
    
    return SingleBookResponse(data=new_book, message='Succesfully created book!')

@router.get('/')
def get_books(request: Request, book_usecase: IBookUsecase= Depends(BookUsecase)) -> MultipleBookResponse:
    books = book_usecase.get_books(request)
    
    return MultipleBookResponse(data=books, message='Succesfully retrieved books!')

@router.get('/{book_id}')
def get_book_by_id(request: Request, book_id: int, book_usecase: IBookUsecase= Depends(BookUsecase)) -> SingleBookResponse:
    book = book_usecase.get_book_by_id(request, book_id)
    
    return SingleBookResponse(data=book, message='Succesfully retrieved book!')

@router.put('/{book_id}')
def update_book(request: Request, book_id: int, update_book_request: UpsertBookRequest, book_usecase: IBookUsecase= Depends(BookUsecase)) -> SingleMessageResponse:
    message = book_usecase.update_book(request, book_id, update_book_request)
    
    return SingleMessageResponse(message=message)

@router.delete('/{book_id}')
def delete_book(request: Request, book_id: int, book_usecase: IBookUsecase= Depends(BookUsecase)) -> SingleMessageResponse:
    message = book_usecase.delete_book(request, book_id)
    
    return SingleMessageResponse(message=message)
    