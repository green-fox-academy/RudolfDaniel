nr1 = int(input("Type in number one: "))
nr2 = int(input("Type in number two: "))

if nr2 <= nr1:
    print("The second number should be bigger")
elif nr2 > nr1:
    for i in range(nr1, nr2):
        print(i)