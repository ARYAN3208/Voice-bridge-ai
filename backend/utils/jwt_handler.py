from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt

from config import settings
from backend.utils.constants import JWT_ALGORITHM


class JWTHandler:

    @staticmethod
    def create_access_token(
        data: dict[str, Any],
        expires_delta: timedelta | None = None,
    ) -> str:
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + (
            expires_delta
            if expires_delta
            else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )

        to_encode.update({"exp": expire, "type": "access"})

        return jwt.encode(
            to_encode,
            settings.SECRET_KEY,
            algorithm=JWT_ALGORITHM,
        )

    @staticmethod
    def create_refresh_token(
        data: dict[str, Any],
        expires_delta: timedelta | None = None,
    ) -> str:
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + (
            expires_delta
            if expires_delta
            else timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        )

        to_encode.update({"exp": expire, "type": "refresh"})

        return jwt.encode(
            to_encode,
            settings.SECRET_KEY,
            algorithm=JWT_ALGORITHM,
        )

    @staticmethod
    def decode_token(token: str) -> dict | None:
        try:
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[JWT_ALGORITHM],
            )
            return payload

        except JWTError:
            return None

    @staticmethod
    def verify_access_token(token: str) -> dict | None:
        payload = JWTHandler.decode_token(token)

        if not payload:
            return None

        if payload.get("type") != "access":
            return None

        return payload

    @staticmethod
    def verify_refresh_token(token: str) -> dict | None:
        payload = JWTHandler.decode_token(token)

        if not payload:
            return None

        if payload.get("type") != "refresh":
            return None

        return payload

    @staticmethod
    def get_user_id(token: str) -> int | None:
        payload = JWTHandler.verify_access_token(token)

        if not payload:
            return None

        return payload.get("user_id")