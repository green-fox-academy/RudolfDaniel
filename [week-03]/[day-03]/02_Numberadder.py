def number_adder(number):
    if number <= 0: #base case
        return number
    else:
        return number + (number_adder(number-1))

print(number_adder(3))