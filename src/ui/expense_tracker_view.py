from tkinter import ttk, Button, messagebox, CENTER, RIGHT
from tkinter.ttk import Style
from services.expense_service import expense_service


class ExpenseTrackerView:
    def __init__(self, root, login_view, create_expense_view):
        self._root = root
        self._login_view = login_view
        self._create_expense_view = create_expense_view
        self._frame = None
        self._add_expense_view = None
        self._user = expense_service.get_current_user()

        self._initialise()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _logout(self):
        try:
            expense_service.logout()
            self._login_view()
        except:
            messagebox.showerror("Error")

    def _initialise(self):
        self._root.geometry("600x400")
        self._root.configure(bg="#333333")

        s = Style()
        s.configure("TFrame", background="#333333", foreground="white")

        self._frame = ttk.Frame(master=self._root, style="TFrame")

        expenses = expense_service.get_expenses()

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
            command=self._create_expense_view,
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
        view_all_expenses_button.grid(row=2, column=1)
        logout_button.grid(row=2, column=2)
