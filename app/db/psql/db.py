from sqlalchemy import create_engine, inspect
from core.config import Setting

setting = Setting()

url_psql = setting.url_db_psql

try:

    engine = create_engine(setting.url_db_psql)

    inspector = inspect(engine)

    tables = inspector.get_table_names()

    print(tables)

except Exception as e:
    print(e)