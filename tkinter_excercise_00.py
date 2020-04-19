from tkinter import *
import random

passwords={f"Client{numb}":f"Password{numb}" for numb in range(10)}

window=Tk()
window.title("Password Manager")
window.geometry("800x500")

frameHeader=Frame(window,pady=20)
frameHeader.pack()

searchLabel=Label(frameHeader, text="Search:",font="Arial 15")
searchLabel.grid(row=0,column=0)

searchBox=Entry(frameHeader, width=60,font="Arial 15")
searchBox.grid(row=0,column=1)

frameBody=Frame(window, pady=20)
frameBody.pack()

row_counter=0
for client,password in passwords.items():
    client_lbl=Label(frameBody, text=client, font="Arial 15", width=20, justify=LEFT, fg="dodger blue", relief=RAISED)
    client_lbl.grid(row=row_counter,column=0)

    pasw_lbl=Label(frameBody, text=password, font="Arial 15", width=20, justify=LEFT, fg="VioletRed1", bd=1)
    pasw_lbl.grid(row=row_counter,column=1)

    btn=Button(frameBody, text="Edit", bg="green", width=20, activebackground="green")
    btn.grid(row=row_counter,column=2)

    row_counter+=1

window.mainloop()