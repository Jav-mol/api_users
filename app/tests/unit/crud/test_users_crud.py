from crud.users import user_already_exists, insert_user_db, next_id
from db.mongodb.get_db import get_db_mongo_override
from unittest.mock import patch, MagicMock

users = [
            {"_id":1,"name":"Nico", "Age":24},
            {"_id":2,"name":"Cami", "Age":25},
            {"_id":3,"name":"Azul", "Age":24}
        ]

user = {"_id":1,"username":"Javier", "Age":22}


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
    coll.insert_one(user)
    
    assert user_already_exists(coll,"Javier") == True
    assert user_already_exists(coll,"Javier2") == False

