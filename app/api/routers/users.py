from fastapi import APIRouter, Depends
from typing import Annotated
from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput
from db.mongodb.get_db import get_db_mongo_override, get_db_mongo
from db.psql.get_db import get_db_psql
from services.users_services import create_user

router = APIRouter(
    prefix="/users"
)
import asyncio

@router.post("")
async def router_create_user(user: UserCreate, db: Annotated[Collection, Depends(get_db_mongo)]):
    
    user_created = create_user(user=user, db=db)
    
    return user_created
