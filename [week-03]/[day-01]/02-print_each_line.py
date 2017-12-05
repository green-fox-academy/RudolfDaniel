try:
    my_file = open("my-file.txt", "r")
    print(my_file.readlines())
except IOError:
    print("Unable to read file: my_file.txt")