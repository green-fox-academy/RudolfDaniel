def armstrong(a):
    digits = [int(x) for x in str(a)]
    amount = 0
    for i in range(0, len(digits)):
        amount += digits[i]**len(digits)
    if amount == a:
        print("The " + str(a) + " is an Armstrong number.")
    
armstrong(int(input("Type in a number: ")))