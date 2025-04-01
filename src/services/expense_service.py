from entities.user import User

from repositories.user_repository import user_repository as default_user_repository


class ExpenseService:
    def __init__(self, user_repository):
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        user = self._user_reposiotry.find_by_username(username)

        if not user or user.password != password:
            print("Invalid username or password")
            return False

        self._user = user

        return user

    def logout(self):
        pass

    def create_user(self, username, password):
        check_username = self._user_repository.find_by_username(username)

        if check_username:
            return False

        user = self._user_repository.create_user(User(username, password))
        self._user = user

        return user


expense_service = ExpenseService(default_user_repository)
