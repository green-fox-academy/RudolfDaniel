students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1}
]

def candies():
    x = 0
    for i in students:
        x += i["candies"]
    print(x)

def age():
    y = 0
    for i in students:
        if i["candies"] < 5:
            y += i["age"]
    print(y)

candies()
age()