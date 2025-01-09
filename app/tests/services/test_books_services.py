from services.books_services import create_book, read_books, delete_book, read_book_db_by_id
from services.users_books_services import insert_user_book, read_user_book_by_id

from crud.books import insert_book_db
from crud.users_books import insert_user_book_db

from schemas.books import Book
from schemas.users_books import UserBook

from db.psql.get_db import get_db__psql_override
from schemas.books import Book
from sqlalchemy import Connection
from fastapi import HTTPException
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
                {"book_id":6,"user_id":1},
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
    result = create_book(db=connection, book=Book(title="Un saco de huesos", author="Stephen King"))
    result2 = create_book(db=connection, book=Book(title="El obstaculo es el camino", author="Ryan Holiday"))
    
    assert result[0]["id"] == 11
    assert result2[0]["id"] == 12


def test_create_book_fail(connection: Connection, books_list):
    result = create_book(db=connection, book=Book(title="Un saco de huesos", author="Stephen King"))
    result2 = create_book(db=connection, book=Book(title="Un saco de huesos", author="Stephen King"))
    
    assert result2 == "Book already exists"


def test_read_books(connection: Connection, books_list):
    for book in books_list:
        create_book(db=connection, book=Book(**book))
    books = read_books(db=connection)
    assert len(books) == 10


def test_delete_book_success(connection: Connection, books_list):
    for book in books_list:
        create_book(db=connection, book=Book(**book))
    
    book_id = read_book_db_by_id(db=connection, id=6)
    
    book_deleted = delete_book(db=connection, id=6)
    assert book_id == book_deleted


def test_delete_book_fail(connection: Connection, books_list):
    with pytest.raises(HTTPException, match="the book can not remove"):        
        book_deleted = delete_book(db=connection, id=10)
