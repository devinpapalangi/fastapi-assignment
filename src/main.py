

from fastapi import FastAPI

from src.domains.books import book_http
from src.domains.users import user_http


app = FastAPI()

@app.get("/")
def status():
    return {"status": "ok"}


app.include_router(book_http.router)
app.include_router(user_http.router)