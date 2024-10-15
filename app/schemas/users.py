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


class UserOutput(BaseModel):
    id: int
    username:str


class UserCurrent(UserOutput):
    created_at: str
        
class UserUpdate(BaseModel):
    pass

class UserDict(UserDB):
    password: str = Field(default=None, exclude=True)
    #id: int
    #username: str

class UsersToList(BaseModel):
    user: UserDict
    
    def to_dict(self):
        return {
            self.user.username: {
                "id": self.user.id,
                "username":self.user.username,            
                "email": self.user.email,
                "is_active":self.user.is_active,
                "rol":self.user.rol,
                "created_at":self.user.created_at
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