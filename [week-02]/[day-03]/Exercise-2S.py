reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"


def reversed_string(reversed):
    norma = ""
    for i in range(-1, -(len(reversed)+1), -1):
        norma += reversed[i]
    print(norma)

reversed_string(reversed)