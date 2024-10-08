from crud.users import user_already_exists, next_id
from crud.users import insert_user_db
from crud.users import get_user_by_id, get_users
from crud.users import update_user
from crud.users import delete_user


from db.mongodb.get_db import get_db_mongo_override
from unittest.mock import patch, MagicMock
from schemas.users import UserDB, UserCreate

users = [
            {"_id":1,"username":"Nico", "password":"4321", "email": "nico@gmail.com"},
            {"_id":2,"username":"Cami", "password":"abcd", "email": "cami@gmail.com"},
            {"_id":3,"username":"Azul", "password":"1357", "email": "azul@gmail.com"}
        ]

user_dict = {"id":4,"username":"Javier", "password":"1234", "email":"javi@gmail.com"}

user = UserDB(**user_dict)

def test_next_id():
    coll = get_db_mongo_override()

    result = next_id(coll)
    assert result == 1

    coll.insert_many(users)
    result = next_id(coll)
    assert result == 4

    coll.insert_one({"_id":22,"username":"Javier","age":22})
    result = next_id(coll)
    assert result == 23


def test_user_already_exist():
    coll = get_db_mongo_override()
    
    coll.insert_one(user_dict)

    assert user_already_exists(coll,"Javier") == True
    assert user_already_exists(coll,"Javier2") == False


def test_insert_user_db():
    coll = get_db_mongo_override()

    user_db = user.model_dump()
    user_db["_id"] = user_db.pop("id")

    assert insert_user_db(coll, user_db) == 4


def test_get_user_by_id_success():
    coll = get_db_mongo_override()

    user_dict["_id"] = user_dict.pop("id")
    insert_user_db(coll, user_dict)

    user_db = get_user_by_id(coll, 4) 
    user_db["id"] = user_db.pop("_id")

    assert UserDB(**user_db) == user


def test_get_user_by_id_fail():
    coll = get_db_mongo_override()

    user_db = get_user_by_id(coll, 1) 

    assert user_db == None 



def test_get_users():    
    coll = get_db_mongo_override()
    coll.insert_many(users)

    users_db = get_users(coll)
    users_list = []

    for user in users_db:
        user["id"] = user.pop("_id")
        users_list.append(UserDB(**user))

    assert len(users_list) == 3


def test_update_user():        
    coll = get_db_mongo_override()
    coll.insert_many(users)

    new_user = {"username":"Javier", "password":"1234", "email":"javi@gmail.com"}

    result = update_user(coll, new_user, 1)
    
    assert result["username"] == "Javier"
    assert result["password"] == "1234"
    assert result["email"] == "javi@gmail.com"


def test_delete_user():
        coll = get_db_mongo_override()
        coll.insert_many(users)

        result = delete_user(coll, 3)
        
        assert result == 1