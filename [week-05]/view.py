from tkinter import *
from control import *

root = Tk()

canvas = Canvas(root, width="720", height="720")
canvas.pack()

mappa = Map()

def drawer(thing):
    image = canvas.create_image(thing.coordinate_x + 72, thing.coordinate_y, anchor=NE, image=thing.image)

for i in range(len(mappa.tiles)):
    drawer(mappa.tiles[i])

root.mainloop()