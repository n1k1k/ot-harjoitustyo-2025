from entities.user import User

from repositories.user_repository import user_repository as default_user_repository

from repositories.expense_repository import (
    expense_repository as default_expense_repository,
)


class UsernameExistsError(Exception):
    """
    Raised if the username already exists, when attempting to create a new user.
    """

    pass


class DeleteError(Exception):
    """
    Raised when an expense record cannot be deleted.
    """

    pass


class AuthenticationError(Exception):
    """
    Raised when the give password does not match the password in the database.
    """

    pass


class UserNotFoundError(Exception):
    """
    Raised when the given username is not found in the database.
    """

    pass


class ExpenseService:
    """
    Class responsible for the application logic.

    Attributes:
        user_repository: An instance of class UserRepository.
        expense_repository: An instance of class ExpenseReposiotry.

    """

    def __init__(self, user_repository, expense_repository):
        """
        Class constructor. Creates a new service that is responsible for the application logic.

        Args:
            user_repository: An instance of class UserRepository, that manages user records.
            expense_repository: An instance of class ExpenseReposiotry, that manages
            expense records.
        """

        self._user = None
        self._user_repository = user_repository
        self._expense_repository = expense_repository

    def get_current_user(self):
        """
        Fetches the user that is currently logged-in.

        Returns:
            An instance of class User if user is logged-in, otherwise None.
        """

        return self._user

    def get_expenses(self):
        """
        Fetches the expenses for the currently logged-in user.

        Returns:
            A pandas DataFrame containing the user's expenses if user logged-in, otherwise None.
        """

        expenses = self._expense_repository.expenses_by_user(self._user)
        return expenses

    def get_expenses_filtered_by_date(self, from_date, to_date):

        user = self.get_current_user()
        expenses = self._expense_repository.expenses_by_user_filtered_by_date(
            user, from_date, to_date
        )

        return expenses

    def get_expense_sum(self):
        """
        Fetches the total sum of expenses for the user that is currently logged-in.

        Returns:
            Total sum of expenses for the logged-in user.
        """

        user = self.get_current_user()

        return self._expense_repository.expense_sum(user)

    def create_expense(self, date, description, amount):
        """
        Creates a new expense.

        Args:
            date: Date of the expense.
            category: Description (category) of the expense.
            amount: Amount spent.


        Returns:
            The created expense
        """

        user = self.get_current_user()
        return self._expense_repository.add_expense(date, description, amount, user)

    def delete_expense(self, date, category, amount):
        """
        Deletes a specified expense record for the currently logged-in user.

        Args:
            date: Date of the expense.
            category: Description (category) of the expense.
            amount: Amount spent.

        Raises:
            DeleteError if the record could not be deleted.
        """

        user = self.get_current_user().username

        try:
            default_expense_repository.delete_one_expense(date, category, amount, user)
        except Exception as exc:
            raise DeleteError("Record could not be deleted") from exc

    def login(self, username, password):
        """
        Authenticates a user by username and password.

        Args:
            username: The user's username.
            password: The user's password.

        Returns:
            The authenticated user if user found and password matches.

        Raises:
            AuthenticationError is the given password does not match the one on
            record or UserNotFounError if the given username does not exist.
        """

        user = self._user_repository.find_by_username(username)

        if not user:
            raise UserNotFoundError("User not found")

        if user.password != password:
            raise AuthenticationError("Passwords do not match")

        self._user = user

        return user

    def logout(self):
        """
        Logs out the current user.
        """

        self._user = None

    def create_user(self, username, password):
        """
        Creates a new instance of class User.

        Args:
            username: The username for the user.
            password: The password for the user.

        Returns:
            The instance of class User that was created.

        """

        check_username = self._user_repository.find_by_username(username)

        if check_username:
            raise UsernameExistsError(f"Username {username} is already taken")

        user = self._user_repository.create_user(User(username, password))
        self._user = user

        return user


expense_service = ExpenseService(default_user_repository, default_expense_repository)
