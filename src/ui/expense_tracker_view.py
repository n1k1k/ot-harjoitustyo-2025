from tkinter import ttk, Button, messagebox, Text, END, CENTER
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
        # print(expenses)

        """

        expense_list = Text(master=self._frame, height=10, width=60)
        expense_list.grid(row=0, column=0, pady=20)

        for index, row in expenses.iterrows():
            expense = f"Date: {row['Date']} Description: {row['Description']} Amount: {row['Amount']}"
            expense_list.insert(END, expense)
        """

        tree = ttk.Treeview(
            self._frame, column=("c1", "c2", "c3"), show="headings", height=5
        )

        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Date")

        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Category")

        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Amount")

        for index, row in expenses.iterrows():
            num = index + 1
            i = str(num)
            tree.insert(
                "",
                "end",
                text=i,
                values=(row["Date"], row["Description"], row["Amount"]),
            )

        tree.grid(row=0, column=0, pady=20)

        add_expense_button = Button(
            master=self._frame,
            text="Add Expense",
            background="#797f85",
            command=self._create_expense_view,
            foreground="black",
        )
        add_expense_button.grid(row=1, column=0, columnspan=2, pady=(20))

        logout_button = Button(
            master=self._frame,
            text="Log out",
            command=self._logout,
            background="#797f85",
            foreground="black",
        )
        logout_button.grid(row=2, column=0, columnspan=2, pady=(0))
