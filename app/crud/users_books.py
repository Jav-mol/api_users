from sqlalchemy import Connection, select
from schemas.users_books import UserBook
from db.psql.models.books import users_books, books


def insert_user_book_db(db: Connection, user_book: UserBook) -> int:                
    user_book_db = db.execute(users_books.insert().values(book_id = user_book.book_id, user_id= user_book.user_id))

    return user_book_db.rowcount


def read_users_books_by_user_id(db: Connection, user_id: int) -> list:
    users_books_db = db.execute(select(users_books, books.c.title).join(books, users_books.c.book_id == books.c.id).where(users_books.c.user_id == user_id)).mappings()

    return [user_book for user_book in users_books_db]


def check_user_book_exist(db: Connection, user_id: int, book_id: int) -> bool:
    user_book_exist = db.execute(users_books.select().where(users_books.c.user_id == user_id, users_books.c.book_id == book_id)).fetchall()
    
    return bool(user_book_exist)


def delete_user_book(db: Connection, user_id: int) -> int:
    user_book_deleted = db.execute(users_books.delete().where(users_books.c.user_id == user_id))
    
    return user_book_deleted.rowcount