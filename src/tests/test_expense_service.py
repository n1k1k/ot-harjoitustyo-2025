import unittest
from database_connection import get_database_connection
from services.expense_service import ExpenseService
from repositories.user_repository import UserRepository


class TestExpenseService(unittest.TestCase):
    def setUp(self):
        self._user_repository = UserRepository(get_database_connection())
        self._expense_service = ExpenseService(self._user_repository)

    def test_username_is_set_correctly_when_new_user_is_created(self):
        username = "name"
        password = "password"

        user = self._expense_service.create_user(username, password)
        self.assertEqual(user.username, "name")
