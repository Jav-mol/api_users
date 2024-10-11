from services.users_services import create_user_db
from db.mongodb.get_db import get_db_mongo_override
from schemas.users import UserCreate, UserDB
import pytest


def test_create_user_db_success():
    coll = get_db_mongo_override()
    
    user_input_1 = {"username":"Javier", "password":"1234", "email":"javi@gmail.com"}
    user_input_2 = {"username":"Azul", "password":"4321", "email":"azul@gmail.com"}

    result = create_user_db(coll, UserCreate(**user_input_1))
    result_2 = create_user_db(coll, UserCreate(**user_input_2))

    assert result.model_dump() == {"id":1,"username":"Javier"} 
    assert result_2.model_dump() == {"id":2,"username":"Azul"} 


def test_create_user_db_fail():
    coll = get_db_mongo_override()

    user_input = {"username":"Javier", "password":"1234", "email":"javi@gmail.com"}
    result = create_user_db(coll, UserCreate(**user_input))

    with pytest.raises(ValueError, match="User already exist"):
        result_2 = create_user_db(coll, UserCreate(**user_input))


