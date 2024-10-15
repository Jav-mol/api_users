from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput, UserDict, UsersToList

from crud.users import username_already_exists, next_id, id_exist # --> Others
from crud.users import insert_user_db # --> Create 
from crud.users import get_user_by_username_db, get_users_db # --> Read
from crud.users import update_user_db # --> Update
from crud.users import delete_user_db, delete_many_users_db # --> Delete

from utils.security import get_hashed_password

def create_user(db: Collection, user: UserCreate) -> UserOutput:
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
    users = get_users_db(collection=db)
    users_2 = [UserDict(**i) for i in users]
    users_3 = [UsersToList(user=i).to_dict() for i in users]
    
    return users_3


def read_user_by_username(db: Collection, username: str) -> UserOutput:
    user = get_user_by_username_db(collection=db, username=username)
    if not user:
        raise ValueError("Id not exist")
    return user


def update_user(id: int, db: Collection, user: UserCreate):
    pass