from fastapi.testclient import TestClient
from fastapi import Depends, FastAPI
from pprint import pprint 


from api.routers.users import router

from schemas.users import UserCreate, UserDB, UserOutput
from services.users_services import service_create_user
from db.mongodb.get_db import get_db_mongo, get_db_mongo_override

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

app.dependency_overrides[get_db_mongo] = db_mongo_override


@pytest.fixture
def test_user():
    user = UserCreate(username="Javi", password="1234", email="Jav@gmail.com")
    return user.model_dump()


def test_create_user_success(test_user):

    response = client.post("/users", json=test_user)

    assert response.json()["id"] == 11
    assert response.json()["username"] == "Javi"


def test_create_user_fail():
    with pytest.raises(ValueError, match="User already exist"):
        user = UserCreate(username="Javier", password="1234", email="Jav@gmail.com")
        response = client.post("/users", json=user.model_dump())


def test_get_users():
    response = client.get("/users")
    assert len(response.json()) == 10
    #pprint(response.json(), sort_dicts=False)