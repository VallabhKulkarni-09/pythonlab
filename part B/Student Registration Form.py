from tkinter import *

window = Tk()
window.geometry('300x300')
window.title('Demo of entry, label widgets, button, checkbutton')

lab1 = Label(window, text='First Name')
lab1.grid(column=0, row=0)

t1 = Entry(window)
t1.grid(column=1, row=0)

lab2 = Label(window, text='Last Name')
lab2.grid(column=0, row=1)

t2 = Entry(window)
t2.grid(column=1, row=1)

radio = IntVar()
Radiobutton(window, text="Male", variable=radio, value=1).grid(row=2, columnspan=2, sticky=W)
Radiobutton(window, text="Female", variable=radio, value=2).grid(row=3, columnspan=2, sticky=W)

var1 = IntVar()
var2 = IntVar()
Checkbutton(window, text="KANNADA", variable=var1).grid(row=4, columnspan=2, sticky=W)
Checkbutton(window, text="HINDI", variable=var2).grid(row=5, columnspan=2, sticky=W)

def submit():
    print("First Name:", t1.get())
    print("Last Name:", t2.get())
    if radio.get() == 1:
        print("Gender: Male")
    elif radio.get() == 2:
        print("Gender: Female")
    if var1.get() == 1:
        print("Selected Language: Kannada")
    if var2.get() == 1:
        print("Selected Language: Hindi")

b1 = Button(window, text='Submit', width=10, command=submit)
b1.grid(columnspan=2, row=10)

window.mainloop()
