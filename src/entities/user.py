class User:
    """
    A class that defines a singular user.
    """

    def __init__(self, username, password):
        """Class constructor.

        Args:
            username: String that is the user's username.
            password: String that is the user's password.
        """
        self.username = str(username)
        self.password = str(password)
