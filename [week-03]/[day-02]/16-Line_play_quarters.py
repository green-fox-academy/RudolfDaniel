from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def create_line(x, y):
    line = canvas.create_line(0, 150, 300, 150, fill="black")
    line = canvas.create_line(150, 0, 150, 300, fill="black")
    for i in range(15):
        line = canvas.create_line(x, 0, 150, y, fill="purple")
        y += 10
        x += 10        
    for i in range(15):
        line = canvas.create_line(0, y, x, 150, fill="green")           
        x -= 10
        y -= 10

    x = 150
    for i in range(15):
        line = canvas.create_line(x, 0, 300, y, fill="purple")
        y += 10
        x += 10
    y = 150        
    for i in range(15):
        line = canvas.create_line(150, y, x, 150, fill="green")           
        x -= 10
        y -= 10

    y = 150
    x = 0
    for i in range(15):
        line = canvas.create_line(0, y, x, 300, fill="green")
        y += 10
        x += 10
    x = 150        
    for i in range(15):
        line = canvas.create_line(150, y, x, 150, fill="purple")           
        x -= 10
        y -= 10

    x = 150
    y = 150
    for i in range(15):
        line = canvas.create_line(x, 150, 300, y, fill="purple")
        y += 10
        x += 10                
    for i in range(15):
        line = canvas.create_line(150, y, x, 300, fill="green")           
        x -= 10
        y -= 10

create_line(0, 0)

root.mainloop()