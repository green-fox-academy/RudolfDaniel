nr_of_girls = int(input("Type in the number of girls: "))
nr_of_boys = int(input("Type in the number of boys: "))

if nr_of_girls == nr_of_boys and (nr_of_girls + nr_of_boys) > 20:
    print("The party is exellent!")
elif nr_of_girls != nr_of_boys and (nr_of_girls + nr_of_boys) > 20:
    print("Quite cool party!")
elif (nr_of_girls + nr_of_boys) <= 20 and nr_of_girls != 0:
    print("Average party")
elif nr_of_girls == 0:
    print("Sausage party")