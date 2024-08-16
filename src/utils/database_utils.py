 

from fastapi import Request
from src.depedencies.database_depedency import get_db


def commit(request: Request):
    request.state.db.commit()
    request.state.db = None


def rollback_all(request: Request):
  
    try:
        request.state.db.rollback()
        request.state.db = None
    except Exception as ex: 
        pass


def begin_transaction(request: Request):
    request.state.db = next(get_db())