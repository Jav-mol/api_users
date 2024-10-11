from pymongo import MongoClient
from core.config import Setting
import mongomock

setting = Setting()
url = setting.url_db_mongo

def get_db_mongo():
    try:
        client = MongoClient(url)
        db = client["practice"]
        return db["users"]
    except Exception as e:
        raise e


def get_db_mongo_override():
    try:
        client = mongomock.MongoClient()
        db = client["test_users"]
        return db["users"]
    except Exception as e:
        raise e

#collection = db.create_collection("users")
#collection.insert_one({"nombre":"Javi", "edad":22})
