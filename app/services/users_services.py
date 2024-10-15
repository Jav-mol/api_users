from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput, UsersToList

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


def read_users(db: Collection) -> list[UsersToList]:
    users_db = get_users_db(collection=db)
    
    users_format = []
    for user in users_db:
        user["id"] = user.pop("_id")
        users_format.append(user)
    
    users_list = [UsersToList(**user).to_dict() for user in users_format]
    return users_list


def read_user_by_username(db: Collection, username: str) -> UsersToList:
    user = get_user_by_username_db(collection=db, username=username)
    if not user:
        raise ValueError("Id not exist")
    user["id"] = user.pop("_id")
    return UsersToList(**user)


def update_user(id: int, db: Collection, user: UserCreate):
    pass