import abc

from fastapi import Request

class IOutboundRepository():

    @abc.abstractmethod
    def is_isbn_exist(self, request: Request, isbn: str) -> bool:
        pass