from database_connection import get_database_connection


def drop_tables(db):
    """
    Deletes table users if it exists.

    Args:
        db: A sqlite3.Connection object.
    """

    cursor = db.cursor()

    cursor.execute(
        """
        drop table if exists users;
    """
    )

    db.commit()


def create_tables(db):
    """
    Creates table users.

    Args:
        db: A sqlite3.Connection object.
    """

    cursor = db.cursor()

    cursor.execute(
        """
        create table users (
            username text primary key,
            password text
        );
    """
    )

    db.commit()


def initialise_database():
    """
    Initialises the database tables.
    """

    db = get_database_connection()

    drop_tables(db)
    create_tables(db)


if __name__ == "__main__":
    initialise_database()
