from pymongo.collection import Collection 
from schemas.users import UserCreate, UserBD
from crud.users import insert_user_db

def insert_user(db: Collection, user: UserCreate):
    user_db = UserBD(**user.model_dump())
    user_id = insert_user_db(db=db, user=user_db.model_dump())
    return db.find_one({"_id":user_id})