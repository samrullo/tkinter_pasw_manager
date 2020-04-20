from tkinter import *
import logging


class BulkEditPasswords:
    def __init__(self, parentFrame, paswManagerObj):
        self.parentFrame = parentFrame
        self.paswManagerObj = paswManagerObj
        self.font = "Arial 15"
        self.widgetWidth = "20"
        self.VERTICAL_PADDING = 10

    def create_widgets(self):
        self.bulk_edit_text_widget = Text(self.parentFrame, font=self.font)
        self.bulk_edit_text_widget.grid(row=0, columnspan=2, sticky="ew", padx=30, pady=self.VERTICAL_PADDING)
        self.save_button = Button(self.parentFrame, text="Save", bg="coral", font=self.font, width=self.widgetWidth, command=self.save)
        self.cancel_button = Button(self.parentFrame, text="Cancel", bg="coral", font=self.font, width=self.widgetWidth, command=self.cancel)
        self.save_button.grid(row=1, column=0, pady=self.VERTICAL_PADDING)
        self.cancel_button.grid(row=1, column=1, pady=self.VERTICAL_PADDING)

    def reset(self):
        self.bulk_edit_text_widget.delete("1.0", END)
        for client, pasw in self.paswManagerObj.client_pasw_dict.items():
            self.bulk_edit_text_widget.insert(END, f"{client},{pasw}\n")

    def save(self):
        logging.info(f"save edited passwords")
        bulk_edit_text_content = self.bulk_edit_text_widget.get("1.0", END)
        bulk_edit_text_lines = bulk_edit_text_content.split("\n")
        logging.info(f"bulk edit text lines :\n{bulk_edit_text_lines}")
        client_pasw_dict = {}
        for record in bulk_edit_text_lines:
            logging.info(f"processing record {record}")
            if record:
                client, pasw = record.split(",")
                client_pasw_dict[client] = pasw
            else:
                continue
        logging.info(f"will save {len(client_pasw_dict)} passwords in bulk")
        self.paswManagerObj.save_passwords(client_pasw_dict)
        self.cancel()
        self.paswManagerObj.renderAllPasswords()

    def cancel(self):
        logging.info("cancel bulk edit passwords")
        self.parentFrame.grid_remove()
        self.paswManagerObj.frameBody.grid()
