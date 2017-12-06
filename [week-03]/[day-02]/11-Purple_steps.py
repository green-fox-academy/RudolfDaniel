from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def create_squares(a):
    for i in range(19):
        square = canvas.create_rectangle(int(1+i)*a, int(1+i)*a, int(2+i)*a, int(2+i)*a, fill='purple')

create_squares(10)

root.mainloop()