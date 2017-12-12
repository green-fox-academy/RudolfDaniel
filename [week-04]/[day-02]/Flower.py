class Flower(object):
    def __init__(self, color):
        self.color = color
        self.water_level = 0.0

    def need_water(self):
        if self.water_level < 5:
            print("The "+ str(self.color) + " Flower needs water.")
        else:
            print("The "+ str(self.color) + " Flower doesnt need water.")

    def watering(self, water):
        self.water_level += water*0.75