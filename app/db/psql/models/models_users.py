from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, DateTime, ForeignKey

metadata = MetaData()

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True)
)
