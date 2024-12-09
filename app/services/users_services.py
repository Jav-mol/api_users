from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput, UsersToDict, UserUpdate
from fastapi import HTTPException

from crud.users import username_already_exists, next_id, id_exist # --> Others
from crud.users import insert_user_db # --> Create 
from crud.users import get_user_by_username_db, get_user_by_id_db, get_users_db # --> Read
from crud.users import update_user_db # --> Update
from crud.users import delete_user_db, delete_many_users_db # --> Delete

from utils.security import get_hashed_password

def service_create_user(db: Collection, user: UserCreate) -> UserOutput:
    
    if username_already_exists(collection=db, username=user.username):
        raise HTTPException(401 ,"User already exist")

    user.password = get_hashed_password(user.password) 

    user_db = UserDB(**user.model_dump())
    user_db.id = next_id(collection=db)

    id = insert_user_db(collection=db, user=user_db.model_dump())

    user_inserted = db.find_one({"_id":id})
    user_inserted["id"] = user_inserted.pop("_id")

    return UserOutput(**user_inserted)


def service_read_users(db: Collection) -> list[UsersToDict]:
    users_db = get_users_db(collection=db)

    users_format = []
    for user in users_db:
        user["id"] = user.pop("_id")
        users_format.append(user)

    users_list = [UsersToDict(**user).to_dict() for user in users_format]
    return users_list


def read_user_by_username(db: Collection, username: str) -> UsersToDict:
    user = get_user_by_username_db(collection=db, username=username)
    if not user:
        raise HTTPException(401,"Username not exist")
    user["id"] = user.pop("_id")
    return UsersToDict(**user)


def update_user(id: int, db: Collection, user: UserUpdate):
    if not id_exist(collection=db, id=id):
        raise ValueError("Id not exist")
    
    user_old = get_user_by_id_db(collection=db, id=id)
    if not user.username:
        user.username = user_old["username"]
    if not user.email:
        user.email = user_old["email"]
    if not user.password:
        user.password = user_old["username"]
    else:
        user.password = get_hashed_password(user.password)
        
    user_new = update_user_db(collection=db, user=user.model_dump(), id=id)
    
    return UserUpdate(**user_new)


def dalete_user(id: int, db: Collection) -> int:
    if not id_exist(collection=db, id=id):
        raise ValueError("Id not exist")
    
    user_deleted = delete_user_db(collection=db, id=id)
    return user_deleted


def delete_many_users(ids: list[int], db: Collection):
    for id in ids:
        if not id_exist(collection=db, id=id):
            raise ValueError("Id not exist")
        
    count_users_deleted = delete_many_users_db(collection=db, ids=ids)
    return count_users_deleted
