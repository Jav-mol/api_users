from fastapi.testclient import TestClient
from fastapi import APIRouter, Depends, FastAPI

from api.routers.users import router

from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput
from services.users_services import insert_user_db
from db.mongodb.get_db import get_db_mongo, get_db_mongo_override

import pytest

app = FastAPI()
app.include_router(router)

client = TestClient(app)

app.dependency_overrides[get_db_mongo] = get_db_mongo_override

@pytest.fixture
def test_user():
    user = UserCreate(username="Javi", password="1234", email="Jav@gmail.com")
    
    return user


def test_create_user(test_user):
    
    response = client.post("/users", json=test_user)

    print(response.json())