from tkinter import ttk, Button, messagebox, Text, constants, Toplevel
from tkinter.ttk import Style
from services.expense_service import expense_service


class CreateExpenseView:
    def __init__(self, root, expense_tracker_view):
        self._root = root
        self._expense_tracker_view = expense_tracker_view
        # self._frame = None
        self._toplevel = None
        self._user = expense_service.get_current_user()

        self._initialise_test()

    def pack(self):
        pass
        self._frame.pack()

    def destroy(self):
        self._toplevel.destroy()
        # self._frame.destroy()

    def _add_expense(self):
        date = self._date_entry.get()
        description = self._category_entry.get()
        amount = self._amount_entry.get()

        try:
            expense_service.create_expense(date, description, amount)

            self._expense_tracker_view()
        except:
            messagebox.showerror("Error", "Try Again")

    """
    def _initialise(self):
        self._root.geometry("600x400")
        self._root.configure(bg="#333333")

        s = Style()
        s.configure("TFrame", background="#333333", foreground="white")

        self._frame = ttk.Frame(master=self._root, style="TFrame")

        date_label = ttk.Label(
            master=self._frame,
            text="Date",
            background="#333333",
            foreground="white",
            font=["Arial", 14],
        )
        self._date_entry = ttk.Entry(master=self._frame)

        category_label = ttk.Label(
            master=self._frame,
            text="Description",
            background="#333333",
            foreground="white",
            font=["Arial", 14],
        )
        self._category_entry = ttk.Entry(master=self._frame)

        amount_label = ttk.Label(
            master=self._frame,
            text="Amount",
            background="#333333",
            foreground="white",
            font=["Arial", 14],
        )
        self._amount_entry = ttk.Entry(master=self._frame)

        add_expense_button = Button(
            master=self._frame,
            text="Add Expense",
            command=self._add_expense,
            background="#797f85",
            foreground="black",
        )

        return_button = Button(
            master=self._frame,
            text="Return",
            command=self._expense_tracker_view,
            background="#797f85",
            foreground="black",
        )

        date_label.grid(row=0, column=0, pady=(30, 0), padx=10)
        self._date_entry.grid(row=0, column=1, pady=(30, 0))
        category_label.grid(row=1, column=0, pady=(15, 0), padx=10)
        self._category_entry.grid(row=1, column=1, pady=(15, 0))
        amount_label.grid(row=2, column=0, pady=(15, 0), padx=10)
        self._amount_entry.grid(row=2, column=1, pady=(15, 0))
        add_expense_button.grid(row=3, column=0, columnspan=2, pady=(40, 20))
        return_button.grid(row=4, column=0, columnspan=2, pady=(10))
    """

    def _initialise_test(self):
        self._toplevel = Toplevel(self._root)

        date_label = ttk.Label(
            master=self._toplevel,
            text="Date",
            background="#333333",
            foreground="white",
            font=["Arial", 14],
        )
        self._date_entry = ttk.Entry(master=self._toplevel)

        category_label = ttk.Label(
            master=self._toplevel,
            text="Description",
            background="#333333",
            foreground="white",
            font=["Arial", 14],
        )
        self._category_entry = ttk.Entry(master=self._toplevel)

        amount_label = ttk.Label(
            master=self._toplevel,
            text="Amount",
            background="#333333",
            foreground="white",
            font=["Arial", 14],
        )
        self._amount_entry = ttk.Entry(master=self._toplevel)

        add_expense_button = Button(
            master=self._toplevel,
            text="Add Expense",
            command=self._add_expense,
            background="#797f85",
            foreground="black",
        )

        """return_button = Button(
            master=self._toplevel,
            text="Return",
            command=self._expense_tracker_view,
            background="#797f85",
            foreground="black",
        )"""

        date_label.grid(row=0, column=0, pady=(30, 0), padx=10)
        self._date_entry.grid(row=0, column=1, pady=(30, 0))
        category_label.grid(row=1, column=0, pady=(15, 0), padx=10)
        self._category_entry.grid(row=1, column=1, pady=(15, 0))
        amount_label.grid(row=2, column=0, pady=(15, 0), padx=10)
        self._amount_entry.grid(row=2, column=1, pady=(15, 0))
        add_expense_button.grid(row=3, column=0, columnspan=2, pady=(40, 20))
        # return_button.grid(row=4, column=0, columnspan=2, pady=(10))
