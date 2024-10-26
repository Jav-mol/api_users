from db.psql.get_db import get_db__psql_override
from crud.books import check_book_exists

from sqlalchemy import Connection
import pytest

@pytest.fixture
def connection() -> Connection:
    result = get_db__psql_override()
    db = next(result)
    return db

@pytest.fixture
def list_books():
    return []