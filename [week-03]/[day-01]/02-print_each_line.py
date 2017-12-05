try:
    my_file = open("my_file.txt", "r")
    print(my_file.readlines())
    my_file.close()
except IOError:
    print("Unable to read file: my_file.txt")