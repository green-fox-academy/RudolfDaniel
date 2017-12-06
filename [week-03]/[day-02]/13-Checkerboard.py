from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.
def checkerboard(a):
    for i in range(10):
        y = 0
        y += i*30
        if i%2 == 0:
            for i in range(5):
                x = 0
                x += i*60
                square = canvas.create_rectangle(x, y, x+a, y+a, fill='black')
                square = canvas.create_rectangle(x+a, y, x+(2*a), y+a, fill='white')
        else:
            for i in range(5):
                x = 0
                x += i*60
                square = canvas.create_rectangle(x+a, y, x+(2*a), y+a, fill='black')
                square = canvas.create_rectangle(x, y, x+a, y+a, fill='white')

checkerboard(31)

root.mainloop()