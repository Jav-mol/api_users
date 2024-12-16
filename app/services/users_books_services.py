from crud.users_books import check_user_book_exist, read_users_books_by_user_id
from crud.users_books import insert_user_book_db

from crud.users import get_user_by_id_db
from crud.books import read_book_db_by_id

from schemas.users_books import UserBook

from sqlalchemy import Connection
from pymongo.collection import Collection
from fastapi import HTTPException


def insert_user_book(db: Connection, user_id: int ,book_id: int):
    user_book = UserBook(user_id=user_id, book_id=book_id)
    if check_user_book_exist(db=db, book_id=user_book.book_id, user_id=user_book.user_id):
        raise ValueError("User-book already exists")
    print(read_book_db_by_id(db=db, id=user_book.book_id))
    
    insert_user_book_db(db=db, user_book=user_book)    
    return user_book


def read_user_book_by_id(db_mongo: Collection, db_psql: Connection, id: int):
    user = get_user_by_id_db(collection=db_mongo, id=id)
    
    print(user)
    
    user_book = read_users_books_by_user_id(db=db_psql, user_id=id)
    
    print(user_book)