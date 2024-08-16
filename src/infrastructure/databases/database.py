
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from src.config.config import get_config


def postgres() -> Session:
    config = get_config()
    engine = create_engine(
        f"postgresql+psycopg2://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    )
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
    db = session_local()
    return db