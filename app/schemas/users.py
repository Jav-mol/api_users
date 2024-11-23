from pydantic import BaseModel, EmailStr, Field
from typing import Literal
from datetime import datetime

class UserCreate(BaseModel): 
    username: str
    password: str
    email: str

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


class UserOutput(BaseModel):
    id: int
    username:str

class UserUpdate(BaseModel):
    username: str = None
    password: str = None
    email: EmailStr = None


class UsersToList(UserDB):
    password: str = Field(default=None, exclude=True)
    
    def to_dict(self):
        return {
            self.username: {
                "id": self.id,
                "username":self.username,            
                "email": self.email,
                "is_active":self.is_active,
                "rol":self.rol,
                "created_at":self.created_at
            }
        }
"""

Javier: {
    id: 1,
    username: Javier
    is_active: True
    rol:user
    }
"""