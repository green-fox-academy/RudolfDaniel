try:
    number = int(input("Type in a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("You can not divide by zero!!!")