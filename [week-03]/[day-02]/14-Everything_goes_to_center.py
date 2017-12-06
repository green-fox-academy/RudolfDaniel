from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.
def create_line(x, y):
    for i in range(14):
        line = canvas.create_line(x, y, 150, 150, fill="red")
        x += 22
    for i in range(14):
        line = canvas.create_line(x, y, 150, 150, fill="red")
        y += 22
    for i in range(14):
        line = canvas.create_line(x, y, 150, 150, fill="red")
        x -= 22
    for i in range(14):
        line = canvas.create_line(x, y, 150, 150, fill="red")
        y -= 22
create_line(0, 0)

root.mainloop()