import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "..", "data", "database.sqlite"))

# onnection = sqlite3.connect("test.sqlite")
connection.row_factory = sqlite3.Row

print(connection)


def get_database_connection():
    return connection
