from tkinter import ttk, constants


class LoginView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialise()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialise(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Test!")
        label.grid(row=0, column=0)
