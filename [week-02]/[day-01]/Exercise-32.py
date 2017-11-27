nr = int(input("Type in a number "))

if nr != 1:
    print("%"*(nr))

    for i in range(0, nr-2):
        print("%" + " "*i + "%" + " "*(nr-3-i) + "%")

    print("%"*(nr))

elif nr == 1:
    print("%")

elif nr <= 0:
    print("Type in a positive number!")