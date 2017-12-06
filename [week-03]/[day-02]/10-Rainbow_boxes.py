from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def create_square(x, y):
    for i in range(7):
        square = canvas.create_rectangle(150-x/(i+2), 150-x/(i+2), 150+x/(i+2), 150+x/(i+2), fill=colors[i])

create_square(150, colors)

root.mainloop()