from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

metadata = MetaData()

books = Table('books', metadata,
              Column('id', Integer, primary_key=True),
              Column('title', String, unique=True),
              Column('author', String, unique=True),
              Column("created_at", DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

user_book = Table("user_book", metadata,
              Column('book_id', Integer, ForeignKey("books.Id")),
              Column('user_id', Integer)
                  )
