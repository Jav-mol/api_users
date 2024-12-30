from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from api.routers.auth import Token
from schemas.users import UserCreate, UserDB, UserOutput, UsersToDict

from db.mongodb.get_db import get_db_mongo
from db.psql.get_db import get_db_psql

from services.users_services import service_create_user, service_read_users, service_dalete_user, service_update_user_role
from services.users_books_services import read_user_book_by_id

from crud.users_books import delete_user_book

from sqlalchemy import Connection
from pymongo.collection import Collection
from typing import Annotated, Literal
from utils.security import decode_token

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

    users = service_read_users(db=db)
    return users


@router.get("/{id}", status_code=200, response_model=UsersToDict)
async def get_user_data(id: int, db_psql: Annotated[Connection,Depends(get_db_psql)], db_mongo: Annotated[Collection, Depends(get_db_mongo)], user: Annotated[dict, Depends(get_current_user)]):
        if not user.get("role") == "admin":
            raise HTTPException(403, "Not authorized")

        user_by_id = read_user_book_by_id(db_mongo=db_mongo, db_psql=db_psql, id_user=id)
        
        return user_by_id


@router.delete("/{id}", response_model=dict[str,UserOutput])
async def delete_user(id: int, db_psql: Annotated[Connection, Depends(get_db_psql)],db_mongo: Annotated[Collection, Depends(get_db_mongo)], user: Annotated[dict, Depends(get_current_user)]):
    
    if not user.get("role") == "admin":
        raise HTTPException(403, "Not authorized")

    id_user_deleted = service_dalete_user(id=id, db=db_mongo)
    user_book = delete_user_book(db=db_psql, user_id=id)

    return {"User deleted":id_user_deleted}


@router.put("/{id}")
async def update_role(id: int, role: Literal["admin", "user"], db: Annotated[Collection, Depends(get_db_mongo)], user: Annotated[dict, Depends(get_current_user)]):
    user = service_update_user_role(id=id, role=role, db=db)
    return user
