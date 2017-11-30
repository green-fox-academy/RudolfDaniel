def find_substr(a, b):
    output = [-1]
    for i in range(len(b)):
        if a in b[i]:
            output = [i]
    return output

list_of_strings = ["this", "is", "what", "I'm", "searching", "in"]
txt = "ching"

print(find_substr(txt, list_of_strings))