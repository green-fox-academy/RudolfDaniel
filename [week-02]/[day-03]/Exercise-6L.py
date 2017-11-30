list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def check(a):
    checklist = [4, 8, 12, 16]
    contain_all = True
    for i in range(len(checklist)):
        contain = False
        for j in range(len(list_of_numbers)):
            if checklist[i] == a[j]:
                contain = True
        contain_all = contain_all and contain
    
    print(contain_all)

check(list_of_numbers)