import pytest
from unittest.mock import MagicMock, patch
from sqlalchemy import Connection
from db.psql.get_db import get_db_psql, get_db__psql_override

def test_get_db_psql_success():
    mock_connection = MagicMock()
    with patch("db.psql.get_db.engine.connect", return_value=mock_connection) as mock:
        gen = get_db_psql()
        connection = next(gen)
        mock.assert_called_once()
        assert connection == mock_connection
        next(gen, None)
        mock_connection.commit.assert_called_once()
        mock_connection.close.assert_called_once()


def test_get_db_psql_exception():
    mock_connection = MagicMock()
    with patch("db.psql.get_db.engine.connect", return_value=mock_connection) as mock:
        gen = get_db_psql()
        next(gen)
        with pytest.raises(Exception):
            gen.throw(Exception)
        mock_connection.rollback.assert_called_once()

from db.psql.models.books import books

def test_get_db_psql_override_success():
    db = get_db__psql_override()        

    with db as connection:
        assert isinstance(connection, Connection) == True
    

