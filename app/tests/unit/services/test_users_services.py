from services.users_services import create_user_db
from db.mongodb.get_db import get_db_mongo_override
from schemas.users import UserCreate, UserDB
import pytest

user_input = {"username":"Javier", "password":"1234", "email":"javi@gmail.com"}

def test_create_user_db_success():
    coll = get_db_mongo_override()
    
    result = create_user_db(coll, UserCreate(**user_input))
    
    assert result.model_dump() == {"id":1,"username":"Javier"} 
    
def test_create_user_db_fail():
    coll = get_db_mongo_override()

    create_user_db(coll, UserCreate(**user_input))

    with pytest.raises(ValueError, match="User already exist"):
        create_user_db(coll, UserCreate(**user_input))
