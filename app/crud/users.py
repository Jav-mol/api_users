from pymongo.collection import Collection
from schemas.users import UserCreate


def next_id(collection: Collection):
    max_id = collection.find().sort("_id", -1).limit(1)
    try:
        return max_id[0]["_id"] + 1
    except:
        print("error")
        return 1


def user_already_exists(db: Collection, username: str):
    user = db.find({"username":username})
    try:
        user[0]
        return True
    except:
        return False


def insert_user_db(db: Collection, user: dict):
    user_inserted = db.insert_one(user)
    return user_inserted.inserted_id

