from pymongo.collection import Collection 
from schemas.users import User
from crud.users import insert_user_db

def insert_user(db: Collection, user: User):
    user_dict = user.model_dump()
    user_id = insert_user_db(db=db, user=user_dict)
    return db.find_one({"_id":user_id})