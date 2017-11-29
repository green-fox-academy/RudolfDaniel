students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

def many_candies():
    for i in students:
        if i["candies"] > 4:
            print(i["name"] + " has more, than four candies.")

def ave():
    y = 0
    for i in students:
        y += i["candies"]
    y = y/(len(students))
    print(y)

many_candies()
ave()