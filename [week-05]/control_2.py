from model_2 import *
from view_2 import *
from random import *

mappa = Map()
drawing = Draw()
dezso = Hero(0, 0)
supreme_nemesis = Boss(5 * 72, 5 * 72)
skeleton_1 = Skeleton(2 * 72, 5 * 72)
skeleton_2 = Skeleton(6 * 72, 3 * 72)
skeleton_3 = Skeleton(6 * 72, 9 * 72)
list_of_monsters = []
list_of_skeletons = []
list_of_monsters.append(skeleton_1)
list_of_monsters.append(skeleton_2)
list_of_monsters.append(skeleton_3)
list_of_monsters.append(supreme_nemesis)
list_of_skeletons.append(skeleton_1)
list_of_skeletons.append(skeleton_2)
list_of_skeletons.append(skeleton_3)

counter = 0

def label():
        drawing.canvas.create_rectangle(0, 720, 720, 750, fill="white")
        drawing.canvas.create_text(360, 735, fill="black", font=30, text="Hero (Level " + str(dezso.level) + ") HP: " + str(dezso.actual_hp) + "/" + str(dezso.hp) + " | DP: " + str(dezso.dp) + " | SP: " + str(dezso.sp))

def give_the_key_to_a_random_skeleton():
    which = randint(0, 2)
    list_of_skeletons[which].if_has_the_key = True

give_the_key_to_a_random_skeleton()

def drawing_refresh():
    for i in range(len(mappa.tiles)):
        drawing.drawer(mappa.tiles[i])
    if dezso.actual_hp > 0:
        drawing.drawer(dezso)
    if supreme_nemesis.actual_hp > 0:
        drawing.drawer(supreme_nemesis)
    if skeleton_1.actual_hp > 0:
        drawing.drawer(skeleton_1)
    if skeleton_2.actual_hp > 0:
        drawing.drawer(skeleton_2)
    if skeleton_3.actual_hp > 0:
        drawing.drawer(skeleton_3)
    label()

def fight(hero, monster):
    while hero.actual_hp > 0 and monster.actual_hp > 0:
        strike_value = (hero.sp + randint(2, 12)) - monster.dp
        if strike_value > 0:
            monster.actual_hp -= strike_value
            print("Strike value to monster: " + str(strike_value))
            print("Monster actual hp: " + str(monster.actual_hp))
            if monster.actual_hp <= 0:
                dezso.level_up()
                if monster.if_has_the_key == True:
                    return print("You reached next level!")
        strike_value = monster.sp + randint(2, 12) - hero.dp
        if strike_value > 0:
            hero.actual_hp -= strike_value
            print("Strike value to hero: " + str(strike_value))
            print("Hero actual hp: " + str(hero.actual_hp))
            if hero.actual_hp <= 0:
                return print("Game over!")

drawing_refresh()

def monster_mover(monster, direction):
    if direction == "Up" and monster.coordinate_y >= 72:
        if isinstance(mappa.get_tile(monster.coordinate_x, monster.coordinate_y - 72), Wall):
            return None
        else:
            monster.move("up")
    elif direction == "Down" and monster.coordinate_y <= 640:
        if isinstance(mappa.get_tile(monster.coordinate_x, monster.coordinate_y + 72), Wall):
            return None
        else:
            monster.move("down")
    elif direction == "Right" and monster.coordinate_x <= 640:
        if isinstance(mappa.get_tile(monster.coordinate_x + 72, monster.coordinate_y), Wall):
            return None
        else:
            monster.move("right")
    elif direction == "Left" and monster.coordinate_x >= 72:
        if isinstance(mappa.get_tile(monster.coordinate_x - 72, monster.coordinate_y), Wall):
            return None
        else:
            monster.move("left")

def on_key_press(e):
    global counter
    if e.keysym == "Up" and dezso.coordinate_y >= 72:
        counter += 1
        if isinstance(mappa.get_tile(dezso.coordinate_x, dezso.coordinate_y - 72), Wall):
            dezso.image = dezso.image_up
        else:
            dezso.move("up")
            dezso.image = dezso.image_up
    elif e.keysym == "Down" and dezso.coordinate_y <= 640:
        counter += 1
        if isinstance(mappa.get_tile(dezso.coordinate_x, dezso.coordinate_y + 72), Wall):
            dezso.image = dezso.image_down
        else:
            dezso.move("down")
            dezso.image = dezso.image_down
    elif e.keysym == "Right" and dezso.coordinate_x <= 640:
        counter += 1
        if isinstance(mappa.get_tile(dezso.coordinate_x + 72, dezso.coordinate_y), Wall):
            dezso.image = dezso.image_right
        else:
            dezso.move("right")
            dezso.image = dezso.image_right
    elif e.keysym == "Left" and dezso.coordinate_x >= 72:
        counter += 1
        if isinstance(mappa.get_tile(dezso.coordinate_x - 72, dezso.coordinate_y), Wall):
            dezso.image = dezso.image_left
        else:
            dezso.move("left")
            dezso.image = dezso.image_left

    elif e.keycode == 32:
        for i in range(len(list_of_monsters)):
            if dezso.coordinate_x == list_of_monsters[i].coordinate_x and dezso.coordinate_y == list_of_monsters[i].coordinate_y:
                fight(dezso, list_of_monsters[i])

    if counter % 2 == 0:
        list_of_directions = ["Up", "Down", "Right", "Left"]
        random_index = randrange(0, len(list_of_directions))
        monster_mover(skeleton_1, list_of_directions[random_index])
        random_index = randrange(0, len(list_of_directions))
        monster_mover(skeleton_2, list_of_directions[random_index])
        random_index = randrange(0, len(list_of_directions))
        monster_mover(skeleton_3, list_of_directions[random_index])
        random_index = randrange(0, len(list_of_directions))
        monster_mover(supreme_nemesis, list_of_directions[random_index])
    drawing_refresh()

drawing.canvas.bind("<KeyPress>", on_key_press)

drawing.root.mainloop()