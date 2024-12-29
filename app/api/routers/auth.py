from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pymongo.collection import Collection
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from utils.security import verify_hashed_password, get_access_token

from db.mongodb.get_db import get_db_mongo

from services.users_services import read_user_by_username

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


router = APIRouter()
#oauth2 = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/login")
async def login_access(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Collection, Depends(get_db_mongo)]) -> Token:
    user_db = read_user_by_username(db=db, username=form_data.username)
    
    if not verify_hashed_password(user_db.password, form_data.password):
        raise HTTPException(401, "Password incorrect")
    
    access_token = get_access_token({"sub":form_data.username, "role":user_db.rol, "id":user_db.id})
    
    return Token(access_token=access_token)