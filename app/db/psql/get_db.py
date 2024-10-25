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

from db.psql.models.books import metadata
url_test = "sqlite:///:memory:"

def get_db__psql_override():
    engine2 = create_engine(url_test)
    connection = engine2.connect()    
    inspector = inspect(engine2)
    metadata.create_all(engine2)
    print(inspector.get_table_names())
    print("Hola")
    try:
        yield inspector
        connection.commit()
    except Exception as e:
        raise f"Error: {e}"
    finally:
        connection.close()

    