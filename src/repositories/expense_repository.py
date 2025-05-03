import pandas as pd
from config import EXPENSES_PATH


class ExpenseRepository:
    """
    Repository for managing and storing expense records in a CSV file.
    """

    def __init__(self, file_path):
        """
        Class constructor.

        Args:
            file_path: Path to the CSV file, that the expenses are stored in.
        """
        self._file_path = file_path

    def all_expenses(self):
        """
        Fetches all expenses from the CSV file and sorts them by date in descending order

        Returns:
            A pandas DataFrame containing all expense records, sorted by date in descending order.
        """

        try:
            df = pd.read_csv(self._file_path)
            df = df.sort_values(by="Date", ascending=False)
        except Exception:
            data = {"Date": [], "Description": [], "Amount": [], "User": []}

            df = pd.DataFrame(data)

        return df

    def expenses_by_user(self, user):
        """
        Fetches expenses for a specified user.

        Args:
            user: An instance of class User.

        Returns:
            A pandas DataFrane containing expense records for the given user.
        """

        expenses = self.all_expenses()
        username = user.username
        user_expenses = expenses.query(f"User == '{username}'")

        return user_expenses

    def expenses_by_user_filtered_by_date(self, user, from_date, to_date):
        from_date = pd.to_datetime(from_date)
        to_date = pd.to_datetime(to_date)

        expenses = self.expenses_by_user(user)

        expenses["Date"] = pd.to_datetime(expenses["Date"], errors="coerce")
        expenses.set_index("Date", inplace=True)

        mask = (expenses.index >= from_date) & (expenses.index <= to_date)
        filtered_expenses = expenses[mask]

        filtered_expenses = filtered_expenses.reset_index()
        filtered_expenses["Date"] = filtered_expenses["Date"].dt.strftime(r"%Y-%m-%d")

        sum = filtered_expenses.Amount.sum()

        return (filtered_expenses, sum)

    def expense_sum(self, user):
        """
        Calculates the sum of expenses for a specified user.

        Returns:
            Sum of expenses for the given user.
        """

        expenses = self.expenses_by_user(user)

        return expenses.Amount.sum()

    def add_expense(self, date, description, amount, user):
        """
        Adds a new expense to the CSV file.

        Args:
            date: Date of the expense.
            description: Description (category) of the expense.
            amount: Amount spent.
            user: An instance of class User.

        Returns:
            A pandas DataFrame containing expense records including the newly added expense.
        """

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
        """
        Writes the given DataFrame to the CSV file.

        Args:
            expenses: The pandas DataFrame to write.
        """

        expenses.to_csv(self._file_path, index=False)

    def delete_one_expense(self, date, category, amount, user):
        """
        Deletes a specified expense from the CSV file that mathes the given arguments.

        Args:
            date: Date of the expense.
            description: Description (category) of the expense.
            amount: Amount spent.
            user: Username associated with the expense.
        """

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
        """
        Overwrites the CSV file with an empty pandas DataFrame.
        """

        df = pd.DataFrame({"Date": [], "Description": [], "Amount": [], "User": []})

        self.write(df)


expense_repository = ExpenseRepository(EXPENSES_PATH)
