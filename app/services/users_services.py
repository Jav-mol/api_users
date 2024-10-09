from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput

from crud.users import next_id, insert_user_db, user_already_exists

def create_user_db(db: Collection, user: UserCreate):
    
    if user_already_exists(collection=db, username=user.username):
        raise ValueError("User already exist")
    
    user_db = UserDB(**user.model_dump())
    
    id = next_id(collection=db)
    user_db.id = id
    
    id_inserted = insert_user_db(collection=db, user=user_db.model_dump())

    user_inserted = db.find_one({"_id":id_inserted})
    user_inserted["id"] = user_inserted.pop("_id")
    
    return UserOutput(**user_inserted)

