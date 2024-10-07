from schemas.users import UserDB
from pymongo.collection import Collection
from schemas.users import UserCreate


def next_id(collection: Collection) -> int:
    max_id = collection.find().sort("_id", -1).limit(1)
    try:
        return max_id[0]["_id"] + 1
    except:
        print("error")
        return 1


def user_already_exists(collection: Collection, username: str) -> bool:
    user = collection.find({"username":username})
    try:
        user[0]
        return True
    except:
        return False


def insert_user_db(collection: Collection, user: UserDB) -> int:
    user_dict = user.model_dump()
    
    user_dict["_id"] = user_dict.pop("id")
    
    user_inserted = collection.insert_one(user_dict)
    return user_inserted.inserted_id


def user_by_id(collection: Collection, id: int) -> dict:
    user = collection.find_one({"_id":id})
    return user
