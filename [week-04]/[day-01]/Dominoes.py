from domino import Domino

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = initialize_dominoes()
print(dominoes)

def sorting(dominoes):
    new_dominoes = []
    new_dominoes.append(dominoes[0])    

    while len(new_dominoes) != len(dominoes):
        for i in range(1, len(dominoes)):
            if dominoes[i].values[0] == new_dominoes[-1].values[1]:
                new_dominoes.append(dominoes[i])

    return new_dominoes

print(sorting(dominoes))