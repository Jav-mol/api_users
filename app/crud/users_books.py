from sqlalchemy import Connection, select
from schemas.users_books import UserBook
from db.psql.models.books import users_books, books

def insert_user_book_db(db: Connection, user_book: UserBook):                
    user_book_db = db.execute(users_books.insert().values(book_id = user_book.book_id, user_id= user_book.user_id))
    return user_book_db.rowcount

def read_users_books_by_user_id(db: Connection, user_id: int):
    users_books_db = db.execute(select(users_books, books.c.title).join(books, users_books.c.book_id == books.c.id).where(users_books.c.user_id == user_id)).mappings()
    
    return [user_book for user_book in users_books_db]
