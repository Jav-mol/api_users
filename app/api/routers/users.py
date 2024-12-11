from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from pymongo.collection import Collection
from schemas.users import UserCreate, UserDB, UserOutput, UsersToDict
from db.mongodb.get_db import get_db_mongo_override, get_db_mongo
from services.users_services import service_create_user, service_read_users, service_dalete_user
from fastapi.security import OAuth2PasswordBearer
from utils.security import decode_token
from api.routers.auth import Token

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter(
    prefix="/users"
)

def get_current_user(token: Annotated[Token, Depends(oauth2)]) -> dict:
    token_dict = token.model_dump()
    data = token_dict.get("access_token") 
    user = decode_token(data)
    return user 


@router.post("", status_code=201,response_model=UserOutput)
async def create_user(user: UserCreate, db: Annotated[Collection, Depends(get_db_mongo)]):
    user_created = service_create_user(user=user, db=db)
    return user_created


@router.get("", status_code=200, response_model=list)
async def get_users(db: Annotated[Collection, Depends(get_db_mongo)], user: Annotated[dict, Depends(get_current_user)]):

    if not user.get("role") in ["user","admin"]:
        raise HTTPException(403, "Not authorized")

    users = service_read_users(db=db)
    return users

@router.delete("/{id}")
async def delete_user(id: int, db: Annotated[Collection, Depends(get_db_mongo)], user: Annotated[dict, Depends(get_current_user)]):
    user_deleted = service_dalete_user(id=id, db=db)
    print(user_deleted)