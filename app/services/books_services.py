from fastapi import HTTPException
from pymongo.collection import Collection
from schemas.books import Book

from crud.books import check_book_exists, read_books_db, read_book_db_by_id
from crud.books import insert_book_db
from crud.books import delete_book_db
from crud.books import update_book_db

from crud.users_books import delete_user_book, get_books_by_id_user


def create_book(db: Collection, book: Book) -> list:
    if not(check_book_exists(db=db, book=book)):
        book_id = insert_book_db(db=db, book=book)
        book_created = read_book_db_by_id(db=db, id=book_id)
        return book_created

    return "Book already exists"


def read_books(db: Collection) -> list[tuple]:
    return read_books_db(db=db)


def delete_book(db: Collection, id: int):
    book_deleted = read_book_db_by_id(db=db, id=id)
    if not book_deleted: 
        raise ValueError("Id not found")
    delete_book_db(db=db, id_book=id)
    return book_deleted


def update_book_service(db: Collection, id: int, book: Book):
    books = get_books_by_id_user(db=db, user_id=id)
    ids_books = [id_book["id"] for id_book in books]
    if not id in ids_books:
        raise HTTPException(401, "Book invalid")
    book_updated = update_book_db(db=db, id_book=id, book_new=book.model_dump())
    return book_updated