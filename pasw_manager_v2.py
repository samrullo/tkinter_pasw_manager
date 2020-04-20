from tkinter import *
from password_manager import PasswordManager
from add_client import AddClient
from edit_client import EditClient
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():
    window = Tk()
    window.title("Password Manager")

    paswManagerObj = PasswordManager(window)
    window.mainloop()


if __name__ == "__main__":
    main()
