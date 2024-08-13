
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from src.config.config import get_config


def postgres(name: str) -> Session:
    config = get_config()
    engine = create_engine(
        "postgresql+psycopg2://{username}:{password}@{host}:{port}/{name}".format(
            config.DB_USER, config.DB_PASSWORD, config.DB_HOST, config.DB_PORT, config.DB_NAME
        )
    )
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = session_local()
    return db