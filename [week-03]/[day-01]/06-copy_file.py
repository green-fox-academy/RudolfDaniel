def write_file(original_file, copied_file):
    try:
        my_file = open(original_file, "r")
        my_new_file = open(copied_file, "w")
        text = my_file.read()
        my_new_file.write(text)

        my_file.close()
        my_new_file.close()
        return True
    except:
        return False

print(write_file("original.txt", "copy.txt"))