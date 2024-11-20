from crud.users_books import check_user_book_exist, read_users_books_by_user_id
from crud.users_books import insert_user_book_db

from schemas.users_books import UserBook
from sqlalchemy import Connection


def insert_user_book(db: Connection, user_id: int ,book_id: int):
    user_book = UserBook(user_id=user_id, book_id=book_id)
    if check_user_book_exist(db=db, book_id=user_book.book_id, user_id=user_book.user_id):
        raise ValueError("User-book already exists")
    
    insert_user_book_db(db=db, user_book=user_book)    
    return user_book