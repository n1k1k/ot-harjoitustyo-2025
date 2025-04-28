import pandas as pd
from config import EXPENSES_PATH


class ExpenseRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def all_expenses(self):
        try:
            df = pd.read_csv(self._file_path)
            df = df.sort_values(by="Date", ascending=False)
        except:
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

    def delete_one_expense(self, date, category, amount, user):
        df = self.all_expenses()

        i = df[
            (
                (df.Date == date)
                & (df.Description == category)
                & (df.Amount == float(amount))
                & (df.User == user)
            )
        ].index

        new_df = df.drop(i[0])
        self.write(new_df)

    def delete_all_expenses(self):
        df = pd.DataFrame({"Date": [], "Description": [], "Amount": [], "User": []})

        self.write(df)


expense_repository = ExpenseRepository(EXPENSES_PATH)
