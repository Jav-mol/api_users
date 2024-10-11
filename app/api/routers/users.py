from fastapi import APIRouter, Depends
from typing import Annotated
from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput
from services.users_services import create_user_db
from db.mongodb.get_db import get_db_mongo

router = APIRouter()

@router.post("/user", response_model=UserOutput)
async def create_user(user: UserCreate, db: Annotated[Collection, Depends(get_db_mongo)]):
    pass