
from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()

class Config(BaseSettings):
    DB_HOST:str
    DB_NAME:str
    DB_PORT:int
    DB_USER:str
    DB_PASSWORD:str
    
    GOOGLE_BOOK_API_KEY:str
    
    JWT_SECRET_KEY: str
    JWT_EXPIRE_MINUTES: str
    JWT_HASHING_ALGORITHM: str
    
    model_config = SettingsConfigDict(env_file=".env")
    

def get_config():
    return Config()