def list_of_numbers(a):
    output = []
    for i in range(len(a)):
        if a[i] not in output:
            output.append(a[i])
    return output



numbers = (input("Type in numbers with spaces between them: "))
ls = numbers.split()

print(list_of_numbers(ls))