from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def connective(a):
    canvas.create_polygon(a, outline="green", fill="red", width=3)

box = [[10, 10], [290,  10], [290, 290], [10, 290]]
second = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

connective(box)
connective(second)

root.mainloop()