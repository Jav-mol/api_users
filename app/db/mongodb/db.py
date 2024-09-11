from pymongo import MongoClient
from core.config import setting

url = setting.url_db_mongo

client = MongoClient(url)

#def get_db_mongo():
db = client["practice"]
#collection = db.create_collection("users")
#collection.insert_one({"nombre":"Javi", "edad":22})

print(db.list_collection_names())

client.close()