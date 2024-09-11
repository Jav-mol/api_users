from sqlalchemy import create_engine, inspect
from core.config import Setting

setting = Setting()

url = setting.url_db_psql.unicode_string()
engine = create_engine(url)

def get_db_psql():
    connection = engine.connect()
    try:
        yield connection
    except:
        raise "error"
    finally:
        connection.close()

if __name__== "__main__":

    try:

        engine = create_engine(setting.url_db_psql)

        inspector = inspect(engine)

        tables = inspector.get_table_names()

        print(tables)

    except Exception as e:
        print(e)