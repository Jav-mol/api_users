from fastapi.testclient import TestClient

from api.routers.users import router

from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput
from services.users_services import insert_user_db
from db.mongodb.get_db import get_db_mongo_override


client = TestClient(router)

def test_create_user():
    user = UserCreate(username="Javi", password="1234", email="Jav@gmail.com")
    
    response = client.post("/users", json={"user":user})
    
    print(response.json())