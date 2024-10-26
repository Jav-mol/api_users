from sqlalchemy import create_engine, inspect
from core.config import Setting
import sqlite3

setting = Setting()

url = setting.url_db_psql
engine = create_engine(url)

def get_db_psql():
    connection = engine.connect()
    try:
        yield connection
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise f"Error: {e}"
    finally:
        connection.close()


from contextlib import contextmanager
from db.psql.models.books import metadata
url_test = "sqlite:///:memory:"

@contextmanager
def get_db__psql_override():
    engine = create_engine(url_test)
    connection = engine.connect()    
    try:
        metadata.create_all(engine)
        yield connection
        connection.commit()
    except Exception as e:
        raise f"Error: {e}"
    finally:
        connection.close()

    