from pydantic import BaseModel, EmailStr
from typing import Literal

class User(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    is_active: bool = True
    rol: Literal["admin", "user"] = "user" 