from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
top = canvas.create_line(20, 20, 280, 20, fill='light sea green')
right = canvas.create_line(280, 20, 280, 280, fill='lime green')
bottom = canvas.create_line(280, 280, 20, 280, fill='olive drab')
left = canvas.create_line(20, 280, 20, 20, fill='gold')

root.mainloop()