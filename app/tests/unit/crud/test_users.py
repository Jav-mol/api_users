import mongomock
from pymongo.collection import Collection

#from pymongo import MongoClient
#from crud.users import insert_user_db

client = mongomock.MongoClient()
db = client["test_db"]
collection = db["test_users"]

#user = collection.insert_many([
#                                {"_id":1,"name":"Nico", "Age":22},
#                                {"_id":2,"name":"Cami", "Age":22},
#                                {"_id":3,"name":"Azul", "Age":22}
#                            ])


user = {"_id":"","name":"Javi", "Age":22}

def next_id(collection: Collection):
    max_id = collection.find().sort("_id", -1).limit(1)
    try:
        return max_id[0]["_id"] + 1
    except:
        return 1

def insert_user_db(db: Collection, user: dict):
    id = next_id(collection)
    user.update({"_id":id})
    user_inserted = db.insert_one(user)
    return user_inserted.inserted_id


insert_user_db(collection, user)

for user in collection.find():
    print(user)


    