from pymongo.collection import Collection

def next_id(collection: Collection) -> int:
    max_id = collection.find().sort("_id", -1).limit(1)
    try:
        return max_id[0]["_id"] + 1
    except:
        return 1

def id_exist(collection: Collection, id: int):
    user = collection.find({"_id":id})
    try:
        user[0]
        return True
    except: None

def username_already_exists(collection: Collection, username: str) -> bool:
    user = collection.find({"username":username})
    try:
        user[0]
        return True
    except: None

# --- CREATE ---
def insert_user_db(collection: Collection, user: dict) -> int:    
    user["_id"] = user.pop("id")
    user_inserted = collection.insert_one(user)
    return user_inserted.inserted_id

# --- READ ---
def get_user_by_username_db(collection: Collection, username: str) -> dict:
    user = collection.find_one({"username":username})
    try: 
        user["id"] = user.pop("_id")
        return user
    except: None

def get_user_by_id_db(collection: Collection, id: int) -> dict:
    user = collection.find_one({"_id":id})
    try: 
        user["id"] = user.pop("_id")
        return user
    except: None

def get_users_db(collection: Collection) -> list[dict]:
    users_db = collection.find()
    return  users_db

# --- UPDATE ---
def update_user_db(collection: Collection, user: dict, id: int) -> dict:
    collection.update_one({"_id":id}, {"$set": {"username":user["username"], "password":user["password"], "email":user["email"]}})
    return collection.find_one({"_id":id})

# --- DELETE ---
def delete_user_db(collection: Collection, id: int) -> int:
    result = collection.delete_one({"_id":id})
    return result.deleted_count

def delete_many_users_db(collection: Collection, ids: list[int]) -> int:
    result = collection.delete_many({"_id":{"$in":ids}})
    return result.deleted_count
