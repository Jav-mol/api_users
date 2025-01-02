from sqlalchemy import Connection
from schemas.books import Book
from db.psql.models.books import books


def check_book_exists(db: Connection, book: Book) -> bool:
    book_db = db.execute(books.select().where(books.c.title == book.title, books.c.author == book.author))
    return bool(book_db.all())


def insert_book_db(db: Connection, book: Book) -> int:
    book_inserted = db.execute(books.insert().values(title=book.title, author=book.author))
    return book_inserted.inserted_primary_key[0]


def read_books_db(db: Connection) -> list[tuple]:
    books_db = db.execute(books.select())
    return [book for book in books_db] 


def read_book_db_by_id(db: Connection, id: int) -> list[tuple]:
    book = db.execute(books.select().where(books.c.id == id)).mappings().all()
    return book 


def delete_book_db(db: Connection, id_book: int) -> int:
    book_deleted = db.execute(books.delete().where(books.c.id == id_book))
    return book_deleted.rowcount


def update_book_db(db: Connection, id_book: int, book_new: dict):
    db.execute(books.update().values(title=book_new["title"], author=book_new["author"]).where(books.c.id ==id_book))
    book_updated = read_book_db_by_id(db=db, id=id_book)
    return book_updated