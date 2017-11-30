def find_int(a, b):
    output = []
    for i in range(len(a)):
        if str(b) in str(a[i]):
            output.append(i)
    return output


input = [1, 11, 34, 52, 61]
nr = 1

print(find_int(input, nr))