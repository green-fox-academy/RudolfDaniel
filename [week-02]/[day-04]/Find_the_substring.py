def find_the_substring(a, b):
    if b in a:
        location = len(a) - len(b)
        return location
    else:
        return -1 


print(find_the_substring("Hello World!", "World!"))