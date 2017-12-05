def decrypt(file_name):
    try:
        my_file = open(file_name, "r")
        my_new_file = open("decoded.txt", "w")

        text = my_file.read()
        new_text = ""
        for i in range(len(text)):
# An if need to be here to filter spaces            
            new_text += chr(ord(text[i])-1)
        print(new_text)
        my_new_file.write(new_text)
        my_file.close()
        my_new_file.close()
    except IOError:
        print("Could not open the file!")

decrypt("coded_text.txt")    