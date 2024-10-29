from sqlalchemy import Connection
from schemas.books import Book
from db.psql.models.books import books

def check_book_exists(db: Connection, book: Book) -> dict:
    book_db = db.execute(books.select().where(books.c.title == book.title, books.c.author == book.author))
    return bool(book_db.all())
    
def insert_book_db(db: Connection, book: Book):
    book_inserted = db.execute(books.insert().values(title=book.title, author=book.author))
    return book_inserted.inserted_primary_key

def read_books_db(db: Connection):
    books_db = db.execute(books.select())
    return [book for book in books_db] 
