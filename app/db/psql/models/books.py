from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

metadata = MetaData()

books = Table('books', metadata,
              Column("id", Integer, primary_key=True),
              Column("title", String, unique=True),
              Column("author", String, unique=True),
              Column("created_at", String, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


users_books = Table("users_books", metadata,
              Column("user_id", Integer),
              Column("book_id", Integer, ForeignKey("books.id"))
                )
