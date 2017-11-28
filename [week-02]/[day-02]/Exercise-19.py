aj = [3, 4, 5, 6, 7]

"""
aj.reverse()
"""

for i in range(0, 5):
    aj.append(aj[i-1])
    print(aj)
    #del aj[i-2]

print(aj)