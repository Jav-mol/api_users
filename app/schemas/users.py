from pydantic import BaseModel, EmailStr, Field
from typing import Literal
from datetime import datetime

class UserCreate(BaseModel): 
    username: str
    password: str
    email: EmailStr

    #model_config = {
    #    "from_attributes":True
    #}

class UserDB(BaseModel):
    id: int = None
    username: str
    password: str
    email: EmailStr
    is_active: bool = True
    rol: Literal["admin", "user"] = "user" 
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
