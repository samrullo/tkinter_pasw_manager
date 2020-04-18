from tkinter import *

window=Tk()
window.geometry("400x400")

button1=Button(text="Push Me")
button1.place(x=200,y=300)


label=Label(text="Bir defe podmetay dosvidaniya.¥¥n"
                 "Bir defe podmetay dosvidaniya.¥n"
                 "Bir defe podmetay dosvidaniya.¥n"
                 "Bir defe podmetay dosvidaniya.")
label.place(x=25,y=150)


entry=Entry(text="")
entry.place(x=150,y=50)


window.mainloop()