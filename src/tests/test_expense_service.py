import unittest
import numpy as np
from services.expense_service import (
    ExpenseService,
    UsernameExistsError,
    UserNotFoundError,
    AuthenticationError,
)
from repositories.user_repository import user_repository
from repositories.expense_repository import expense_repository
from entities.user import User


class TestExpenseService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        expense_repository.delete_all_expenses()

        self.expense_service = ExpenseService(user_repository, expense_repository)
        self.test_user = User("SpongeBob", "sb123")

    def create_test_and_login_test_user(self):
        self.expense_service.create_user(
            self.test_user.username, self.test_user.password
        )

    def test_create_user_with_valid_username_and_password(self):
        username = "Patrick"
        password = "Start123"

        user = self.expense_service.create_user(username, password)
        self.assertEqual(user.username, "Patrick")

    def test_create_user_with_nonunique_username(self):
        self.create_test_and_login_test_user()
        username = self.test_user.username

        self.assertRaises(
            UsernameExistsError,
            lambda: self.expense_service.create_user(username, "random"),
        )

    def test_login_with_valid_credentials(self):
        self.create_test_and_login_test_user()
        self.expense_service.logout()

        result = self.expense_service.login(
            self.test_user.username, self.test_user.password
        )

        self.assertEqual(self.test_user.username, result.username)

    def test_login_with_nonexistant_username(self):
        self.assertRaises(
            UserNotFoundError,
            lambda: self.expense_service.login("random", "random"),
        )

    def test_login_with_invalid_password(self):
        self.create_test_and_login_test_user()
        self.expense_service.logout()

        username = self.test_user.username

        self.assertRaises(
            AuthenticationError,
            lambda: self.expense_service.login(username, "random"),
        )

    def test_get_current_user(self):
        self.create_test_and_login_test_user()

        result = self.expense_service.get_current_user()

        self.assertEqual(self.test_user.username, result.username)

    def test_create_expense(self):
        self.create_test_and_login_test_user()
        user = self.test_user.username

        all_expenses = self.expense_service.create_expense(
            "05-05-2025", "Transportation", 2.9
        )
        expense = all_expenses.iloc[0]

        self.assertEqual(all_expenses.shape, (1, 4))
        self.assertEqual(expense.Date, "05-05-2025")
        self.assertEqual(expense.Description, "Transportation")
        self.assertEqual(expense.Amount, 2.9)
        self.assertEqual(expense.User, user)

    def test_delete_expense(self):
        self.create_test_and_login_test_user()

        self.expense_service.create_expense("05-05-2025", "Transportation", 2.9)
        self.expense_service.delete_expense("05-05-2025", "Transportation", 2.9)

        expenses = self.expense_service.get_expenses()

        self.assertEqual(expenses.shape, (0, 4))

    def test_expense_sum(self):
        self.create_test_and_login_test_user()

        self.expense_service.create_expense("05-05-2025", "Transportation", 2.9)
        self.expense_service.create_expense("05-05-2025", "Groceries", 23)

        sum = self.expense_service.get_expense_sum()

        self.assertEqual(25.90, float(sum))
