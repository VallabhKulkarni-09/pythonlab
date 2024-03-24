from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Student Registration Form")
window.geometry('300x200')
window.configure(background="grey")

a = Label(window, text="First Name").grid(row=0, column=0)
b = Label(window, text="Last Name").grid(row=1, column=0)
c = Label(window, text="Email Id").grid(row=2, column=0)
d = Label(window, text="Contact Number").grid(row=3, column=0)

a1 = Entry(window)
b1 = Entry(window)
c1 = Entry(window)
d1 = Entry(window)

a1.grid(row=0, column=1)
b1.grid(row=1, column=1)
c1.grid(row=2, column=1)
d1.grid(row=3, column=1)

output_label = Label(window, text="")
output_label.grid(row=5, column=0, columnspan=2)

def clicked():
    res = "Welcome to python, " + a1.get() + " " + b1.get() + "!"
    output_label.configure(text=res)

btn = ttk.Button(window, text="Submit", command=clicked)
btn.grid(row=4, column=0, columnspan=2)

window.mainloop()
print("Registration form is created successfully...")
