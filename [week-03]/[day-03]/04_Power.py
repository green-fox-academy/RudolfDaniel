def powermaker(base, power):
    if base == 0 or power == 0: #base case
        return 1
    else:
        return base * powermaker(base, power-1)

print(powermaker(3, 2))