import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

EXPENSES_FILENAME = os.getenv("EXPENSES_FILENAME") or "expenses.csv"
EXPENSES_PATH = os.path.join(dirname, "..", "data", EXPENSES_FILENAME)
