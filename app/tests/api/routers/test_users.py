from fastapi.testclient import TestClient
from fastapi import FastAPI
from pprint import pprint 


from api.routers.users import router

from api.routers.auth import Token
from api.routers.users import  get_current_user
from schemas.users import UserCreate, UserDB, UserOutput
from services.users_services import service_create_user
from db.mongodb.get_db import get_db_mongo, get_db_mongo_override
from db.psql.get_db import get_db_psql, get_db__psql_override

from schemas.books import Book
from schemas.users_books import UserBook


from crud.users_books import insert_user_book_db
from crud.books import insert_book_db


import pytest

app = FastAPI()
app.include_router(router)
client = TestClient(app)


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


def db_mongo_override():
    db = get_db_mongo_override()
    
    for user in users:    
        service_create_user(db=db, user=UserCreate(**user))
    return db

from utils.security import get_access_token


def get_current_user_override():
    data = {"sub":"Javier", "role":"admin"}
    access_token = get_access_token(data=data)
    
    token = Token(access_token=access_token)
    user = get_current_user(token)
    
    return user


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


def get_db_psql_override_2():
    db = get_db__psql_override()
    with db as connect:       
        for user_book in users_books_list:
            insert_user_book_db(db=connect, user_book=UserBook(**user_book))
        
        for book in books:
            insert_book_db(db=connect, book=Book(**book))

        yield connect


app.dependency_overrides[get_db_mongo] = db_mongo_override
app.dependency_overrides[get_current_user] = get_current_user_override
app.dependency_overrides[get_db_psql] = get_db_psql_override_2


@pytest.fixture
def test_user():
    user = UserCreate(username="Javi", password="1234", email="Jav@gmail.com")
    return user.model_dump()


def test_create_user_success(test_user):
    response = client.post("/users", json=test_user)
    assert response.json()["id"] == 11
    assert response.json()["username"] == "Javi"


def test_create_user_fail():
    user = UserCreate(username="Javier", password="1234", email="Jav@gmail.com")
    response = client.post("/users", json=user.model_dump())
    assert response.status_code == 401


def test_get_users():
    response = client.get("/users")
    assert len(response.json()) == 10
    assert response.status_code == 200
    #pprint(response.json(), sort_dicts=False)


def test_delete_user():
    response = client.delete(f"/users/{1}")
    assert response.status_code == 200
    assert response.json()["User deleted"] == {"id":1,"username":"Javier"}


def test_update_role():
    response = client.put(f"/users/{1}?role={'admin'}")

    assert response.status_code == 200
    assert response.json()["rol"] == "admin"


def test_get_user():
    
    response = client.get(f"/users/{2}")
    
    assert response.status_code == 200
    assert response.json()["username"] == "Azul"
    #pprint(response.json(), sort_dicts=False)
