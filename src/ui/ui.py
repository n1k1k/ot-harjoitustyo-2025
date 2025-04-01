from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.expence_tracker_view import ExpenceTrackerView


class UI:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root, self._show_create_user_view, self._show_expence_tracker_view
        )
        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root, self._show_login_view, self._show_expence_tracker_view
        )
        self._current_view.pack()

    def _show_expence_tracker_view(self):
        self._hide_current_view()

        self._current_view = ExpenceTrackerView(self._root, self._show_login_view)
        self._current_view.pack()
