from fleet import Fleet
from thing import Thing

fleet = Fleet()

milk = Thing("Get milk")
obstacles = Thing("Remove the obstacles")
stand = Thing("Stand up")
stand.complete()
lunch = Thing("Eat luch")
lunch.complete()

fleet.add(milk)
fleet.add(obstacles)
fleet.add(stand)
fleet.add(lunch)

print(fleet)