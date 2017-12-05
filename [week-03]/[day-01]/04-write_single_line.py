try:
    my_file = open("my-file.txt", "w")
    my_file.write("Rudi")
    my_file.close()
except IOError:
    print("Unable to write file: my-file.txt")