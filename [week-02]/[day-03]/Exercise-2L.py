girls = ["Eve", "Ashley", "Bözsi", "Kat", "Jane"]

boys = ["Joe", "Fred", "Béla", "Todd", "Neef", "Jeff"]

order = []

for i in range(len(boys)):
    if i <= len(girls)-1:
        order.append(girls[i])
    order.append(boys[i])

print(order)