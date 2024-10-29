from db.psql.get_db import get_db__psql_override
from crud.books import check_book_exists, insert_book_db, read_books_db

from schemas.books import Book
from db.psql.models.books import books

from sqlalchemy import Connection
from pprint import pprint
import pytest

@pytest.fixture
def connection():
    db = get_db__psql_override()
    with db as connect:
        yield connect

@pytest.fixture
def list_books():
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
    return books


def test_check_book_exists(connection: Connection, list_books: list):
    for book in list_books:
        insert_book_db(db=connection, book=Book(**book))
    
    book_exist = check_book_exists(db=connection, book=Book(title="Los Miserables", author="Victor Hugo"))
    print(book_exist)
    
def test_insert_book_db(connection: Connection, list_books: list):
    book = Book(**list_books[0])
    book_db = insert_book_db(db=connection, book=book)
    print(book_db[0])