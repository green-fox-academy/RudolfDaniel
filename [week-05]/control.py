from model import *
from view import *

mappa = Map()
drawing = Draw()
dezso = Hero(0, 0, 1, 20, 10, 10)

for i in range(len(mappa.tiles)):
    drawing.drawer(mappa.tiles[i])
"""
drawing.drawer(dezso)
dezso.move("right")
drawing.drawer(dezso)
"""
drawing.drawer(dezso)
def on_key_press(e):
    print(e)
    if e.keysym == "Up":
        dezso.move("up")
    elif e.keysym == "Down":
        dezso.move("down")
    elif e.keysym == "Right":
        dezso.move("right")
    elif e.keysym == "Left":
        dezso.move("left")
    drawing.drawer(dezso)

drawing.canvas.bind("<KeyPress>", on_key_press)

drawing.root.mainloop()