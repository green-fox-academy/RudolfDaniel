from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def create_line(x, y):
    for i in range(14):
        line = canvas.create_line(x, 0, 300, y, fill="purple")
        y += 22
        x += 22
    for i in range(14):
        line = canvas.create_line(0, y, x, 300, fill="green")
        x -= 22
        y -= 22

create_line(0, 0)

root.mainloop()