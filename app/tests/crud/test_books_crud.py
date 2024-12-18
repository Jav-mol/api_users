from db.psql.get_db import get_db__psql_override
from crud.books import check_book_exists, insert_book_db, read_books_db, read_book_db_by_id, delete_book_db
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


def test_check_book_exists(connection: Connection, books_list: list):
    insert_book_db(db=connection, book=Book(**books_list[0]))
    
    book_exist = check_book_exists(db=connection, book=Book(title="Los Miserables", author="Victor Hugo"))
    assert book_exist == True
    
    book_exist_2 = check_book_exists(db=connection, book=Book(title="Los Miserables2", author="Victor Hugo"))
    assert book_exist_2 == False
    
    
def test_insert_book_db(connection: Connection, books_list: list):
    book = Book(**books_list[0])
    book_id = insert_book_db(db=connection, book=book)
    assert book_id == 1


def test_read_books_db(connection: Connection, books_list: list):
    for book in books_list:
        insert_book_db(db=connection, book=Book(**book))
    
    books_db = read_books_db(db=connection)
    assert len(books_db) == 10


def test_read_book_by_id(connection: Connection, books_list: list):
    for book in books_list:
        insert_book_db(db=connection, book=Book(**book))
    
    book = read_book_db_by_id(db=connection, id=1)

    assert book[0]["id"] == 1
    
def test_delete_book_db(connection: Connection, books_list: list):
    insert_book_db(db=connection, book=Book(**books_list[0]))
    
    book_deleted = delete_book_db(db=connection, id_book=1)
    
    assert book_deleted == 1
    