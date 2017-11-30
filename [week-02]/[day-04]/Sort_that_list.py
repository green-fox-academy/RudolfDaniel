def list_of_numbers(a):
    output = []
    for i in range(len(a)):
        if a[i] not in output:
            output.append(a[i])
    return sorted(output, reverse = False)

numbers = (input("Type in numbers with spaces between them: "))
ls = numbers.split()

print(list_of_numbers(ls))