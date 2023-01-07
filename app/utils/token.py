from datetime import datetime, timedelta

from jose import jwt

from app.core.config import settings


def create_access_token(user_id) -> str:

    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRATION)
    payload = {"user_id": user_id, "exp": expire, "type": "access"}
    encoded_jwt = jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt


def create_refresh_token(user_id) -> str:

    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRATION)
    payload = {"user_id": user_id, "exp": expire, "type": "refresh"}
    encoded_jwt = jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt
