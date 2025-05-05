from tkinter import ttk, Entry, Button, messagebox, constants
from tkinter.ttk import Style
from services.expense_service import expense_service, UsernameExistsError


class CreateUserView:
    """User interface for creating a new user"""

    def __init__(self, root, login_view, expense_tracker_view):
        """Class constructor.

        Args:
            root: TKinter Tk-application object.
            login_view: The method called when switching to LoginView.
            expense_tracker_view: The method called when switching to ExpenseTrackerView.
        """

        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._login_view = login_view
        self._expense_tracker_view = expense_tracker_view

        self._initialise()

    def pack(self):
        """Displays the view."""
        self._frame.pack()

    def destroy(self):
        """Destroys the view."""
        self._frame.destroy()

    def _create_user(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) <= 2 or len(password) <= 2:
            messagebox.showerror(
                "Error",
                "Account could not be created. Both username and password are required and they must be  at least 3 characters.",
            )
        else:
            try:
                user = expense_service.create_user(username, password)
                expense_service.login(user.username, user.password)
                self._expense_tracker_view()
            except UsernameExistsError:
                messagebox.showerror("Error", f'Username "{username}" is already taken')

    def _initialise(self):
        self._root.geometry("670x450")
        self._root.configure(bg="#333333")

        s = Style()
        s.configure("TFrame", background="#333333", foreground="white")

        self._frame = ttk.Frame(master=self._root, style="TFrame")

        welcome_label = ttk.Label(
            master=self._frame,
            text="Welcome!",
            background="#333333",
            foreground="white",
            font=["Arial", 30],
        )
        welcome_label.configure(anchor="center")
        welcome_label.grid(row=0, column=0, columnspan=2, pady=(25, 5))

        create_label = ttk.Label(
            master=self._frame,
            text="Create a new account",
            background="#333333",
            foreground="white",
            font=["Arial", 22],
        )
        create_label.configure(anchor="center")
        create_label.grid(row=1, column=0, columnspan=2, pady=(0, 40))

        username_label = ttk.Label(
            master=self._frame,
            text="Username",
            background="#333333",
            foreground="white",
            font=["Arial", 16],
        )

        username_label.grid(row=2, column=0)
        self._username_entry = Entry(master=self._frame)
        self._username_entry.grid(row=2, column=1, padx=5)

        password_label = ttk.Label(
            master=self._frame,
            text="Password",
            background="#333333",
            foreground="white",
            font=["Arial", 16],
        )

        password_label.grid(row=3, column=0, pady=20, padx=5)
        self._password_entry = Entry(master=self._frame, show="*")
        self._password_entry.grid(row=3, column=1)

        login_button = Button(
            master=self._frame,
            text="Back to Login",
            command=self._login_view,
            background="lightgray",
            foreground="black",
        )
        login_button.grid(row=5, column=0, columnspan=2)

        create_user_button = Button(
            master=self._frame,
            text="Create New Account",
            command=self._create_user,
            background="#60a9eb",
            foreground="black",
        )
        create_user_button.grid(row=4, column=0, columnspan=2, pady=(35, 25))
