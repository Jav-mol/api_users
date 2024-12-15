from services.users_books_services import insert_user_book

from crud.users_books import insert_user_book_db
from crud.books import insert_book_db

from db.psql.get_db import get_db__psql_override
from db.mongodb.get_db import get_db_mongo_override

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

def test_insert_book_db(connection: Connection):
    pass    