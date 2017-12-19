from tkinter import *
from random import *

class Tile(object):
    def __init__(self, coordinate_x, coordinate_y):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.image = PhotoImage(file = "floor.png")
            
class Wall(object):
    def __init__(self, coordinate_x, coordinate_y):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.image = PhotoImage(file = "wall.png")

class Character(object):
    def __init__(self, coordinate_x, coordinate_y, level, hp, dp, sp):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.level = level
        self.hp = hp
        self.dp = dp
        self.sp = sp

class Hero(Character):
    def __init__(self, coordinate_x, coordinate_y, level, hp, dp, sp):
        super().__init__(coordinate_x, coordinate_y, level, hp, dp, sp)
        self.image_up = PhotoImage(file = "hero-up.png")
        self.image_right = PhotoImage(file = "hero-right.png")
        self.image_down = PhotoImage(file = "hero-down.png")
        self.image_left = PhotoImage(file = "hero-left.png")
        self.image = self.image_down
        self.hp = 20 + 3 * randint(1, 6)
        self.dp = dp
        self.sp = sp

class Skeleton(Character):
    def __init__(self, coordinate_x, coordinate_y, level, hp, dp, sp):
        super().__init__(coordinate_x, coordinate_y, level, hp, dp, sp)
        self.image = PhotoImage(file = "skeleton.png")

class Boss(Character):
    def __init__(self, coordinate_x, coordinate_y, level, hp, dp, sp):
        super().__init__(coordinate_x, coordinate_y, level, hp, dp, sp)
        self.image = PhotoImage(file = "boss.png")
