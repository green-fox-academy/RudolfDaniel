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
    def __init__(self, coordinate_x, coordinate_y):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.level = 1

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
    def __init__(self, coordinate_x, coordinate_y):
        super().__init__(coordinate_x, coordinate_y)
        self.image = "hero-down.png"
        self.image_up = "hero-up.png"
        self.image_right = "hero-right.png"
        self.image_left = "hero-left.png"
        self.image_down = "hero-down.png"
        self.hp = 20 + 3 * randint(1, 6)
        self.actual_hp = self.hp
        self.dp = 2 * randint(1, 6)
        self.sp = 5 + randint(1, 6)
    def level_up(self):
        self.level += 1
        self.hp += randint(1, 6)
        self.dp += randint(1, 6)
        self.sp += randint(1, 6)

class Skeleton(Character):
    def __init__(self, coordinate_x, coordinate_y):
        super().__init__(coordinate_x, coordinate_y)
        self.if_has_the_key = False
        self.image = "skeleton.png"
        self.hp = 2 * self.level * randint(1, 6)
        self.actual_hp = self.hp
        self.dp = self.level / 2 * randint(1, 6)
        self.sp = self.level + randint(1, 6)
    def level_up(self):
        self.level += 1

class Boss(Character):
    def __init__(self, coordinate_x, coordinate_y):
        super().__init__(coordinate_x, coordinate_y)
        self.if_has_the_key = False
        self.image = "boss.png"
        self.hp = 2 * self.level * randint(1, 6) + randint(1, 6)
        self.actual_hp = self.hp
        self.dp = self.level / 2 * randint(1, 6) + randint(1, 6)
        self.sp = self.level + randint(1, 6) + self.level
    def level_up(self):
        self.level += 1

class Map(object):
    def __init__(self):
        self.floor = Tile(0, 0)
        self.wall = Wall(0, 0)
        self.tiles = []
        for j in range(10):
            for i in range(10):
                self.tiles.append(Tile(i * 72, j * 72))

        for i in range(3, 6, 2):
            self.tiles[i] = Wall(i * 72, 0 * 72)

        for i in range(13, 18, 2):
            self.tiles[i] = Wall((i-10) * 72, 1 * 72)
        self.tiles[18] = Wall(8 * 72, 1 * 72)

        for i in range(21, 24):
            self.tiles[i] = Wall((i-20) * 72, 2 * 72)
        for i in range(25, 28, 2):
            self.tiles[i] = Wall((i-20) * 72, 2 * 72)
        self.tiles[28] = Wall(8 * 72, 2 * 72)

        self.tiles[35] = Wall(5 * 72, 3 * 72)

        for i in range(40, 44):
            self.tiles[i] = Wall((i-40) * 72, 4 * 72)
        for i in range(45, 49):
            self.tiles[i] = Wall((i-40) * 72, 4 * 72)

        for i in range(51, 54, 2):
            self.tiles[i] = Wall((i-50) * 72, 5 * 72)
        self.tiles[58] = Wall(8 * 72, 5 * 72)

        for i in range(61, 66, 2):
            self.tiles[i] = Wall((i-60) * 72, 6 * 72)
        for i in range(66, 69, 2):
            self.tiles[i] = Wall((i-60) * 72, 6 * 72)

        for i in range(75, 77):
            self.tiles[i] = Wall((i-70) * 72, 7 * 72)
        self.tiles[78] = Wall(8 * 72, 7 * 72)

        for i in range(81, 84):
            self.tiles[i] = Wall((i-80) * 72, 8 * 72)
        self.tiles[88] = Wall(8 * 72, 8 * 72)

        for i in range(91, 96, 2):
            self.tiles[i] = Wall((i-90) * 72, 9 * 72)
    
    def get_tile(self, coordinate_x, coordinate_y):
        for i in range(len(self.tiles)):
            if coordinate_x == self.tiles[i].coordinate_x and coordinate_y == self.tiles[i].coordinate_y:
                return self.tiles[i]