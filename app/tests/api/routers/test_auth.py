from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.routers.auth import router
from db.mongodb.get_db import get_db_mongo_override, get_db_mongo
from schemas.users import UserCreate
from services.users_services import service_create_user

import python_multipart

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


def test_login_access():
    response = client.post("login", data={"username":"Javier", "password":"1234"})
    print(response.json())
    print(response)