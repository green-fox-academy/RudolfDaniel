try:
    my_file = open(input("What file do you want to open: "), "r")
    lines = my_file.readlines()
    print(len(lines))
except IOError:
    print(0)