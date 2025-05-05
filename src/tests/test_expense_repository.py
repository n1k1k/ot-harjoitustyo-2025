import unittest
from repositories.expense_repository import expense_repository
from repositories.user_repository import user_repository
from entities.user import User


class TestExpenseRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        expense_repository.delete_all_expenses()
        self.test_user1 = User("SpongeBob", "sb123")

    def test_add_expense(self):
        expense_repository.add_expense(
            date="25/06/2003",
            description="Groceries",
            amount="25",
            user=self.test_user1,
        )

        expenses = expense_repository.all_expenses()

        self.assertEqual(expenses.shape[0], 1)
        self.assertEqual(expenses.iloc[0]["Date"], "25/06/2003")
        self.assertEqual(expenses.iloc[0]["Description"], "Groceries")
        self.assertEqual(expenses.iloc[0]["Amount"], 25)
        self.assertEqual(expenses.iloc[0]["User"], self.test_user1.username)

    def test_expenses_by_user_filtered_by_date(self):
        expense_repository.add_expense(
            date="27/05/2025",
            description="Transportation",
            amount="2.9",
            user=self.test_user1,
        )

        expense_repository.add_expense(
            date="25/05/2025",
            description="Groceries",
            amount="20",
            user=self.test_user1,
        )

        expense_repository.add_expense(
            date="12/03/2025",
            description="Groceries",
            amount="33",
            user=self.test_user1,
        )

        filtered_expenses, sum = expense_repository.expenses_by_user_filtered_by_date(
            self.test_user1, "2025-04-20", "2025-05-25"
        )

        expense = filtered_expenses.iloc[0]

        print(filtered_expenses)

        # self.assertEqual(filtered_expenses.shape(), (1, 4))
        self.assertEqual(sum, 20.00)
        self.assertEqual(expense.Date, "2025-05-25")
