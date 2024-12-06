from fastapi import APIRouter, Depends
from typing import Annotated
from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput
from db.mongodb.get_db import get_db_mongo_override, get_db_mongo
from db.psql.get_db import get_db_psql
from services.users_services import service_create_user, service_read_users
from fastapi.security import OAuth2PasswordBearer


oauth2 = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter(
    prefix="/users"
)

@router.post("")
async def create_user(user: UserCreate, db: Annotated[Collection, Depends(get_db_mongo)]):
    user_created = service_create_user(user=user, db=db)
    return user_created


@router.get("")
async def get_users(db: Annotated[Collection, Depends(get_db_mongo)], token: Annotated[str, Depends(oauth2)]):
    users = service_read_users(db=db)
    return users