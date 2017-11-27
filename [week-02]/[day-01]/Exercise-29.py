nr = int(input("Type in a number "))

for i in range(0, nr, 2):
    print(" "*(nr//2) + "*"*i)
    nr -= 1
