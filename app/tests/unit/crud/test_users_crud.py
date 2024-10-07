from crud.users import user_already_exists, insert_user_db, next_id, user_by_id
from db.mongodb.get_db import get_db_mongo_override
from unittest.mock import patch, MagicMock
from schemas.users import UserDB

users = [
            {"_id":1,"name":"Nico", "Age":24},
            {"_id":2,"name":"Cami", "Age":25},
            {"_id":3,"name":"Azul", "Age":24}
        ]

user_dict = {"_id":4,"username":"Javier", "password":"1234", "email":"javi@gmail.com"}

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
    
    #print(user)
    
    #user.id = 1
    
    #print(user.model_dump())
    
    assert insert_user_db(coll, user) == 4


def test_user_by_id():
    coll = get_db_mongo_override()
    
    user.id = 1
    
    insert_user_db(coll,user)
    
    
    
    print(user_by_id(coll, 1)) 
    print(user.model_dump())


#def test_user_db():    
#    print(user._id)