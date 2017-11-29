verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"


def create_new_verbs():
    for i in range(0, 5):
        verbs[i] = "be" + verbs[i]
    print(verbs)

create_new_verbs()