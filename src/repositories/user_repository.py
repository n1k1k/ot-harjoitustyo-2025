from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """
    Repository for managing and storing user records in a SQLite database.
    """

    def __init__(self, db):
        """
        Class constructor.

        Args:
            db: A sqlite3.Connection object.
        """

        self._db = db

    def create_user(self, user):
        """
        Creates a new user and stores the user records in the database.

        Args:
            user: An instance of class User.

        Returns:
            The instance of class User that was stored in the database.
        """

        cursor = self._db.cursor()

        cursor.execute(
            "insert into users (username, password) values (?,?)",
            (user.username, user.password),
        )

        self._db.commit()

        return user

    def find_by_username(self, username):
        """
        Finds a user by their username from the database.

        Args:
            username: The username to search for.

        Returns:
            An instance of class User if user found, otherwise None.
        """

        cursor = self._db.cursor()

        cursor.execute("select * from users where username = ?", (username,))
        row = cursor.fetchone()

        user = User(row["username"], row["password"]) if row else None

        return user

    def delete_all_users(self):
        """
        Deletes all users from the database.
        """

        cursor = self._db.cursor()
        cursor.execute("delete from users")

        self._db.commit()


db_connection = get_database_connection()
user_repository = UserRepository(db_connection)
