from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.
def create_line(x, y):
    line = canvas.create_line(x, y, 150, 150, fill="red")

# create_line(int(input("Give me the x coordinate of the line's starting point: ")), int(input("Give me the y coordinate of the line's starting point: ")))    
create_line(0, 0)
create_line(300, 0)
create_line(300, 300)

root.mainloop()