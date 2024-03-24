import tkinter


window = tkinter.Tk() 
window.geometry("400x400")
    
c = tkinter.Canvas(window, bg="pink", height="200")
c.create_oval(10, 1, 80, 80, fill='green', width=2)
c.create_oval(110, 10, 210, 80, fill='green', width=2)
c.create_rectangle(230, 10, 290, 60, fill='blue', width=2)
points = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200]
c.create_polygon(points, fill='red', width=2)
c.create_line(300, 50, 350, 150, fill='red', width=2)
    
c.pack()
window.mainloop()


