from tkinter import ttk, Entry, Button, messagebox
from tkinter.ttk import Style
from services.expense_service import expense_service


class LoginView:
    def __init__(self, root, create_user_view, expense_tracker_view):
        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._create_user_view = create_user_view
        self._expense_tracker_view = expense_tracker_view

        self._initialise()

    def pack(self):
        # self._frame.pack(fill=constants.BOTH)
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _login(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            expense_service.login(username, password)
            self._expense_tracker_view()
        except:
            messagebox.showerror("Error", "Try Again")

    def _initialise(self):
        self._root.geometry("650x400")
        self._root.configure(bg="#333333")

        s = Style()
        s.configure("TFrame", background="#333333", foreground="white")

        self._frame = ttk.Frame(master=self._root, style="TFrame")

        login_label = ttk.Label(
            master=self._frame,
            text="Login",
            background="#333333",
            foreground="white",
            font=["Arial", 30],
        )
        login_label.configure(anchor="center")
        login_label.grid(row=0, column=0, columnspan=2, pady=40)

        # Initialise username field
        username_label = ttk.Label(
            master=self._frame,
            text="Username",
            background="#333333",
            foreground="white",
            font=["Arial", 16],
        )

        username_label.grid(row=1, column=0)
        self._username_entry = Entry(master=self._frame)
        self._username_entry.grid(row=1, column=1, padx=5)

        # Initialise password field
        password_label = ttk.Label(
            master=self._frame,
            text="Password",
            background="#333333",
            foreground="white",
            font=["Arial", 16],
        )
        # password_label.configure(style="My.TFrame")
        password_label.grid(row=2, column=0, pady=20, padx=5)
        self._password_entry = Entry(master=self._frame, show="*")
        self._password_entry.grid(row=2, column=1)

        # Buttons
        login_button = Button(
            master=self._frame,
            text="Login",
            command=self._login,
            background="#20bd65",
            foreground="black",
        )
        login_button.grid(row=3, column=0, columnspan=2, pady=15)

        create_user_button = Button(
            master=self._frame,
            text="Create New Account",
            command=self._create_user_view,
            background="#20bd65",
            foreground="black",
        )
        create_user_button.grid(row=4, column=0, columnspan=2, pady=5)
