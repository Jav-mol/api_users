from sqlalchemy import create_engine, inspect

url = "javi"

variable = "Var"

try:

    engine = create_engine(url)

    inspector = inspect(engine)

    tables = inspector.get_table_names()

    print(tables)

except Exception as e:
    print(e)