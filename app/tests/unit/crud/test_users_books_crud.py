from db.psql.get_db import get_db__psql_override
from crud.users_books import insert_user_book_db, read_users_books_by_user_id
from crud.books import check_book_exists, insert_book_db, read_books_db, delete_book_db
from schemas.users_books import UserBook
from schemas.books import Book

from sqlalchemy import Connection
from pprint import pprint
import pytest

users_books_list = [
                {"book_id":1,"user_id":1},
                {"book_id":1,"user_id":2},
                {"book_id":2,"user_id":1},
                {"book_id":3,"user_id":2},
                {"book_id":4,"user_id":3},
                {"book_id":5,"user_id":3}
            ]

@pytest.fixture
def connection():
    db = get_db__psql_override()
    with db as connect:       
        for user_book in users_books_list:
            insert_user_book_db(db=connect, user_book=UserBook(**user_book))
        yield connect


def test_insert_user_book_db(connection: Connection):#, users_books_list: list):
    
    book_dict = UserBook(book_id=1, user_id=1)
    user_book_db = insert_user_book_db(db=connection, user_book=book_dict)
    
    assert user_book_db == 1


def test_read_users_books_db(connection: Connection):
    users_books_db = read_users_books_by_user_id(db=connection, user_id=1)

    print()
    
    #print(users_books_list)
    print(users_books_db)
    
    #for i,o in zip(users_books_db, users_books_list):
    #    print(f"I: {i} -- O: {o}")
