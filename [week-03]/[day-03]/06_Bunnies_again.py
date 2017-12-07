def earcounter(bunnies):
    if bunnies == 0: #base case
        return 0
    elif bunnies % 2 == 0:
        return 3 + earcounter(bunnies-1)
    else:
        return 2 + earcounter(bunnies-1)

print(earcounter(10))

"""
Alternate version:

def earcounter(ears, bunnies):
    if bunnies == 0: #base case
        return 0
    else:
        return ears + earcounter(ears, bunnies-1)

print(earcounter(2.5, 10))
"""