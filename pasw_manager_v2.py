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

    paswManagerObj = PasswordManager(window, pasw_folder=r"H:\Users\samrullo\GPAS_position\secrets", pasw_file=".pasw")
    window.mainloop()


if __name__ == "__main__":
    main()
