from tkinter import ttk, Button, messagebox, CENTER, Toplevel
from tkinter.ttk import Style
from services.expense_service import expense_service


class ExpenseTrackerView:
    def __init__(
        self,
        root,
        login_view,
    ):
        self._root = root
        self._login_view = login_view
        self._frame = None
        self._toplevel = None
        self._user = expense_service.get_current_user()

        self._initialise()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        if self._toplevel:
            self._toplevel.destroy()

        self._frame.destroy()

    def _logout(self):
        try:
            expense_service.logout()
            self._login_view()
        except:
            messagebox.showerror("Error")

    def _add_expense(self):
        date = self._date_entry.get()
        description = self._category_entry.get()
        amount = self._amount_entry.get()

        try:
            expense_service.create_expense(date, description, amount)
            self.destroy()
            self._initialise()
            self.pack()
        except:
            messagebox.showerror("Error", "Try Again")

    def _add_expense_window(self):
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

        date_label.grid(row=0, column=0, pady=(30, 0), padx=10)
        self._date_entry.grid(row=0, column=1, pady=(30, 0))
        category_label.grid(row=1, column=0, pady=(15, 0), padx=10)
        self._category_entry.grid(row=1, column=1, pady=(15, 0))
        amount_label.grid(row=2, column=0, pady=(15, 0), padx=10)
        self._amount_entry.grid(row=2, column=1, pady=(15, 0))
        add_expense_button.grid(row=3, column=0, columnspan=2, pady=(40, 20))

    def _initialise(self):
        self._root.geometry("600x400")
        self._root.configure(bg="#333333")

        s = Style()
        s.configure("TFrame", background="#333333", foreground="white")

        self._frame = ttk.Frame(master=self._root, style="TFrame")

        expense_label = ttk.Label(
            master=self._frame,
            text="Resent Expenses",
            background="#333333",
            foreground="white",
            font=["Arial", 15],
        )

        expense_tree = ttk.Treeview(
            self._frame, column=("c1", "c2", "c3"), show="headings", height=10
        )

        expense_tree.column("# 1", anchor=CENTER)
        expense_tree.heading("# 1", text="Date")
        expense_tree.column("# 2", anchor=CENTER)
        expense_tree.heading("# 2", text="Category")
        expense_tree.column("# 3", anchor=CENTER)
        expense_tree.heading("# 3", text="Amount")

        expenses = expense_service.get_expenses()

        for index, row in expenses.iterrows():
            num = index + 1
            i = str(num)
            expense_tree.insert(
                "",
                "end",
                text=i,
                values=(row["Date"], row["Description"], row["Amount"]),
            )

        add_expense_button = Button(
            master=self._frame,
            text="Add Expense",
            background="#20bd65",
            command=self._add_expense_window,
            foreground="black",
        )

        view_all_expenses_button = Button(
            master=self._frame,
            text="View All Expenses",
            background="#dde645",
            foreground="black",
        )

        logout_button = Button(
            master=self._frame,
            text="Log out",
            command=self._logout,
            background="#d13b3b",
            foreground="black",
        )

        expense_label.grid(row=0, column=1, pady=(15, 10))
        expense_tree.grid(row=1, column=0, pady=(0, 20), columnspan=3)
        add_expense_button.grid(row=2, column=0, pady=20)
        # view_all_expenses_button.grid(row=2, column=1)
        logout_button.grid(row=2, column=2)
