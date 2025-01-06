from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from api.routers.auth import Token
from schemas.users import UserCreate, UserDB, UserOutput, UsersToDict, UserUpdate
from schemas.books import Book, BookDate

from db.mongodb.get_db import get_db_mongo
from db.psql.get_db import get_db_psql

from services.users_services import service_dalete_user, read_user_by_username, service_update_user
from services.users_books_services import read_user_book_by_id
from services.books_services import create_book, delete_book, update_book_service

from crud.users_books import delete_user_book, get_books_by_id_user

from sqlalchemy import Connection
from pymongo.collection import Collection
from typing import Annotated, Literal
from utils.security import decode_token

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter(
    prefix="/user"
)

def get_current_user(token: Annotated[Token, Depends(oauth2)]) -> dict:
    token_dict = token.model_dump()
    data = token_dict.get("access_token") 
    user = decode_token(data)
    return user 


@router.get("", status_code=200, response_model=UsersToDict)
async def get_user(db: Annotated[Collection, Depends(get_db_mongo)], user: Annotated[dict, Depends(get_current_user)]):
    current_user = read_user_by_username(db=db, username=user.get("sub"))
    return current_user


@router.put("", status_code=200, response_model=UsersToDict)
async def update_user(user_update: UserCreate, db: Annotated[Collection, Depends(get_db_mongo)], user: Annotated[dict, Depends(get_current_user)]):    
    user_updated = service_update_user(id=user["id"], db=db, user=UserUpdate(**user_update.model_dump()))
    user_in_db = read_user_by_username(db=db, username=user_updated.username)
    return user_in_db


@router.delete("", status_code=200, response_model=UserOutput)
async def delete_user(db: Annotated[Collection, Depends(get_db_mongo)], user: Annotated[dict, Depends(get_current_user)]):
    user_deleted = service_dalete_user(user["id"], db=db)
    return user_deleted


@router.get("/books", status_code=200, response_model=list[Book])
async def get_all_book_for_user(user: Annotated[dict, Depends(get_current_user)], db_psql: Annotated[Connection, Depends(get_db_psql)]):
    books = get_books_by_id_user(db=db_psql, user_id=user["id"])
    return books


@router.post("/books", status_code=200, response_model=Book)
async def create_book_router(book: Book, user: Annotated[dict, Depends(get_current_user)], db_psql: Annotated[Connection, Depends(get_db_psql)]):
    book = create_book(db=db_psql, book=book)
    return book[0]


@router.delete("/books/{id}", status_code=200, response_model=Book)
async def delete_book_router(id: int, user: Annotated[dict, Depends(get_current_user)], db_psql: Annotated[Connection, Depends(get_db_psql)]):
    book_deleted = delete_book(db=db_psql, id=id)
    return book_deleted[0]


@router.put("/books/{id}", status_code=200)
async def update_book_by_id(id: int, book: Book, user: Annotated[dict, Depends(get_current_user)], db_psql: Annotated[Connection, Depends(get_db_psql)]):
    
    print(user)
    
    book_updated = update_book_service(db=db_psql, id_book=id, id_user=user.get("id"), book=book)
    
    return book_updated

