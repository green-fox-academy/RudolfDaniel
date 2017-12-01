sentence = input("Type in a sentence: ")

def create_palindrome(a):
    palindrom = sentence + ""
    for i in range(-1, -(len(a)+1), -1):
        palindrom += a[i]
    return palindrom

print(create_palindrome(sentence))