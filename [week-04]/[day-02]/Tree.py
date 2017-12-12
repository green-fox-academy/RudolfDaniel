class Tree(object):
    def __init__(self, color):
        self.color = color
        self.water_level = 0.0

    def need_water(self):
        if self.water_level < 10:
            print("The "+ str(self.color) + " Tree needs water.")
        else:
            print("The "+ str(self.color) + " Tree doesnt need water.")

    def watering(self, water):
        self.water_level += water*0.4