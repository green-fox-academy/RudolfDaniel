out = ""
not_so_cryptic_message = [1, 12, 1, 2, 11, 1, 7, 11, 1, 49, 1, 3, 11, 1, 50, 11]

hashmap = {
    7: "run around and desert you",
    50: "tell a lie and hurt you",
    49: "make you cry,",
    2: "let you down",
    12: "give you up,",
    1: "Never gonna",
    11: "\n",
    3: "say goodbye"
}

def make_message():
    out = ""
    for i in range(len(not_so_cryptic_message)):
        out = out + (hashmap[not_so_cryptic_message[i]] + " ")
    print(out)

make_message()