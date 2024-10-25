from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

metadata = MetaData()

books = Table('books', metadata,
              Column('Id', Integer, primary_key=True),
              Column('Title', String, unique=True),
              Column('Author', String, unique=True),
              Column("Created_at", DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

user_book = Table("user_book", metadata,
              Column('book_id', Integer, ForeignKey("books.Id")),
              Column('user_id', Integer)
                  )
