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



@pytest.fixture
def test_user():
    user = UserCreate(username="Javi2", password="1234", email="Jav@gmail.com")
    return user.model_dump()

#@pytest.fixture
def override_get_db_mongo():
    db = get_db_mongo_override()
    
    user = UserDB(username="Javi", password="1234", email="Jav@gmail.com")
    print(user.model_dump())
    insert_user_db(collection=db, user=user.model_dump())
    
    return db

app.dependency_overrides[get_db_mongo] = override_get_db_mongo


def test_create_user(test_user):

    response = client.post("/users", json=test_user)
    #response2 = client.post("/users", json=test_user)
    
    #print(response2.json())
    print(response.json())