from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer

from datetime import datetime, timedelta, timezone
from core.config import Setting
from typing import Annotated

import jwt
import bcrypt

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

setting = Setting()


def get_hashed_password(password: str):
    hashed_password = bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt())
    return hashed_password.decode()


def verify_hashed_password(hashed_password: str, password: str):
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password.encode())


def get_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    access_token = jwt.encode(to_encode, setting.secret_key, setting.algorithm)
    return access_token


def decode_token(token: str):
    try:
        data = jwt.decode(token , setting.secret_key, setting.algorithm)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
    return data 


def get_current_user(token: Annotated[str, Depends(oauth2)]) -> dict:
    user = decode_token(token)
    return user