from Flower import Flower
from Tree import Tree

yellow_flower = Flower("yellow")
blue_flower = Flower("blue")
purple_tree = Tree("purple")
orange_tree = Tree("orange")

garden = [yellow_flower, blue_flower, purple_tree, orange_tree]

yellow_flower.need_water()
blue_flower.need_water()
purple_tree.need_water()
orange_tree.need_water()

def watering_all(amount):
    needed_water = []
    for i in range(0, 2):
        if garden[i].water_level < 5:
            needed_water.append(garden[i])      
    for i in range(2, 4):
        if garden[i].water_level < 10:
            needed_water.append(garden[i])        
    for i in range(len(needed_water)):
        needed_water[i].watering(amount/len(needed_water))
    for i in range(len(garden)):
        garden[i].need_water()

print("\n" + "Watering with 40")
watering_all(40)
print("\n" + "Watering with 70")
watering_all(70)