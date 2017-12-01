def is_anagram(a, b):
    first_string = sorted(a)
    second_string = sorted(b)
    if first_string == second_string:
        return print(True)
    else:
        return print(False)

is_anagram((input("Type in a word: ")), (input("Type in the next word: ")))