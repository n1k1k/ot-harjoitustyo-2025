from tkinter import ttk, Button, messagebox, CENTER, BOTH, Y, Toplevel, constants
from tkinter.ttk import Style
from tkcalendar import DateEntry
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

    def _new_expense_handler(self):
        self._frame.destroy()
        self._initialise()
        self.pack()

    def _logout(self):
        try:
            expense_service.logout()
            self._login_view()
        except:
            messagebox.showerror("Error")

    def _add_expense(self):
        date = self._date_entry.get_date()
        description = self._category_entry.get()
        amount = self._amount_entry.get()

        try:
            expense_service.create_expense(date, description, amount)
            self._handel_new_expense()
        except:
            messagebox.showerror("Error", "Try Again")

    def _add_expense_window(self):
        self._toplevel = Toplevel(self._root)
        self._toplevel.geometry("340x250")
        self._toplevel.config(bg="#333333")
        self._toplevel.title("Add Expense")

        toplevel_frame = ttk.Frame(self._toplevel)
        toplevel_frame.pack(fill=constants.Y)

        date_label = ttk.Label(
            master=toplevel_frame,
            text="Date (DD/MM/YYY)",
            background="#333333",
            foreground="white",
            font=["Arial", 11],
        )
        self._date_entry = DateEntry(
            master=toplevel_frame, locale="en_US", date_pattern="dd/mm/yyyy"
        )

        category_label = ttk.Label(
            master=toplevel_frame,
            text="Category",
            background="#333333",
            foreground="white",
            font=["Arial", 11],
        )

        categories = [
            "Housing",
            "Utilities",
            "Transportation",
            "Groceries",
            "Restaurants",
            "Healthcare",
            "Entertainment",
            "Clothing",
            "Other",
        ]
        self._category_entry = ttk.Combobox(
            master=toplevel_frame, state="readonly", values=categories
        )

        amount_label = ttk.Label(
            master=toplevel_frame,
            text="Amount",
            background="#333333",
            foreground="white",
            font=["Arial", 11],
        )
        self._amount_entry = ttk.Entry(master=toplevel_frame)

        add_expense_button = Button(
            master=toplevel_frame,
            text="Add Expense",
            command=self._add_expense,
            background="#dde645",
            foreground="black",
        )

        date_label.grid(row=0, column=0, pady=(30, 0), padx=(15, 0))
        category_label.grid(row=1, column=0, pady=(20, 0), padx=(15, 0))
        amount_label.grid(row=2, column=0, pady=(20, 0), padx=(15, 0))

        self._date_entry.grid(row=0, column=1, pady=(30, 0), sticky="w", padx=10)
        self._category_entry.config(width=18)
        self._category_entry.grid(row=1, column=1, pady=(20, 0), padx=10)
        self._amount_entry.config(width=19)
        self._amount_entry.grid(row=2, column=1, pady=(20, 0), padx=10)
        add_expense_button.grid(row=3, column=0, columnspan=2, pady=(40, 20))

    def _initialise(self):
        self._root.geometry("650x400")
        self._root.configure(bg="#333333")

        s = Style()
        s.configure("TFrame", background="#333333", foreground="white")

        self._frame = ttk.Frame(master=self._root, style="TFrame")

        frame = ttk.Frame(self._frame)

        expense_tree = ttk.Treeview(
            frame,
            column=("c1", "c2", "c3"),
            show="headings",
            height=13,
            selectmode="browse",
        )

        expense_tree.column("# 1", anchor=CENTER)
        expense_tree.heading("# 1", text="Date")
        expense_tree.column("# 2", anchor=CENTER)
        expense_tree.heading("# 2", text="Category")
        expense_tree.column("# 3", anchor=CENTER)
        expense_tree.heading("# 3", text="Amount (€)")

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=expense_tree.yview)
        expense_tree.configure(yscrollcommand=scrollbar.set)

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

        logout_button = Button(
            master=self._frame,
            text="Log out",
            command=self._logout,
            background="#d13b3b",
            foreground="black",
        )

        frame.grid(row=1, column=0, columnspan=2, padx=5, pady=(20, 10))
        expense_tree.pack(side="left")
        scrollbar.pack(side="right", fill="y")
        add_expense_button.grid(row=2, column=0, pady=20)
        logout_button.grid(row=2, column=1)
