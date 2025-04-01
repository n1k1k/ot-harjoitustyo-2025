from tkinter import ttk, Button
from tkinter.ttk import Style


class ExpenseTrackerView:
    def __init__(self, root, login_view):
        self._root = root
        self._login_view = login_view

        self._initialise()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialise(self):
        self._root.geometry("600x400")
        self._root.configure(bg="#333333")

        s = Style()
        s.configure("TFrame", background="#333333", foreground="white")

        self._frame = ttk.Frame(master=self._root, style="TFrame")

        logout_button = Button(
            master=self._frame,
            text="Log out",
            command=self._login_view,
            background="#797f85",
            foreground="black",
        )
        logout_button.grid(row=1, column=0, columnspan=2, pady=(300))
