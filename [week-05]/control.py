from model import *
from view import *

mappa = Map()
drawing = Draw()
dezso = Hero(0, 0, 1, 20, 10, 10)

for i in range(len(mappa.tiles)):
    drawing.drawer(mappa.tiles[i])

drawing.drawer(dezso)
def on_key_press(e):
    if e.keysym == "Up" and dezso.coordinate_y >= 72:
        dezso.move("up")
    elif e.keysym == "Down" and dezso.coordinate_y <= 640:
        dezso.move("down")
    elif e.keysym == "Right" and dezso.coordinate_x <= 640:
        dezso.move("right")
    elif e.keysym == "Left" and dezso.coordinate_x >= 72:
        dezso.move("left")
    drawing.drawer(dezso)

drawing.canvas.bind("<KeyPress>", on_key_press)

drawing.root.mainloop()