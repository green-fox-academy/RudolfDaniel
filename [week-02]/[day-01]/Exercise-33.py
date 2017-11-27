nr1 = 23

nr2 = int(input("What number is your guess? "))

if nr2 == nr1:
    print("You found the number: " + str(nr1))
elif nr2 > nr1:
    print("The stored number is lower.")
elif nr2 < nr1:
    print("The stored number is higher.")