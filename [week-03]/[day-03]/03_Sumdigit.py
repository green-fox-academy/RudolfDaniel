def sumdigit(number):
    if number > 0 and number < 10: #base case
        return number
    else:
        return (number % 10) + sumdigit(number // 10)

print(sumdigit(1234))