from entities.user import User

db = None


class UserRepository:
    def __init__self(self, db):
        self._db = db


user_repository = UserRepository(db)
