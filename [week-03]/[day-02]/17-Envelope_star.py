from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def envelope(a, b):
    x = a
    y = b
    for i in range(15):
        line = canvas.create_line(150, y, x, 150, fill="green")
        x -= 10
        y += 10
    x = a
    y = b
    for i in range(15):
        line = canvas.create_line(150, y, x, 150, fill="green")
        x += 10
        y += 10
    x = 0
    y = 150
    for i in range(15):
        line = canvas.create_line(x, 150, 150, y, fill="green")
        x += 10
        y += 10
    x = 150
    y = 300
    for i in range(16):
        line = canvas.create_line(x, 150, 150, y, fill="green")
        x += 10
        y -= 10

envelope(150, 0)

root.mainloop()