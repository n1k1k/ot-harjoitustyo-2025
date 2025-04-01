from tkinter import Tk
from ui.ui import UI
from initialise_database import initialise_database


def main():
    window = Tk()
    window.title("Expence Tracker")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
