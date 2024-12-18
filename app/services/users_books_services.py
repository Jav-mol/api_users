from crud.users_books import check_user_book_exist, read_users_books_by_user_id
from crud.users_books import insert_user_book_db, get_books_by_id_user

from crud.users import get_user_by_id_db
from crud.books import read_book_db_by_id

from schemas.users_books import UserBook, UserBookDict

from sqlalchemy import Connection
from pymongo.collection import Collection
from fastapi import HTTPException
from pprint import pprint

def insert_user_book(db_psql: Connection, db_mongo: Collection, user_id: int ,book_id: int):
    user_book = UserBook(user_id=user_id, book_id=book_id)
    if check_user_book_exist(db=db_psql, book_id=user_book.book_id, user_id=user_book.user_id):
        raise HTTPException(404, "User-book already exists")
    if not read_book_db_by_id(db=db_psql, id=user_book.book_id):
        raise HTTPException(404, "Book not exists")
    if not get_user_by_id_db(collection=db_mongo, id=user_book.user_id):
        raise HTTPException(404, "User not exists")
        
    insert_user_book_db(db=db_psql, user_book=user_book)    
    return user_book


def read_user_book_by_id(db_mongo: Collection, db_psql: Connection, id_user: int):
    if not get_user_by_id_db(collection=db_mongo, id=id_user):
        raise HTTPException(404, "User not exists")
    
    user_db = get_user_by_id_db(collection=db_mongo, id=id_user)
    user_db["id"] = user_db.pop("_id")

    books = get_books_by_id_user(db=db_psql, user_id=id_user)
    user_db["books"] = books
    
    user_book = UserBookDict(**user_db)
    
    pprint(user_book.model_dump(), sort_dicts=False)