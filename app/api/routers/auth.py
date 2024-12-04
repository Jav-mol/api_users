from typing import Annotated
from fastapi import APIRouter, Depends
from pymongo.collection import Collection
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from db.mongodb.get_db import get_db_mongo

from services.users_services import read_user_by_username

class Token:
    access_token: str
    token_type: str = "bearer"


router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/login")
async def login_access(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Collection, Depends(get_db_mongo)]):
    user_db = read_user_by_username(db=db, username=form_data.username)
    
    print(form_data)
    print(user_db)