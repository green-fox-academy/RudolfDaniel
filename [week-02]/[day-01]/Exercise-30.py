nr = int(input("Type in a number "))

for i in range(0, nr//2+1):
    print(" "*(nr-(i)) + "*"*(2*i-1))

for i in range(nr//2+1, 0, -1):
    print(" "*(nr-(i)) + "*"*(2*i-1))