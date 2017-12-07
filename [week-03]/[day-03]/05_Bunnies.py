def earcounter(ears, bunnies):
    if bunnies == 0: #base case
        return 0
    else:
        return ears + earcounter(ears, bunnies-1)

print(earcounter(2, 100))