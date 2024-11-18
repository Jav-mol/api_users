from services.books_services import create_book


from db.psql.get_db import get_db__psql_override
from schemas.books import Book
from sqlalchemy import Connection
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
    result = create_book(db=connection, book=Book(title="Javi", author="Javi"))
    
    #assert result == 1
