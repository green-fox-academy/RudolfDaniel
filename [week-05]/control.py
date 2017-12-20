from model import *
from view import *

mappa = Map()
drawing = Draw()
dezso = Hero(0, 0, 1, 0, 0, 0)
supreme_nemesis = Boss(5 * 72, 5 * 72, 0, 0, 0, 0)
skeleton_1 = Skeleton(2 * 72, 5 * 72, 0, 0, 0, 0)
skeleton_2 = Skeleton(6 * 72, 3 * 72, 0, 0, 0, 0)
skeleton_3 = Skeleton(6 * 72, 9 * 72, 0, 0, 0, 0)

for i in range(len(mappa.tiles)):
    drawing.drawer(mappa.tiles[i])

drawing.drawer(dezso)
drawing.drawer(supreme_nemesis)
drawing.drawer(skeleton_1)
drawing.drawer(skeleton_2)
drawing.drawer(skeleton_3)

def on_key_press(e):
    if e.keysym == "Up" and dezso.coordinate_y >= 72:
        if isinstance(mappa.get_tile(dezso.coordinate_x, dezso.coordinate_y - 72), Wall):
            dezso.image = dezso.image_up
        else:
            dezso.move("up")
            dezso.image = dezso.image_up
    elif e.keysym == "Down" and dezso.coordinate_y <= 640:
        if isinstance(mappa.get_tile(dezso.coordinate_x, dezso.coordinate_y + 72), Wall):
            dezso.image = dezso.image_down
        else:
            dezso.move("down")
            dezso.image = dezso.image_down
    elif e.keysym == "Right" and dezso.coordinate_x <= 640:
        if isinstance(mappa.get_tile(dezso.coordinate_x + 72, dezso.coordinate_y), Wall):
            dezso.image = dezso.image_right
        else:
            dezso.move("right")
            dezso.image = dezso.image_right
    elif e.keysym == "Left" and dezso.coordinate_x >= 72:
        if isinstance(mappa.get_tile(dezso.coordinate_x - 72, dezso.coordinate_y), Wall):
            dezso.image = dezso.image_left
        else:
            dezso.move("left")
            dezso.image = dezso.image_left
    drawing.drawer(dezso)

drawing.canvas.bind("<KeyPress>", on_key_press)

drawing.root.mainloop()