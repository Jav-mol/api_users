from fastapi.testclient import TestClient
from fastapi import FastAPI
from pprint import pprint 

from api.routers.books import router
from api.routers.books import  get_current_user
from api.routers.auth import Token

from services.books_services import read_books

from db.psql.get_db import get_db_psql, get_db__psql_override

from schemas.users import UserCreate, UserDB, UserOutput
from schemas.books import Book
from schemas.users_books import UserBook

from utils.security import get_access_token

from crud.users_books import insert_user_book_db
from crud.books import insert_book_db

import pytest


app = FastAPI()
app.include_router(router)
client = TestClient(app)


def get_current_user_override():
    data = {"sub":"Javier", "role":"admin", "id":1}
    token = get_access_token(data=data)
    user = get_current_user(token)
    return user


def get_db_psql_override_2():
    db = get_db__psql_override()
    with db as connect:       
        for user_book in users_books_list:
            insert_user_book_db(db=connect, user_book=UserBook(**user_book))
        for book in books:
            insert_book_db(db=connect, book=Book(**book))
        yield connect


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
                {"book_id":7,"user_id":1},
                {"book_id":9,"user_id":1},
                {"book_id":9,"user_id":2},
                {"book_id":5,"user_id":3}
            ]


app.dependency_overrides[get_current_user] = get_current_user_override
app.dependency_overrides[get_db_psql] = get_db_psql_override_2


def test_get_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json()) ==10


def test_create_book():
    response = client.post("/books", json={"title":"book1", "author":"author1"})
    assert response.json()["id"] == 11
    assert response.json()["title"] == "book1"


def test_delete_book():
    response = client.delete(f"/books/{2}") 
    assert response.json()["id"] == 2
    assert response.status_code == 200


def test_update_book_success():
    response = client.put(f"/books/{2}", json={"title":"book_updated","author":"yo"})
    assert response.json()[0]["id"] == 2
    assert response.json()[0]["title"] == "book_updated"
    assert response.status_code == 200


def test_update_book_fail():
    response = client.put(f"/books/{3}", json={"title":"book_updated","author":"yo"})
    assert response.json() == {'detail': 'Book invalid'}
    assert response.status_code == 401
