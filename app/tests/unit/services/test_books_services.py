from services.books_services import create_book, read_books, delete_book, read_book_db_by_id

from db.psql.get_db import get_db__psql_override
from schemas.books import Book
from sqlalchemy import Connection
from pprint import pprint
import pytest


@pytest.fixture
def connection():
    db = get_db__psql_override()
    with db as connect:
        yield connect

@pytest.fixture
def books_list():
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


def test_create_book_success(connection: Connection, books_list):
    result = create_book(db=connection, book=Book(**books_list[0]))
    result2 = create_book(db=connection, book=Book(**books_list[1]))
    
    assert result == 1
    assert result2 == 2


def test_create_book_fail(connection: Connection, books_list):
    result = create_book(db=connection, book=Book(**books_list[0]))
    result2 = create_book(db=connection, book=Book(**books_list[0]))
    
    assert result2 == "Book already exists"


def test_read_books(connection: Connection, books_list):
    for book in books_list:
        create_book(db=connection, book=Book(**book))
    books = read_books(db=connection)
    assert len(books) == 10


def test_delete_book(connection: Connection, books_list):
    for book in books_list:
        create_book(db=connection, book=Book(**book))
    
    book_id = read_book_db_by_id(db=connection, id=10)
    book_deleted = delete_book(db=connection, id=10)
    assert book_id == book_deleted