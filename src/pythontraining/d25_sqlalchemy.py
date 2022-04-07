"""
Demo of SQLAlchemy and Pandas
"""

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///crm.db")
# engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")

# print(engine.table_names())

with engine.connect() as connection:
    result = connection.execute("""SELECT * FROM clients LIMIT 5""")
    for row in result:
        print(row)

# Read entire table
clients = pd.read_sql("clients", engine)
print(clients.head())

# Use SQL query
budapest = pd.read_sql("""SELECT * FROM clients WHERE city ="Budapest";""", engine)
print(budapest)