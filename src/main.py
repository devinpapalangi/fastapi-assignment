

import http
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.domains.books import book_http
from src.domains.users import user_http


app = FastAPI()

@app.get("/")
def status():
    return {"status": "ok"}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    return JSONResponse(
        status_code=http.HTTPStatus.BAD_REQUEST,
        content=jsonable_encoder(
            {
                "error": " ".join([str(i) for i in exc.errors()[0]["loc"]])
                + " "
                + exc.errors()[0]["msg"],
                "status_code": http.HTTPStatus.BAD_REQUEST,
            }
        ),
    )


@app.exception_handler(ValidationError)
async def validation_exception_handler(
    request: Request, exc: ValidationError
) -> JSONResponse:
    err = " ".join([str(i) for i in exc.errors()[0]["loc"]])
    return JSONResponse(
        status_code=http.HTTPStatus.BAD_REQUEST,
        content=jsonable_encoder(
            {
                "error": err + ": " + exc.errors()[0]["msg"],
                "status_code": http.HTTPStatus.BAD_REQUEST,
            }
        ),
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(
    request: Request, exc: StarletteHTTPException
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder({"error": exc.detail, "status_code": exc.status_code}),
    )


@app.exception_handler(500)
async def internal_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content=jsonable_encoder({"status_code": 500, "error": str(exc)}),
    )
app.include_router(book_http.router)
app.include_router(user_http.router)