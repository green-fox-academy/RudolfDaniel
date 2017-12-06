from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
cyan_rectangle = canvas.create_rectangle(20, 20, 50, 50, fill='cyan')
magenta_rectangle = canvas.create_rectangle(240, 20, 280, 60, fill='magenta')
yellow_rectangle = canvas.create_rectangle(230, 230, 280, 280, fill='yellow')
black_rectangle = canvas.create_rectangle(20, 220, 80, 280, fill='black')

root.mainloop()