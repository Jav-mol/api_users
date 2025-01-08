from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from api.routers.auth import Token
from schemas.users import UserCreate, UserDB, UserOutput, UsersToDict, UserUpdate
from schemas.books import Book, BookDate

from db.mongodb.get_db import get_db_mongo
from db.psql.get_db import get_db_psql

from services.users_services import service_dalete_user, read_user_by_username, service_update_user
from services.users_books_services import read_user_book_by_id
from services.books_services import create_book, delete_book, update_book_service, read_books

from crud.users_books import delete_user_book, get_books_by_id_user

from sqlalchemy import Connection
from pymongo.collection import Collection
from typing import Annotated, Literal
from utils.security import decode_token


oauth2 = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter(
    prefix="/books"
)

def get_current_user(token: Annotated[Token, Depends(oauth2)]) -> dict:
    token_dict = token.model_dump()
    data = token_dict.get("access_token") 
    user = decode_token(data)
    return user 


@router.get("", response_model=list[BookDate])
async def get_all_books(db: Annotated[Connection, Depends(get_db_psql)]):
    books = read_books(db=db)
    return books