from services.users_services import create_user
from services.users_services import read_users
from services.users_services import read_user_by_username
from services.users_services import update_user


from pymongo.collection import Collection
from db.mongodb.get_db import get_db_mongo_override
from schemas.users import UserCreate, UserDB, UsersToList, UserUpdate
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
    
    result = create_user(collection, UserCreate(**users_list[0]))
    result_2 = create_user(collection, UserCreate(**users_list[1]))

    assert result.model_dump() == {"id":1,"username":"Javier"} 
    assert result_2.model_dump() == {"id":2,"username":"Azul"} 


def test_create_user_db_fail(collection: Collection, users_list):
    create_user(collection, UserCreate(**users_list[0]))
    
    with pytest.raises(ValueError, match="User already exist"):
        create_user(collection, UserCreate(**users_list[0]))


def test_get_users(collection: Collection, users_list):

    create_user(collection, UserCreate(**users_list[0]))
    create_user(collection, UserCreate(**users_list[1]))

    users = read_users(db=collection)
    #pprint(users, sort_dicts=False)
    
    assert users[0]["Javier"]["id"] == 1
    assert users[1]["Azul"]["id"] == 2


def test_read_user_by_username():
    pass


def test_update_user(collection: Collection, users_list):
    create_user(collection, UserCreate(**users_list[0]))
    
    user_new = UserUpdate(username="JAVIER", password="password")
    
    user_updated = update_user(id=1, db=collection, user=user_new)
    
    print(user_updated)