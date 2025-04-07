from tkinter import ttk, Button, messagebox, Text
from tkinter.ttk import Style
from services.expense_service import expense_service


class CreateExpenseView:
    def __init__(self, root, expense_tracker_view):
        self._root = root
        self._expense_tracker_view = expense_tracker_view
        self._frame = None
        self._user = expense_service.get_current_user()

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

        add_expense_button = Button(
            master=self._frame,
            text="Add Expense",
            background="#797f85",
            foreground="black",
        )
        add_expense_button.grid(row=1, column=0, columnspan=2, pady=(20))

        return_button = Button(
            master=self._frame,
            text="Return",
            command=self._expense_tracker_view,
            background="#797f85",
            foreground="black",
        )
        return_button.grid(row=2, column=0, columnspan=2, pady=(20))
