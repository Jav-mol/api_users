from pydantic import BaseModel
from datetime import datetime

class Book(BaseModel):
    id: int = None
    title: str
    author: str


class BookDate(Book):
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
