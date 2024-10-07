from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    autor: str