accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

def balance():
    nr = int((input("Type in account number: ")))
    balance = "404 - account not found"
    for i in range(0, len(accounts)):
        if nr == accounts[i]["account_number"]:
            balance = accounts[i]["balance"]
    return balance

print(balance())

def transfer():
    accfrom = int(input("Type in account number transfer from: "))
    accto = int(input("Type in account number transfer to: "))
    amount = int(input("Type in amount: "))
    for i in range(0, len(accounts)):
        if accfrom == accounts[i]["account_number"]:
            accounts[i]["balance"] -= amount
    for i in range(0, len(accounts)):
        if accto == accounts[i]["account_number"]:
            accounts[i]["balance"] += amount
    return print(accounts)

print(transfer())