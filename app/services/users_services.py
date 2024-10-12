from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput

from crud.users import username_already_exists, next_id, id_exist # --> Others
from crud.users import insert_user_db # --> Create 
from crud.users import get_user_by_username, get_users # --> Read
from crud.users import update_user # --> Update
from crud.users import delete_user, delete_many_users # --> Delete

from utils.security import get_hashed_password

def create_user_db(db: Collection, user: UserCreate) -> UserOutput:
    if username_already_exists(collection=db, username=user.username):
        raise ValueError("User already exist")
    
    user.password = get_hashed_password(user.password) 
    
    user_db = UserDB(**user.model_dump())
    user_db.id = next_id(collection=db)
    
    id = insert_user_db(collection=db, user=user_db.model_dump())
    
    user_inserted = db.find_one({"_id":id})
    user_inserted["id"] = user_inserted.pop("_id")
    
    return UserOutput(**user_inserted)


def read_users(db: Collection) -> list:
    users = get_users(collection=db)
    return users


def read_user_by_username(db: Collection, username: str) -> UserOutput:
    user = get_user_by_username(collection=db, username=username)
    if not user:
        raise ValueError("Id not exist")
    return user
