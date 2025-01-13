from db.psql.get_db import get_db__psql_override

from crud.users_books import insert_user_book_db
from crud.users_books import read_users_books_by_user_id, check_user_book_exist, read_users_books_by_book_id, get_books_by_id_user
from crud.users_books import delete_user_book

from crud.books import insert_book_db

from schemas.users_books import UserBook
from schemas.books import Book

from sqlalchemy import Connection
from pprint import pprint
import pytest


books = [
            {"author": "Victor Hugo", "title": "Los Miserables"},
            {"author": "Fiódor Dostoyevski", "title": "Crimen y Castigo"},
            {"author": "George Orwell", "title": "1984"},
            {"author": "Gabriel García Márquez", "title": "Cien años de soledad"},
            {"author": "Jane Austen", "title": "Orgullo y prejuicio"},
            {"author": "J. D. Salinger", "title": "El guardián entre el centeno"},
            {"author": "Franz Kafka", "title": "La metamorfosis"},
            {"author": "Ernest Hemingway", "title": "El viejo y el mar"},
            {"author": "Hermann Hesse", "title": "Siddhartha"},
            {"author": "Antoine de Saint-Exupéry", "title": "El principito"}
        ]


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
        
        for book in books:
            insert_book_db(db=connect, book=Book(**book))

        yield connect


def test_insert_user_book_db(connection: Connection):#, users_books_list: list):
    book_dict = UserBook(book_id=1, user_id=1)
    user_book_db = insert_user_book_db(db=connection, user_book=book_dict)
    assert user_book_db == 1


def test_read_users_books_db(connection: Connection):
    users_books_db = read_users_books_by_user_id(db=connection, user_id=1)
    assert len(users_books_db) == 2


def test_check_user_book_exist(connection: Connection):
    user_book = check_user_book_exist(db=connection, user_id=1, book_id=2)
    assert user_book == True
    
    user_book_2 = check_user_book_exist(db=connection, user_id=1, book_id=4)
    assert user_book_2 == False


def test_delete_user_book(connection: Connection):
    user_book_deleted = delete_user_book(db=connection, user_id=1)
    assert user_book_deleted == 2


def test_get_books_by_id_user(connection: Connection):
    books = get_books_by_id_user(db=connection, user_id=1)
    assert len(books) == 2 
