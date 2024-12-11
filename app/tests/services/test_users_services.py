from services.users_services import service_create_user
from services.users_services import service_read_users
from services.users_services import read_user_by_username
from services.users_services import service_update_user
from services.users_services import service_dalete_user
from services.users_services import delete_many_users


from fastapi import HTTPException
from utils.security import verify_hashed_password
from pymongo.collection import Collection
from db.mongodb.get_db import get_db_mongo_override
from schemas.users import UserCreate, UserUpdate
from pprint import pprint
import pytest

@pytest.fixture
def collection():
    return get_db_mongo_override()

@pytest.fixture
def users_list():
    users = [
        {"username":"Javier", "password":"1234", "email":"javi@gmail.com"},
        {"username":"Azul", "password":"4321", "email":"azul@gmail.com"}
    ]
    return users


def test_create_user_db_success(collection: Collection, users_list):
    
    result = service_create_user(collection, UserCreate(**users_list[0]))
    result_2 = service_create_user(collection, UserCreate(**users_list[1]))
    
    assert result.model_dump() == {"id":1,"username":"Javier"} 
    assert result_2.model_dump() == {"id":2,"username":"Azul"} 


def test_create_user_db_fail(collection: Collection, users_list):
    service_create_user(collection, UserCreate(**users_list[0]))
    
    with pytest.raises(HTTPException, match="User already exist"):
        service_create_user(collection, UserCreate(**users_list[0]))


def test_get_users(collection: Collection, users_list):

    service_create_user(collection, UserCreate(**users_list[0]))
    service_create_user(collection, UserCreate(**users_list[1]))

    users = service_read_users(db=collection)
    #pprint(users, sort_dicts=False)
    
    assert users[0]["Javier"]["id"] == 1
    assert users[1]["Azul"]["id"] == 2


def test_read_user_by_username_success(collection: Collection, users_list):
    service_create_user(collection, UserCreate(**users_list[0]))
    user = read_user_by_username(collection, "Javier")
    
    assert user.model_dump()["username"] == "Javier"


def test_read_user_by_username_fail(collection: Collection):
    with pytest.raises(HTTPException, match="Username not exist"):
        read_user_by_username(collection, "Javier")


def test_update_user_success(collection: Collection, users_list):
    service_create_user(collection, UserCreate(**users_list[0]))
    
    user_new = UserUpdate(username="JAVIER", password="password_updated")
    
    user_updated = service_update_user(id=1, db=collection, user=user_new)
    
    assert user_updated.model_dump()["username"] == "JAVIER"
    
    new_password = user_updated.model_dump()["password"]
    assert verify_hashed_password(new_password, "password_updated") == True
    
    
def test_update_user_fail(collection: Collection):
    user_new = UserUpdate(username="JAVIER", password="password_updated")
    with pytest.raises(ValueError, match="Id not exist"):
        service_update_user(id=1, db=collection, user=user_new)
    
    
def test_dalete_user_success(collection: Collection, users_list):
    service_create_user(collection, UserCreate(**users_list[0]))
    
    user_deleted = service_dalete_user(db=collection, id=1)
    assert user_deleted == 1
    
    
def test_dalete_user_fail(collection: Collection):
    with pytest.raises(ValueError, match="Id not exist"):
        service_dalete_user(db=collection, id=1)


def test_delete_many_users_success(collection: Collection, users_list):    
    service_create_user(collection, UserCreate(**users_list[0]))
    service_create_user(collection, UserCreate(**users_list[1]))
        
    count_users_deleted = delete_many_users(db=collection, ids=[1,2])
    assert count_users_deleted == 2


def test_delete_many_users_fail(collection: Collection, users_list):    
    service_create_user(collection, UserCreate(**users_list[0]))
    with pytest.raises(ValueError, match="Id not exist"):
        delete_many_users(db=collection, ids=[1,2])