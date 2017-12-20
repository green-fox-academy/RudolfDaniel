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
    def move(self, direction):
        self.direction = direction
        if self.direction == "right":
            self.coordinate_x += 72
        elif self.direction == "left":
            self.coordinate_x -= 72
        elif self.direction == "up":
            self.coordinate_y -= 72
        elif self.direction == "down":
            self.coordinate_y += 72

class Hero(Character):
    def __init__(self, coordinate_x, coordinate_y, level, hp, dp, sp):
        super().__init__(coordinate_x, coordinate_y, level, hp, dp, sp)
        self.image = "hero-down.png"
        self.image_up = "hero-up.png"
        self.image_right = "hero-right.png"
        self.image_left = "hero-left.png"
        self.image_down = "hero-down.png"
        self.hp = 20 + 3 * randint(1, 6)
        self.dp = 2 * randint(1, 6)
        self.sp = 5 + randint(1, 6)

class Skeleton(Character):
    def __init__(self, coordinate_x, coordinate_y, level, hp, dp, sp):
        super().__init__(coordinate_x, coordinate_y, level, hp, dp, sp)
        self.image = PhotoImage(file = "skeleton.png")
        self.hp = 2 * self.level * randint(1, 6)
        self.dp = self.level / 2 * randint(1, 6)
        self.sp = self.level + randint(1, 6)


class Boss(Character):
    def __init__(self, coordinate_x, coordinate_y, level, hp, dp, sp):
        super().__init__(coordinate_x, coordinate_y, level, hp, dp, sp)
        self.image = PhotoImage(file = "boss.png")
        self.hp = 2 * self.level * randint(1, 6) + randint(1, 6)
        self.dp = self.level / 2 * randint(1, 6) + randint(1, 6)
        self.sp = self.level + randint(1, 6) + self.level

class Map(object):
    def __init__(self):
        self.floor = Tile(0, 0)
        self.wall = Wall(0, 0)
        self.tiles = []
        for j in range(10):
            for i in range(10):
                self.tiles.append(Tile(i * 72, j * 72))
        self.tiles[3] = Wall(3 * 72, 0 * 72)
        self.tiles[5] = Wall(5 * 72, 0 * 72)

        self.tiles[13] = Wall(3 * 72, 1 * 72)
        self.tiles[15] = Wall(5 * 72, 1 * 72)
        self.tiles[17] = Wall(7 * 72, 1 * 72)
        self.tiles[18] = Wall(8 * 72, 1 * 72)

        self.tiles[21] = Wall(1 * 72, 2 * 72)
        self.tiles[22] = Wall(2 * 72, 2 * 72)
        self.tiles[23] = Wall(3 * 72, 2 * 72)
        self.tiles[25] = Wall(5 * 72, 2 * 72)
        self.tiles[27] = Wall(7 * 72, 2 * 72)
        self.tiles[28] = Wall(8 * 72, 2 * 72)

        self.tiles[35] = Wall(5 * 72, 3 * 72)

        self.tiles[40] = Wall(0 * 72, 4 * 72)
        self.tiles[41] = Wall(1 * 72, 4 * 72)
        self.tiles[42] = Wall(2 * 72, 4 * 72)
        self.tiles[43] = Wall(3 * 72, 4 * 72)
        self.tiles[45] = Wall(5 * 72, 4 * 72)
        self.tiles[46] = Wall(6 * 72, 4 * 72)
        self.tiles[47] = Wall(7 * 72, 4 * 72)
        self.tiles[48] = Wall(8 * 72, 4 * 72)

        self.tiles[51] = Wall(1 * 72, 5 * 72)
        self.tiles[53] = Wall(3 * 72, 5 * 72)
        self.tiles[58] = Wall(8 * 72, 5 * 72)

        self.tiles[61] = Wall(1 * 72, 6 * 72)
        self.tiles[63] = Wall(3 * 72, 6 * 72)
        self.tiles[65] = Wall(5 * 72, 6 * 72)
        self.tiles[66] = Wall(6 * 72, 6 * 72)
        self.tiles[68] = Wall(8 * 72, 6 * 72)

        self.tiles[75] = Wall(5 * 72, 7 * 72)
        self.tiles[76] = Wall(6 * 72, 7 * 72)
        self.tiles[78] = Wall(8 * 72, 7 * 72)

        self.tiles[81] = Wall(1 * 72, 8 * 72)
        self.tiles[82] = Wall(2 * 72, 8 * 72)
        self.tiles[83] = Wall(3 * 72, 8 * 72)
        self.tiles[88] = Wall(8 * 72, 8 * 72)

        self.tiles[91] = Wall(1 * 72, 9 * 72)
        self.tiles[93] = Wall(3 * 72, 9 * 72)
        self.tiles[95] = Wall(5 * 72, 9 * 72)