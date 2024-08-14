from fastapi import HTTPException, Request
from src.config.config import get_config
from src.domains.outbounds.outbound_interface import IOutboundRepository
import requests


class OutboundRepository(IOutboundRepository):
    
    def is_isbn_exist(self, request: Request, isbn: str) -> bool:
        config = get_config()
        try:
            response = requests.get(f'https://www.googleapis.com/books/v1/volumes', params={'q': f'isbn:{isbn}','key': config.GOOGLE_BOOK_API_KEY})
            
            if response.status_code != 200:
                raise HTTPException(status_code=500, detail="Outbound Error: Google API is not available")
            
            total_items = response.json()['totalItems']
            
            if total_items>0:
                return True
            else:
                return False
        except:
            raise HTTPException(
                status_code=500,
                detail="Unknow error from Google API",
            )