nr = int(input("Type in a number "))

for i in range(0, nr+1):
    print(" "*(nr-(i)) + "*"*(2*i-1))