ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True }
]

def table():
    for i in range(0, len(ingredients)):
        if ingredients[i]["needs_cooling"] == True:
            ingredients[i]["needs_cooling"] = "Yes"
        else:
            ingredients[i]["needs_cooling"] = "No"
    print("+" + "-"*20 + "+" + "-"*15 + "+" + "-"*10 + "+")
    print("| Ingredient         | Needs cooling | In stock |")
    print("+" + "-"*20 + "+" + "-"*15 + "+" + "-"*10 + "+")
    for i in range(0, len(ingredients)):
        print("| " + ingredients[i]["name"] + " "*(19-len(ingredients[i]["name"])) + "| ")

table()