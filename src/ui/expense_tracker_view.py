from tkinter import ttk, Button, messagebox, CENTER, Toplevel, constants
from tkinter.ttk import Style
from tkcalendar import DateEntry
from services.expense_service import expense_service, DeleteError


class ExpenseTrackerView:
    """User interface for displaying the users expenses and managing them."""

    def __init__(
        self,
        root,
        login_view,
    ):
        """Class constructor.

        Args:
            root: TKinter Tk-application object.
            login_view: The method called when switching to LoginView.
        """

        self._root = root
        self._login_view = login_view
        self._frame = None
        self._toplevel = None
        self._user = expense_service.get_current_user()

        self._initialise()

    def pack(self):
        """Displays the view."""
        self._frame.pack()

    def destroy(self):
        """Destroys the view."""
        if self._toplevel:
            self._toplevel.destroy()

        self._frame.destroy()

    def _get_selected_expense(self):
        selection = self._expense_tree.selection()
        if selection == ():
            return False

        return selection

    def _change_expense_records(self):
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
            float(amount)
        except:
            messagebox.showerror(
                "Error",
                "Amount must be a number and the decimal separator a dot (.)",
            )
            return

        try:
            expense_service.create_expense(date, description, amount)
            self._change_expense_records()
        except:
            messagebox.showerror("Error", "Try Again")

    def _edit_expense(self):
        selection = self._get_selected_expense()
        if not selection:
            return

        expense = selection[0]
        date, category, amount = self._expense_tree.item(expense)["values"]

        try:
            self._edit_expense_window(date, category, amount)
        except:
            messagebox.showerror("Error", "Try again")
            return

    def _handle_edit_expense(self):
        date = self._date_entry.get_date()
        description = self._category_entry.get()
        amount = self._amount_entry.get()

        try:
            float(amount)
        except:
            messagebox.showerror(
                "Error",
                "Amount must be a number and the decimal separator a dot (.)",
            )
            return

        try:
            expense_service.create_expense(date, description, amount)
            self._delete_expense()
            self._change_expense_records()
            self._toplevel.destroy()
        except:
            messagebox.showerror("Error", "Try Again")
            return False

    def _delete_expense(self):
        selection = self._get_selected_expense()
        if not selection:
            return

        expense = selection[0]
        date, category, amount = self._expense_tree.item(expense)["values"]

        try:
            expense_service.delete_expense(date, category, amount)
            self._change_expense_records()
        except DeleteError:
            messagebox.showerror("Error", "Record was not deleted. Try again!")

    def _apply(self):
        pass

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

    def _edit_expense_window(self, date, category, amount):
        self._toplevel = Toplevel(self._root)
        self._toplevel.geometry("340x250")
        self._toplevel.config(bg="#333333")
        self._toplevel.title("Edit")

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
            master=toplevel_frame, locale="en_US", date_pattern="yyyy-mm-dd"
        )
        self._date_entry.set_date(date)

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

        i = categories.index(category)
        self._category_entry.current(i)

        amount_label = ttk.Label(
            master=toplevel_frame,
            text="Amount",
            background="#333333",
            foreground="white",
            font=["Arial", 11],
        )
        self._amount_entry = ttk.Entry(master=toplevel_frame)
        self._amount_entry.insert("end", amount)

        edit_expense_button = Button(
            master=toplevel_frame,
            text="Update Expense",
            command=self._handle_edit_expense,
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
        edit_expense_button.grid(row=3, column=0, columnspan=2, pady=(40, 20))

    def _initialise(self):
        self._root.geometry("650x400")
        self._root.configure(bg="#333333")

        s = Style()
        s.configure("TFrame", background="#333333", foreground="white")

        self._frame = ttk.Frame(master=self._root, style="TFrame")

        from_date_label = ttk.Label(
            master=self._frame,
            text="from",
            background="#333333",
            foreground="white",
            font=["Arial", 11],
        )
        self._from_date_entry = DateEntry(
            master=self._frame, locale="en_US", date_pattern="yyyy-mm-dd"
        )

        to_date_label = ttk.Label(
            master=self._frame,
            text="to",
            background="#333333",
            foreground="white",
            font=["Arial", 11],
        )
        self._to_from_date_entry = DateEntry(
            master=self._frame, locale="en_US", date_pattern="yyyy-mm-dd"
        )

        apply_button = Button(
            master=self._frame,
            text="Apply",
            background="#20bd65",
            command=self._apply,
            foreground="black",
        )

        frame = ttk.Frame(self._frame, width=60)

        self._expense_tree = ttk.Treeview(
            frame,
            column=("c1", "c2", "c3"),
            show="headings",
            height=13,
            selectmode="browse",
        )

        self._expense_tree.column("# 1", anchor=CENTER)
        self._expense_tree.heading("# 1", text="Date (yyyy-mm-dd)")
        self._expense_tree.column("# 2", anchor=CENTER)
        self._expense_tree.heading("# 2", text="Category")
        self._expense_tree.column("# 3", anchor=CENTER)
        self._expense_tree.heading("# 3", text="Amount (€)")

        scrollbar = ttk.Scrollbar(
            frame, orient="vertical", command=self._expense_tree.yview
        )
        self._expense_tree.configure(yscrollcommand=scrollbar.set)

        expenses = expense_service.get_expenses()

        for index, row in expenses.iterrows():
            amount = row["Amount"]
            i = index + 1
            self._expense_tree.insert(
                "",
                "end",
                text=str(i),
                values=(row["Date"], row["Description"], f"{amount:.2f}"),
            )

        sum = expense_service.get_expense_sum()
        expense_total = ttk.Label(
            self._frame,
            text=f" Total: {sum:.2f}",
            background="lightgray",
            foreground="black",
        )

        add_expense_button = Button(
            master=self._frame,
            text="Add Expense",
            background="#20bd65",
            command=self._add_expense_window,
            foreground="black",
        )

        edit_expense_button = Button(
            master=self._frame,
            text="Edit",
            background="#ddf542",
            command=self._edit_expense,
            foreground="black",
        )

        delete_expense_button = Button(
            master=self._frame,
            text="Delete",
            background="#d13b3b",
            command=self._delete_expense,
            foreground="black",
        )

        logout_button = Button(
            master=self._frame,
            text="Log out",
            command=self._logout,
            background="gray",
            foreground="black",
        )

        from_date_label.grid(row=0, column=0, pady=10)
        self._from_date_entry.grid(row=0, column=1)
        to_date_label.grid(row=0, column=2)
        self._to_from_date_entry.grid(row=0, column=3)
        apply_button.grid(row=0, column=4)
        frame.grid(row=1, column=0, columnspan=5, padx=5, pady=0)
        self._expense_tree.pack(side="left")
        scrollbar.pack(side="right", fill="y")
        expense_total.grid(row=2, column=0, columnspan=5, sticky="ew", padx=5)
        add_expense_button.grid(row=3, column=0, pady=(15, 20))
        edit_expense_button.grid(row=3, column=1)
        delete_expense_button.grid(row=3, column=2)
        logout_button.grid(row=3, column=4)
