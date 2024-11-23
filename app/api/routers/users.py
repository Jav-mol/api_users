from fastapi import APIRouter, Depends
from typing import Annotated
from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput
from services.users_services import insert_user_db
from db.mongodb.get_db import get_db_mongo_override, get_db_mongo
from db.psql.get_db import get_db_psql

router = APIRouter(
    prefix="/users"
)

@router.post("")
async def create_user(user: UserCreate, db: Annotated[Collection, Depends(get_db_mongo)]):
    return user