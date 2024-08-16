


from datetime import datetime, timedelta, timezone

import jwt

from src.config.config import get_config


def create_access_token(userId: int):
    config = get_config()
    expire = datetime.now(timezone.utc) + timedelta(minutes=config.JWT_EXPIRE_MINUTES)
    data = {
        "sub": userId,
        "exp": expire
    }
    encoded_jwt = jwt.encode(data, config.JWT_SECRET_KEY, algorithm=config.JWT_HASHING_ALGORITHM)
    return encoded_jwt