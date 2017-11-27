nr1 = 23

nr2 = int(input("What number is your guess? "))

while nr2 != nr1:
    if nr2 > nr1:
        print("The stored number is lower.")
        nr2 = int(input("Guess again: "))
    elif nr2 < nr1:
        print("The stored number is higher.")
        nr2 = int(input("Guess again: "))
print("You find the number: " + str(nr1))