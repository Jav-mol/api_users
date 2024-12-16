from crud.users_books import insert_user_book_db
from crud.books import insert_book_db

from services.users_books_services import insert_user_book
from services.users_services import service_create_user

from db.psql.get_db import get_db__psql_override
from db.mongodb.get_db import get_db_mongo_override

from schemas.users_books import UserBook
from schemas.books import Book
from schemas.users import UserCreate

from pymongo.collection import Collection
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
                {"book_id":1,"user_id":1},
                {"book_id":1,"user_id":2},
                {"book_id":2,"user_id":1},
                {"book_id":3,"user_id":2},
                {"book_id":4,"user_id":3},
                {"book_id":5,"user_id":3}
            ]

users = [
    {"username": "Javier", "password": "1234", "email": "javi@gmail.com"},
    {"username": "Azul", "password": "4321", "email": "azul@gmail.com"},
    {"username": "Lucas", "password": "pass5678", "email": "lucas@hotmail.com"},
    {"username": "Martina", "password": "martina2024", "email": "martina@yahoo.com"},
    {"username": "Tomás", "password": "tomaspass", "email": "tomas123@gmail.com"},
    {"username": "Camila", "password": "camipassword", "email": "camila_99@hotmail.com"},
    {"username": "Santiago", "password": "santi_321", "email": "santi@mail.com"},
    {"username": "Valentina", "password": "valen@2023", "email": "valentina.v@outlook.com"},
    {"username": "Mateo", "password": "mateo4321", "email": "mateo.t@gmail.com"},
    {"username": "Sofía", "password": "sofia2020", "email": "sofia_02@yahoo.com"},
]


@pytest.fixture
def db_psql():
    db = get_db__psql_override()
    with db as connect:       
        for user_book in users_books_list:
            insert_user_book_db(db=connect, user_book=UserBook(**user_book))

        for book in books:
            insert_book_db(db=connect, book=Book(**book))

        yield connect

@pytest.fixture
def db_mongo():
    db = get_db_mongo_override()
    
    for user in users:    
        service_create_user(db=db, user=UserCreate(**user))
    return db


def test_insert_book_db_success(db_psql: Connection, db_mongo: Collection):
    user_book = insert_user_book(db_psql=db_psql, db_mongo=db_mongo, user_id=1, book_id=10)

    assert user_book.book_id == 10
    assert user_book.user_id == 1


def test_insert_book_db_fail_user(db_psql: Connection, db_mongo: Collection):
    with pytest.raises(HTTPException, match="User not exists"):
        user_book = insert_user_book(db_psql=db_psql, db_mongo=db_mongo, user_id=11, book_id=10)


def test_insert_book_db_fail_book(db_psql: Connection, db_mongo: Collection):
    with pytest.raises(HTTPException, match="Book not exists"):
        user_book = insert_user_book(db_psql=db_psql, db_mongo=db_mongo, user_id=1, book_id=11)
