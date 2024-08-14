from typing import Generator
from sqlalchemy.orm import Session

from src.infrastructure.databases.database import postgres


def get_db() -> Generator[Session, None, None]:
    db = postgres()
    try:
        yield db
    finally:
        db.close()