import random

def guess(a):
    lives = 5
    origin_nr = random.randint(0, a) 
    while lives > 0:
        print("I've the number between 0 and " + str(a) + ". You have " + str(lives) + " lives.")
        guess = int(input("Guess my number: "))
        if guess < origin_nr:
            lives -= 1
            print("Too low. You have " + str(lives) + " left.")
        elif guess > origin_nr:
            lives -= 1
            print("Too high. You have " + str(lives) + " left.")
        elif guess == origin_nr:
            return print("Congratulations. You won!")
    
guess(int(input("Type in the max of the interval: ")))