from db.psql.get_db import get_db__psql_override
from crud.books import check_book_exists, insert_book_db, read_books_db, delete_book_db
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
    insert_book_db(db=connection, book=Book(**list_books[0]))
    
    book_exist = check_book_exists(db=connection, book=Book(title="Los Miserables", author="Victor Hugo"))
    assert book_exist == True
    
    book_exist_2 = check_book_exists(db=connection, book=Book(title="Los Miserables2", author="Victor Hugo"))
    assert book_exist_2 == False
    
    
def test_insert_book_db(connection: Connection, list_books: list):
    book = Book(**list_books[0])
    book_id = insert_book_db(db=connection, book=book)
    assert book_id == 1


def test_read_books_db(connection: Connection, list_books: list):
    for book in list_books:
        insert_book_db(db=connection, book=Book(**book))
    
    books_db = read_books_db(db=connection)
    assert len(books_db) == 10
    

def test_delete_book_db(connection: Connection, list_books: list):
    insert_book_db(db=connection, book=Book(**list_books[0]))
    
    book_deleted = delete_book_db(db=connection, id_book=1)
    
    assert book_deleted == 1
    