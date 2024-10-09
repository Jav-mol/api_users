from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput

from crud.users import username_already_exists, next_id, id_exist # --> Others
from crud.users import insert_user_db # --> Create 
from crud.users import get_user_by_id, get_users # --> Read
from crud.users import update_user # --> Update
from crud.users import delete_user, delete_many_users # --> Delete


def create_user_db(db: Collection, user: UserCreate):
    if username_already_exists(collection=db, username=user.username):
        raise ValueError("User already exist")
    
    user_db = UserDB(**user.model_dump())
    user_db.id = next_id(collection=db)
    
    _id = insert_user_db(collection=db, user=user_db.model_dump())
    user_inserted = db.find_one({"_id":_id})
    user_inserted["id"] = user_inserted.pop("_id")
    
    return UserOutput(**user_inserted)

