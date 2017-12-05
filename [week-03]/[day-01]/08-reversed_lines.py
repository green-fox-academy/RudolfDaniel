def decrypt(file_name):
    try:
        my_file = open(file_name, "r")
        my_new_file = open("reversed.txt", "w")

        text = my_file.read()
        new_text = ""
        for i in reversed(range(len(text))):
            new_text += text[i]
        my_new_file.write(new_text)
        my_file.close()
        my_new_file.close()
    except IOError:
        print("Could not open the file!")

decrypt("reversed_text.txt")