from tkinter import *
import logging
import os
import pickle
from add_client import AddClient
from edit_client import EditClient
from bulk_edit import BulkEditPasswords
from tkinter.filedialog import askopenfile


class PasswordManager:
    def __init__(self, window, pasw_folder=r"H:\Users\samrullo\GPAS_position\secrets", pasw_file=".pasw"):
        self.window = window

        # visual related
        self.VERTICAL_PADDING = 10
        self.font = "Arial 15"
        self.foreground_color = "coral"
        self.button_bg_color = ""

        self.frameNewClient = Frame(self.window)
        self.addClientObj = AddClient(self.frameNewClient, self)
        self.addClientObj.create_widgets()

        self.frameEditClient = Frame(self.window)
        self.editClientObj = EditClient(self.frameEditClient, self)
        self.editClientObj.create_widgets()

        self.frameBulkEdit = Frame(self.window)
        self.bulkEditObj = BulkEditPasswords(self.frameBulkEdit, self)
        self.bulkEditObj.create_widgets()

        self.make_menu_bar()

        self.frameBody = Frame(self.window)
        self.frameBody.grid()
        self.pasw_file = os.path.join(pasw_folder, pasw_file)
        self.client_pasw_dict = self.get_client_pasw_dict()
        self.make_searchbox_header()
        self.make_list_box()
        self.renderAllPasswords()
        self.make_add_edit_buttons()

    def make_searchbox_header(self):
        self.frameHeader = Frame(self.frameBody, pady=20)
        self.frameHeader.grid(pady=10)

        self.searchLabel = Label(self.frameHeader, text="Search:", font="Arial 15", width=10)
        self.searchLabel.grid(row=0, column=0)

        self.searchBox = Entry(self.frameHeader, width=60, font="Arial 15")
        self.searchBox.grid(row=0, column=1)
        self.searchBox.bind("<Key>", self.search_passwords)

    def make_list_box(self):
        self.listBox = Listbox(self.frameBody, font="Arial 15", width=60, justify=CENTER)
        self.listBox.grid(pady=10)

    def get_client_pasw_dict(self):
        client_pasw_dict = self.load_passwords()
        return client_pasw_dict

    def make_add_edit_buttons(self):
        self.addClientButton = Button(self.frameBody, text="Add New Client", font="Arial 15", width=40, padx=10, pady=10,
                                      bg="coral", activebackground="green", command=self.open_new_client_frame)
        self.addClientButton.grid(pady=10)

        self.editClientButton = Button(self.frameBody, text="Edit Client", font="Arial 15", width=40, padx=10, pady=10,
                                       bg="coral", activebackground="green", command=self.open_edit_client_pasw)
        self.editClientButton.grid(pady=10)

    def make_menu_bar(self):
        menubar = Menu(self.window)
        file_menu = Menu(menubar, tearoff=0)
        # file_menu.add_command(label="Choose Password File", command=self.choose_pasw_file)
        file_menu.add_command(label="Bulk Edit Passwords", command=self.bulk_edit_passwords)
        # file_menu.add_separator()
        # file_menu.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.window.config(menu=menubar)

    def choose_pasw_file(self):
        pasw_filepath = askopenfile(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        logging.info(f"chosen password file path : {pasw_filepath}")
        self.pasw_file = pasw_filepath

    def bulk_edit_passwords(self):
        logging.info(f"will open bulk edit frame")
        self.frameBody.grid_remove()
        self.frameBulkEdit.grid()
        self.bulkEditObj.reset()

    def load_passwords(self):
        if os.path.exists(self.pasw_file):
            with open(self.pasw_file, "rb") as fh:
                client_passwords_dict = pickle.load(fh)
                logging.info(f"finished loading {len(client_passwords_dict)} passwords from {self.pasw_file}")
                return client_passwords_dict
        else:
            logging.info(f"{self.pasw_file} doesn't exist so will return empty dictionary")
            return {}

    def save_passwords(self, client_pasw_dict):
        with open(self.pasw_file, "wb") as fh:
            pickle.dump(client_pasw_dict, fh)
            logging.info(f"finished dumping {len(client_pasw_dict)} client passwords")
        self.client_pasw_dict = self.load_passwords()
        logging.info(f"also finished loading newly saved passwords")

    def renderAllPasswords(self):
        logging.info("will render all passwords")
        self.listBox.delete(0, END)
        counter = 0
        for client, password in self.client_pasw_dict.items():
            self.listBox.insert(counter, f"{client} : {password}")
            counter += 1

    def search_passwords(self, event):
        logging.info(f"search_passwords is called with event {event}")
        logging.info(f"entered key symbol is {event.keysym}")
        search_text = self.searchBox.get()
        if event.keysym != 'BackSpace':
            search_text += event.char
        else:
            logging.info(f"BackSpace was pressed : {event.keysym}")
            search_text = search_text[:-1]
        logging.info(f"current searchBox text : {search_text}")
        self.listBox.delete(0, END)
        new_client_pasw_dict = {}
        counter = 0
        for client, pasw in self.client_pasw_dict.items():
            if re.search(search_text.lower(), client.lower()):
                new_client_pasw_dict[client] = pasw
                self.listBox.insert(counter, f"{client} : {pasw}")
            if search_text == "":
                logging.info("search box is empty so will render all passwords")
                self.renderAllPasswords()

    def open_new_client_frame(self):
        logging.info(f"will add a new client")
        self.frameBody.grid_remove()

        ## calculate horizontal  and vertical paddings
        paddings = self.calc_paddings()
        self.frameNewClient.grid(row=0, column=0, padx=paddings[0], pady=paddings[1], sticky="nsew")
        self.addClientObj.paswEntry.delete(0, END)
        self.addClientObj.clientNameEntry.delete(0, END)

    def open_edit_client_pasw(self):
        client_pasw_lines = self.listBox.get(0, END)
        if len(client_pasw_lines) > 0:
            client_pasw_line = client_pasw_lines[0]
            client, pasw = client_pasw_line.split(":")
            client = client.strip()
            pasw = pasw.strip()
            logging.info(f"will edit {client},{pasw}")
            self.frameBody.grid_remove()
            self.editClientObj.set_client_pasw_to_edit(client, pasw)
            paddings = self.calc_paddings()
            self.frameEditClient.grid(padx=paddings[0], pady=paddings[1])

    def calc_paddings(self):
        ## calculate horizontal  and vertical paddings
        pad_horizontal = self.window.winfo_width() / 4
        logging.info(f"calculated horizontal padding : {pad_horizontal}")

        pad_vertical = self.window.winfo_height() / 4
        logging.info(f"calculated vertical padding : {pad_vertical}")
        return (pad_horizontal, pad_vertical)
