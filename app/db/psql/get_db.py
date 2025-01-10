from sqlalchemy import create_engine, inspect
from core.config import Setting
from db.psql.models.books import metadata
import sqlite3

setting = Setting()

url = setting.url_db_psql
engine = create_engine(url)

def get_db_psql():
    connection = engine.connect()
    #metadata.create_all(engine)
    try:
        yield connection
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()


from contextlib import contextmanager
url_test = "sqlite:///:memory:"


@contextmanager
def get_db__psql_override():
    engine = create_engine(url_test, connect_args={"check_same_thread": False})
    connection = engine.connect()    
    try:
        metadata.create_all(engine)
        yield connection
        connection.commit()
    except Exception as e:
        raise e
    finally:
        connection.close()

