lenght_of_list = int(input("Type in a number "))

list_of_nr = []

while len(list_of_nr) < lenght_of_list:
    list_of_nr.append(int(input("Type in a number: ")))

print("Sum: " + str((sum(list_of_nr))))
print("Average: " + str((sum(list_of_nr))/lenght_of_list))