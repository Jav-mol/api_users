from pymongo.collection import Collection
from schemas.books import Book

from crud.books import check_book_exists, read_books_db
from crud.books import insert_book_db

def create_book(db: Collection, book: Book) -> Book:
    print(check_book_exists(db=db, book=book))
    #    book_id = insert_book_db(db=db, book=book)
    #    return book_id
    
    #return "Book already exists"