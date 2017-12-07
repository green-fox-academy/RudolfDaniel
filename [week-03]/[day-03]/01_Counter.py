def final_countdown(number):
    if number == 0: #base case
        return 0
    else:
        return (final_countdown(number-1))

print(final_countdown(10))