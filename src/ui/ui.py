from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.expense_tracker_view import ExpenseTrackerView


class UI:
    """
    Class responsible for the user interface of the application.
    """

    def __init__(self, root):
        """
        Class constructor.

        Args:
            root: TKinter Tk-application object.
        """

        self._root = root
        self._frame = None
        self._current_view = None

    def start(self):
        """
        Starts the user interface of the application.
        """

        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root, self._show_create_user_view, self._show_expense_tracker_view
        )
        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root, self._show_login_view, self._show_expense_tracker_view
        )
        self._current_view.pack()

    def _show_expense_tracker_view(self):
        self._hide_current_view()

        self._current_view = ExpenseTrackerView(self._root, self._show_login_view)

        self._current_view.pack()
