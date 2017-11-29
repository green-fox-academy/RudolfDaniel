watchlist = []

security_alcohol_loot = 0

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

def entry():
    security_alcohol_loot = 0
    no_entry = "No pasarán!!!"
    welcome = "You are welcome as hell!"
    for i in range(0, len(queue)):
        if queue[i]["guns"] > 0:
            watchlist.append(queue[i]["name"])
            queue[i]["guns"] = 0
        else:
            print(no_entry)
    for i in range(0, len(queue)):
        if queue[i]["alcohol"] > 0:
            security_alcohol_loot += queue[i]["alcohol"]
            queue[i]["alcohol"] = 0
        else:
            print(welcome)
    print(watchlist)
    print(security_alcohol_loot)

entry()