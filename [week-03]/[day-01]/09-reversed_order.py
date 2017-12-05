def decrypt(file_name):
    try:
        my_file = open(file_name, "r")
        my_new_file = open("corrected_order.txt", "w")

        text = my_file.readlines()
        new_text = text[::-1]
        latest_text = "".join(new_text)

        my_new_file.write(latest_text)
        my_file.close()
        my_new_file.close()
    except IOError:
        print("Could not open the file!")

decrypt("reversed_order.txt")