from entities.user import User

from repositories.user_repository import user_repository as default_user_repository

from repositories.expense_repository import (
    expense_repository as default_expense_repository,
)


class UsernameExistsError(Exception):
    pass


class DeleteError(Exception):
    pass


class ExpenseService:
    def __init__(self, user_repository, expense_repository):
        self._user = None
        self._user_repository = user_repository
        self._expense_repository = expense_repository

    def get_current_user(self):
        return self._user

    def get_expenses(self):
        expense_df = self._expense_repository.expenses_by_user(self._user)
        return expense_df

    def add_expense(self, date, description, amount):
        user = self.get_current_user()
        return self._expense_repository.add_expense(date, description, amount, user)

    def delete_expense(self, date, category, amount):
        user = self.get_current_user().username

        try:
            default_expense_repository.delete_one_expense(date, category, amount, user)
        except:
            raise DeleteError("Record could not be deleted")

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise ValueError

        self._user = user

        return user

    def logout(self):
        self._user = None

    def create_user(self, username, password):
        check_username = self._user_repository.find_by_username(username)

        if check_username:
            raise UsernameExistsError(f"Username {username} is already taken")

        user = self._user_repository.create_user(User(username, password))
        self._user = user

        return user

    def create_expense(self, date, description, amount):
        self._expense_repository.add_expense(date, description, amount, self._user)


expense_service = ExpenseService(default_user_repository, default_expense_repository)
