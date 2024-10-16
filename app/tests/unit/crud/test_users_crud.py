from crud.users import username_already_exists, next_id # --> Others
from crud.users import insert_user_db # --> Create 
from crud.users import get_user_by_username_db, get_user_by_id_db, get_users_db, id_exist # --> Read
from crud.users import update_user_db # --> Update
from crud.users import delete_user_db, delete_many_users_db # --> Delete

from pymongo.collection import Collection
from db.mongodb.get_db import get_db_mongo_override
from schemas.users import UserDB
import pytest

@pytest.fixture
def users_dict():
    users = [
                {"_id":1,"username":"Nico", "password":"4321", "email": "nico@gmail.com"},
                {"_id":2,"username":"Cami", "password":"abcd", "email": "cami@gmail.com"},
                {"_id":3,"username":"Azul", "password":"1357", "email": "azul@gmail.com"}
            ]
    return users

@pytest.fixture
def user_dict():
    return {"id":4,"username":"Javier", "password":"1234", "email":"javi@gmail.com"}


@pytest.fixture
def collection():
    return get_db_mongo_override()


def test_next_id(collection: Collection, users_dict):
    
    result = next_id(collection)
    assert result == 1

    collection.insert_many(users_dict)
    result = next_id(collection)
    assert result == 4

    collection.insert_one({"_id":22,"username":"Javier","age":22})
    result = next_id(collection)
    assert result == 23


def test_id_exist(collection: Collection, user_dict):
    #user_dict_test = user_dict.copy()
    
    insert_user_db(collection, user_dict)

    assert id_exist(collection, 4) == True
    assert id_exist(collection, 5) == None


def test_user_already_exist(collection: Collection, user_dict):
    collection.insert_one(user_dict)

    assert username_already_exists(collection,"Javier") == True
    assert username_already_exists(collection,"Nico") == None


def test_insert_user_db(collection: Collection, user_dict):
    user = UserDB(**user_dict)

    user_db = user.model_dump()    
    assert insert_user_db(collection, user_db) == 4


def test_get_user_by_username_success(collection: Collection, user_dict):  
    user = UserDB(**user_dict)

    insert_user_db(collection, user_dict)  
    user_db = get_user_by_username_db(collection, "Javier")

    assert UserDB(**user_db) == user


def test_get_user_by_username_fail(collection: Collection):
    result = get_user_by_username_db(collection, "Javier2") 
    assert result == None


def test_get_user_by_id_success(collection: Collection, user_dict):  
    user = UserDB(**user_dict)

    insert_user_db(collection, user_dict)  
    user_db = get_user_by_id_db(collection, 4)

    assert UserDB(**user_db) == user


def test_get_user_by_id_fail(collection: Collection):
    result = get_user_by_id_db(collection, 1) 
    assert result == None


def test_get_users(collection: Collection, users_dict):   
    collection.insert_many(users_dict)

    users_db = get_users_db(collection)
    users_list = []

    for user in users_db:
        user["id"] = user.pop("_id")
        users_list.append(UserDB(**user))

    assert len(users_list) == 3
    assert users_list[0].id == 1
    assert users_list[1].id == 2
    assert users_list[2].id == 3


def test_update_user_success(collection: Collection, users_dict):       
    collection.insert_many(users_dict)

    new_user = {"username":"Javier", "password":"1234", "email":"javi@gmail.com"}
    result = update_user_db(collection, new_user, 1)

    assert result["username"] == "Javier"
    assert result["password"] == "1234"
    assert result["email"] == "javi@gmail.com"


def test_update_user_fail(collection: Collection):       

    new_user = {"username":"Javier", "password":"1234", "email":"javi@gmail.com"}
    result = update_user_db(collection, new_user, 1)

    assert result == None


def test_delete_user_success(collection: Collection, users_dict):
        collection.insert_many(users_dict)

        result = delete_user_db(collection, 3)
        assert result == 1


def test_delete_user_fail(collection: Collection):
        result = delete_user_db(collection, 1)
        assert result == 0


def test_delete_many_users_success(collection: Collection, users_dict):
        collection.insert_many(users_dict)

        ids = [1,2,3]
        result = delete_many_users_db(collection, ids)

        assert result == 3


def test_delete_many_users_fail(collection: Collection):
        result = delete_many_users_db(collection, [1,2,3])
        assert result == 0
