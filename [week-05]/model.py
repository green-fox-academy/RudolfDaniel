from random import *

class Tile(object):
    def __init__(self, coordinate_x, coordinate_y):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.image = "floor.png"
            
class Wall(Tile):
    def __init__(self, coordinate_x, coordinate_y):
        super().__init__(coordinate_x, coordinate_y)
        self.image = "wall.png"

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
        self.image_up = "hero-up.png"
        self.image_right = "hero-right.png"
        self.image_down = "hero-down.png"
        self.image_left = "hero-left.png"
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