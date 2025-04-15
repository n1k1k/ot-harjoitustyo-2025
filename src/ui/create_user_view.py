from tkinter import ttk, Entry, Button, messagebox, constants
from tkinter.ttk import Style
from services.expense_service import expense_service, UsernameExistsError


class CreateUserView:
    def __init__(self, root, login_view, expense_tracker_view):
        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._login_view = login_view
        self._expense_tracker_view = expense_tracker_view

        self._initialise()

    def pack(self):
        self._frame.pack()

    def destroy(self):
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
                expense_service.create_user(username, password)
                expense_service.login(username, password)
                self._expense_tracker_view()
            except UsernameExistsError:
                messagebox.showerror("Error", f'Username "{username}" is already taken')

    def _initialise(self):
        self._root.geometry("650x400")
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

        # Initialise username field
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

        # Initialise password field
        password_label = ttk.Label(
            master=self._frame,
            text="Password",
            background="#333333",
            foreground="white",
            font=["Arial", 16],
        )
        # password_label.configure(style="My.TFrame")
        password_label.grid(row=3, column=0, pady=20, padx=5)
        self._password_entry = Entry(master=self._frame, show="*")
        self._password_entry.grid(row=3, column=1)

        # Buttons
        login_button = Button(
            master=self._frame,
            text="Back to Login",
            command=self._login_view,
            background="#797f85",
            foreground="black",
        )
        login_button.grid(row=5, column=0, columnspan=2)

        create_user_button = Button(
            master=self._frame,
            text="Create New Account",
            command=self._create_user,
            background="#20bd65",
            foreground="black",
        )
        create_user_button.grid(row=4, column=0, columnspan=2, pady=(15, 20))
