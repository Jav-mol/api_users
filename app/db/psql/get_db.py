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

url_test = ":memory:"
def get_db_override():
    connection = sqlite3.connect(url_test)
    try:
        yield connection
        connection.commit()
    except Exception as e:
        raise f"Error: {e}"
    finally:
        connection.close()

if __name__== "__main__":


    try:
        engine = create_engine(setting.url_db_psql)
        
        print(engine)
            
        inspector = inspect(engine)
        
        tables = inspector.get_table_names()
        
        print(tables)
    except Exception as e:
        print(e)
