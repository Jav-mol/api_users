from pymongo.collection import Collection

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


# --- CREATE ---
def insert_user_db(collection: Collection, user: dict) -> int:    
    user_inserted = collection.insert_one(user)
    return user_inserted.inserted_id

# --- READ ---
def get_user_by_id(collection: Collection, id: int) -> dict:
    user = collection.find_one({"_id":id})
    return user


def get_users(collection: Collection) -> list[dict]:
    return  [user for user in collection.find()]

# --- UPDATE ---
def update_user(collection: Collection, user: dict, id: int):
    collection.update_one({"_id":id}, {"$set": {"username":user["username"], "password":user["password"], "email":user["email"]}})
    return collection.find_one({"_id":id})

# --- DELETE ---
def delete_user(collection: Collection, id: int) -> int:
    result = collection.delete_one({"_id":id})
    return result.deleted_count