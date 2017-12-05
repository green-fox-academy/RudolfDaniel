def write_file(path, word, number):
    try:
        my_file = open(path, "w")
        my_file.write(((word) + "\n") * int(number))
        my_file.close()
    except:
        print("ERROR!")

write_file(input("Type in path: "), input("Typye in a word: "), input("How many lines you want: "))