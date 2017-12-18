from model import *

class Map(object):
    def __init__(self):
        self.floor = Tile(0, 0)
        self.level_one = []
        for j in range(10):
            for i in range(10):
                self.level_one.append(Tile(i * 72, j * 72))