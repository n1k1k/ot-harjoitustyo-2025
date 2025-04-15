import unittest
from repositories.expense_repository import expense_repository
from repositories.user_repository import user_repository
from entities.user import User


class TestExpenseRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        expense_repository.delete_all_expenses()
        self._test_user1 = User("SpongeBob", "sb123")

    def test_add_expense(self):
        expense_repository.add_expense(
            date="25/06/2003",
            description="Groceries",
            amount="25",
            user=self._test_user1,
        )

        expenses = expense_repository.all_expenses()

        self.assertEqual(expenses.shape[0], 1)
        self.assertEqual(expenses.iloc[0]["Date"], "25/06/2003")
        self.assertEqual(expenses.iloc[0]["Description"], "Groceries")
        self.assertEqual(expenses.iloc[0]["Amount"], 25)
        self.assertEqual(expenses.iloc[0]["User"], self._test_user1.username)
