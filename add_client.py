from tkinter import *


class AddClient:
    def __init__(self, parentFrame, paswManagerObj):
        self.parentFrame = parentFrame
        self.paswManagerObj = paswManagerObj
        self.font = "Arial 15"
        self.widgetWidth = "20"
        self.VERTICAL_PADDING = 10

    def create_widgets(self):
        self.clientLabel = Label(self.parentFrame, text="Client :", font=self.font, width=self.widgetWidth, fg="coral")
        self.clientNameEntry = Entry(self.parentFrame, font=self.font, width=self.widgetWidth)
        self.paswLabel = Label(self.parentFrame, text="Password :", font=self.font, width=self.widgetWidth, fg="coral")
        self.paswEntry = Entry(self.parentFrame, font=self.font)

        self.submitButton = Button(self.parentFrame, text="Submit", font=self.font, width=self.widgetWidth, command=self.submit)
        self.cancelButton = Button(self.parentFrame, text="Cancel", font=self.font, width=self.widgetWidth, command=self.cancel)

        self.clientLabel.grid(row=0, column=0, pady=self.VERTICAL_PADDING)
        self.clientNameEntry.grid(row=0, column=1, pady=self.VERTICAL_PADDING)
        self.paswLabel.grid(row=1, column=0, pady=self.VERTICAL_PADDING)
        self.paswEntry.grid(row=1, column=1, pady=self.VERTICAL_PADDING)
        self.submitButton.grid(row=2, column=0, pady=self.VERTICAL_PADDING)
        self.cancelButton.grid(row=2, column=1, pady=self.VERTICAL_PADDING)

    def submit(self):
        self.paswManagerObj.client_pasw_dict[self.clientNameEntry.get()] = self.paswEntry.get()
        self.paswManagerObj.save_passwords(self.paswManagerObj.client_pasw_dict)
        self.parentFrame.grid_remove()
        self.paswManagerObj.frameBody.grid()
        self.paswManagerObj.renderAllPasswords()

    def cancel(self):
        self.parentFrame.grid_remove()
        self.paswManagerObj.frameBody.grid()
