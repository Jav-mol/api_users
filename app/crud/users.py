from pymongo.collection import Collection

def insert_user_db(db: Collection, user: dict):
    user_inserted = db.insert_one(user)
    return user_inserted.inserted_id