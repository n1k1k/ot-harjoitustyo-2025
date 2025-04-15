import unittest
from entities.user import User
from repositories.user_repository import user_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        self._test_user = User("SpongeBob", "sb123")

    def test_create_user(self):
        user_repository.create_user(self._test_user)

        cursor = user_repository._db.cursor()
        cursor.execute("select * from users")
        found_users = cursor.fetchall()

        self.assertEqual(len(found_users), 1)
        self.assertEqual(found_users[0]["username"], self._test_user.username)

    def test_find_by_username(self):
        user_repository.create_user(self._test_user)

        found_user = user_repository.find_by_username(self._test_user.username)

        self.assertEqual(found_user.username, self._test_user.username)

    def test_find_by_username_returns_False_if_user_does_no_exist(self):
        found_user = user_repository.find_by_username("test")

        self.assertFalse(found_user)
