from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from api.routers.auth import Token
from schemas.users import UserCreate, UserDB, UserOutput, UsersToDict

from db.mongodb.get_db import get_db_mongo
from db.psql.get_db import get_db_psql

from services.users_services import service_create_user, service_dalete_user, read_user_by_username
from services.users_books_services import read_user_book_by_id

from crud.users_books import delete_user_book

from sqlalchemy import Connection
from pymongo.collection import Collection
from typing import Annotated, Literal
from utils.security import decode_token

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter(
    prefix="/user2"
)

def get_current_user(token: Annotated[Token, Depends(oauth2)]) -> dict:
    token_dict = token.model_dump()
    data = token_dict.get("access_token") 
    user = decode_token(data)
    return user 


@router.get("", status_code=200)
async def get_user(db: Annotated[Collection, Depends(get_db_mongo)], user: Annotated[dict, Depends(get_current_user)]):

    current_user = read_user_by_username(db=db, username=user.get("sub"))
    
    return current_user
