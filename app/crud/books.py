from sqlalchemy import Connection
from schemas.books import Book
from db.psql.models.books import books

def check_book_exists(db: Connection, book: Book):
    book_db = db.execute(books.select().where(books.c.title == book.title, books.c.author == book.author))
    print(book_db)
    
def insert_book_db(db: Connection, book: Book):
    db.execute(books.insert().values(title=book.title, author=book.author))
    db.commit()
