
from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import SettingsConfigDict


class Config:
    DB_HOST:str
    DB_NAME:str
    DB_PORT:int
    DB_USER:str
    DB_PASSWORD:str
    
    model_config = SettingsConfigDict(env_file=".env")
    
_config = Config | None = None
def load_config():
    global _config
    return load_dotenv()

@lru_cache
def get_config():
    global _config
    if _config is None:
        load_config()
        _config = Config(**_config)
    
    return _config