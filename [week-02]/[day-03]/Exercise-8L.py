def calculator(a, b, c):
    if lista[0] == "+":
        return int(b) + int(c)
    elif lista[0] == "-":
        return int(b) - int(c)
    elif lista[0] == "*":
        return int(b) * int(c)
    elif lista[0] == "/":
        return int(b) / int(c)
    elif lista[0] == "%":
        return int(c) / (int(b)*0.01)
    else:
        print("Hiba")

blabla = input("Please type in the expression: ")
lista = blabla.split(" ")

print(calculator(lista[0], lista[1], lista[2]))