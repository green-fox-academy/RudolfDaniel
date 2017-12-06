from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def create_squares(a):
    for i in range(6):
        lenght = 0
        a *= 2 
        lenght += a
        square = canvas.create_rectangle(lenght, lenght, lenght + a, lenght + a, fill='purple')

create_squares(2)

root.mainloop()