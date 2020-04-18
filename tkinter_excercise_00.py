from tkinter import *
import random

passwords={f"Client{numb}":f"Password{numb}" for numb in range(10)}

window=Tk()
window.title("Password Manager")
window.geometry("500x500")

row_counter=0
for client,password in passwords.items():
    client_lbl=Label(text=client,font="Arial 15",width=20,justify=LEFT,fg="dodger blue")
    client_lbl.grid(row=row_counter,column=0)

    pasw_lbl=Label(text=password,font="Arial 15",width=20,justify=LEFT,fg="VioletRed1")
    pasw_lbl.grid(row=row_counter,column=1)

    btn=Button(text="Edit",width=10,background="coral",relief=RAISED)
    btn.grid(row=row_counter,column=2)

    row_counter+=1

window.mainloop()