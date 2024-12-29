from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from api.routers.auth import Token
from schemas.users import UserCreate, UserDB, UserOutput, UsersToDict, UserUpdate

from db.mongodb.get_db import get_db_mongo
from db.psql.get_db import get_db_psql

from services.users_services import service_create_user, service_dalete_user, read_user_by_username, service_update_user
from services.users_books_services import read_user_book_by_id

from crud.users_books import delete_user_book

from sqlalchemy import Connection
from pymongo.collection import Collection
from typing import Annotated, Literal
from utils.security import decode_token

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter(
    prefix="/user"
)

def get_current_user(token: Annotated[Token, Depends(oauth2)]) -> dict:
    token_dict = token.model_dump()
    data = token_dict.get("access_token") 
    user = decode_token(data)
    return user 


@router.get("", status_code=200)
async def get_user(db: Annotated[Collection, Depends(get_db_mongo)], user: Annotated[dict, Depends(get_current_user)]):
    current_user = read_user_by_username(db=db, username=user.get("sub"))
    return current_user

@router.put("", response_model=UsersToDict)
async def update_user(user_update: UserCreate, db: Annotated[Collection, Depends(get_db_mongo)], user: Annotated[dict, Depends(get_current_user)]):    
    
    user_updated = service_update_user(id=user["id"], db=db, user=UserUpdate(**user_update.model_dump()))
    
    user_in_db = read_user_by_username(db=db, username=user_updated.username)
    
    return user_in_db