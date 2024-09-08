from sqlalchemy import create_engine, inspect

# p!hp!7@6cLfM@6p
# JK8PYhdlXIQDXUpn
# JK8PYhdlXIQDXUpn


url = "postgresql://postgres.ibgccyemgogohyiitbix:JK8PYhdlXIQDXUpn@aws-0-sa-east-1.pooler.supabase.com:6543/postgres"
try:

    engine = create_engine(url)

    inspector = inspect(engine)

    tables = inspector.get_table_names()

    print(tables)

except Exception as e:
    print(e)