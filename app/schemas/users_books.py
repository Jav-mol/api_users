from pydantic import BaseModel
from datetime import datetime

from schemas.books import Book

class UserBook(BaseModel):
    user_id: int
    book_id: int



class User(BaseModel):
    id: int
    username: str
    rol: str
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    books: list[Book]
