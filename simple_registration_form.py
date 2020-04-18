from tkinter import *

window=Tk()
window.title("Simple registration form")
window.geometry("400x300")

name_lbl=Label(text="Name:",relief=RAISED)
name_lbl.grid(row=0,column=0)
name_entry=Entry(width=30)
name_entry.grid(row=0,column=1)

email_lbl=Label(text="Email:",relief=GROOVE,bd=3)
email_lbl.grid(row=1,column=0)
email_entry=Entry(width=30)
email_entry.grid(row=1,column=1)

submit_btn=Button(text="Submit",width=30,relief=RAISED)
submit_btn.grid(row=2,column=1)

window.mainloop()