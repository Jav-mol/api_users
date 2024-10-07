from pymongo.collection import Collection
from schemas.users import UserCreate

def insert_user_db(db: Collection, user: UserCreate):
    user_inserted = db.insert_one(user)
    return user_inserted.inserted_id