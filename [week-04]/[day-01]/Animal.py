class Animal(object):
    hunger = 50
    thirst = 50
    
    def eat():
        hunger -= 1
    
    def drink():
        thirst -= 1

    def play():
        hunger += 1
        thirst += 1