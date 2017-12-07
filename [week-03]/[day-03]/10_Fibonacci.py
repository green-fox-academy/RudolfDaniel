def fibonacci(number):
    if number < 2: #base case
        return number
    else:
        return (fibonacci(number-1) + fibonacci(number-2))

print(fibonacci(8))