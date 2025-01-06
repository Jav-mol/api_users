from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.books import Book

from crud.books import check_book_exists, read_books_db, read_book_db_by_id
from crud.books import insert_book_db
from crud.books import delete_book_db
from crud.books import update_book_db

from crud.users_books import delete_user_book, get_books_by_id_user, read_users_books_by_book_id


def create_book(db: Collection, book: Book) -> list:
    if not(check_book_exists(db=db, book=book)):
        book_id = insert_book_db(db=db, book=book)
        book_created = read_book_db_by_id(db=db, id=book_id)
        return book_created

    return "Book already exists"


def read_books(db: Collection) -> list[tuple]:
    return read_books_db(db=db)

from pprint import pprint

def delete_book(db: Collection, id: int):
    book_deleted = read_book_db_by_id(db=db, id=id)
    if not book_deleted: 
        raise ValueError("Id not found")
    delete_book_db(db=db, id_book=id)
    
    book_ids = read_users_books_by_book_id(db=db, book_id=id)
    
    pprint(book_ids)
    
    return book_deleted


def update_book_service(db: Collection, id_user: int, id_book: int, book: Book):
    books = get_books_by_id_user(db=db, user_id=id_user)
    ids_books = [id_book["id"] for id_book in books]
    print(ids_books)
    if not id_book in ids_books:
        raise HTTPException(401, "Book invalid")
    book_updated = update_book_db(db=db, id_book=id_book, book_new=book.model_dump())
    return book_updated