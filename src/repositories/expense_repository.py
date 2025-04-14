from repositories.user_repository import user_repository
from config import EXPENSES_PATH
import pandas as pd


class ExpenseRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def all_expenses(self):
        try:
            df = pd.read_csv(self._file_path)
        except Exception as e:
            data = {"Date": [], "Description": [], "Amount": [], "User": []}

            df = pd.DataFrame(data)

        return df

    def expenses_by_user(self, user):
        expenses = self.all_expenses()
        username = user.username
        user_expenses = expenses.query(f"User == '{username}'")

        return user_expenses

    def add_expense(self, date, description, amount, user):
        username = user.username

        new_expense = pd.DataFrame(
            {
                "Date": [date],
                "Description": [description],
                "Amount": [amount],
                "User": [username],
            }
        )

        expenses = self.all_expenses()
        new_expenses = pd.concat([new_expense, expenses], ignore_index=True)
        self.write(new_expenses)

        return new_expenses

    def write(self, expenses):
        expenses.to_csv(self._file_path, index=False)


expense_repository = ExpenseRepository(EXPENSES_PATH)
