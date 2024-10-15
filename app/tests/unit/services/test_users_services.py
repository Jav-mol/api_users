from services.users_services import create_user
from services.users_services import read_users


from pymongo.collection import Collection
from db.mongodb.get_db import get_db_mongo_override
from schemas.users import UserCreate, UserDB, UsersToList, UserDict
from pprint import pprint
import pytest

@pytest.fixture
def collection():
    return get_db_mongo_override()


def test_create_user_db_success(collection: Collection):
    
    user_input_1 = {"username":"Javier", "password":"1234", "email":"javi@gmail.com"}
    user_input_2 = {"username":"Azul", "password":"4321", "email":"azul@gmail.com"}

    result = create_user(collection, UserCreate(**user_input_1))
    result_2 = create_user(collection, UserCreate(**user_input_2))

    assert result.model_dump() == {"id":1,"username":"Javier"} 
    assert result_2.model_dump() == {"id":2,"username":"Azul"} 


def test_create_user_db_fail(collection: Collection):

    user_input = {"username":"Javier", "password":"1234", "email":"javi@gmail.com"}
    result = create_user(collection, UserCreate(**user_input))

    with pytest.raises(ValueError, match="User already exist"):
        result_2 = create_user(collection, UserCreate(**user_input))


def test_get_users(collection: Collection):

    user_input_1 = {"username":"Javier", "password":"1234", "email":"javi@gmail.com"}
    user_input_2 = {"username":"Azul", "password":"4321", "email":"azul@gmail.com"}

    create_user(collection, UserCreate(**user_input_1))
    create_user(collection, UserCreate(**user_input_2))

    users = read_users(db=collection)
    #pprint(users, sort_dicts=False)
    
    assert users[0]["Javier"]["id"] == 1
    assert users[1]["Azul"]["id"] == 2

