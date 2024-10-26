from pydantic import BaseModel

class Book(BaseModel):
    id: int = None
    title: str
    author: str