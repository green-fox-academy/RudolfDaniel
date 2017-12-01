def search_palindrome(a):
    this_is_list = [char for char in a]
    print(this_is_list)
    output = ["lalala"]
    for i in range(0, len(this_is_list)):
        while this_is_list[i-1] == this_is_list[i+1]:
            output += ["blabla"]
    print(output)

search_palindrome(input("Type in a text: "))