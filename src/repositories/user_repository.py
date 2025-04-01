from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    def __init__(self, db):
        self._db = db

    def create_user(self, user):
        cursor = self._db.cursor()

        cursor.execute(
            "insert into users (username, password) values (?,?)",
            (user.username, user.password),
        )

        self._db.commit()

        return user

    def find_by_username(self, username):
        cursor = self._db.cursor()

        cursor.execute("select * from users where username = ?", (username,))
        row = cursor.fetchone()

        try:
            user = User(row["username"], row["password"]) if row else False
        except:
            return False

        return user


db = get_database_connection()
user_repository = UserRepository(db)
