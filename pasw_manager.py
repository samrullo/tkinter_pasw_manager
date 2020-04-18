from tkinter import *

width=500
height=700
window=Tk()
window.title("Aladdin Pasw Manager")
window.geometry(f"{width}x{height}")

# this is how you create a label widget
label1=Label(text="Welcome to Aladdin Password Manager!")
label1.grid()

# this is how you create a button widget
button1=Button(text="Push Me",width=50,height=20)
button1.grid()

# entry widget
entry1=Entry(width=10)
entry1.grid()

# Text widget
text1=Text(height=10,width=40)
text1.grid()

window.mainloop()