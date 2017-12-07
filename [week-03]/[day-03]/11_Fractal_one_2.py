from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='600', bg="yellow")
canvas.pack()

x = 300
y = 300

def fractal(base, power):
    if base == 0 or power == 0:
        first_vertical = canvas.create_line(200, 0, 200, 600)
        second_vertical = canvas.create_line(400, 0, 400, 600)
        first_horizontal = canvas.create_line(0, 200, 600, 200)
        second_horizontal = canvas.create_line(0, 400, 600, 400)    
        return 1
    else:
        first_vertical = canvas.create_line(300-(600/power)/3, 0, 300-(600/power)/3, 600)
        second_vertical = canvas.create_line(400, 0, 400, 600)
        first_horizontal = canvas.create_line(0, 200, 600, 200)
        second_horizontal = canvas.create_line(0, 400, 600, 400)
        lalala = 0 
        return base * fractal(base, power-1)

print(fractal(5, 4))

root.mainloop()