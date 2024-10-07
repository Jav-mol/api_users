from pydantic import BaseModel

class UserBook(BaseModel):
    user_id: int
    book_id: int