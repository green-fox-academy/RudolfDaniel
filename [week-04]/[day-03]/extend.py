def add(a, b):
    return a + b

def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

def median(pool):
    quotient, remainder = divmod(len(pool), 2)
    if remainder:
        return sorted(pool)[quotient]
    return sum(sorted(pool)[quotient - 1:quotient + 1]) / 2.

def is_vovel(char):
    if char in 'aeiouéáőűöüóí':
        return True
    else:
        return False

def translate(hungarian):
    teve = ""
    for char in hungarian:
        if is_vovel(char):
            teve += (char+'v'+char)
        else:
            teve += (char)
    return teve