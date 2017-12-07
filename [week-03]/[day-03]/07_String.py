def charchanger(sentence, old, new):
    if sentence == "": #base case
        return ""
    elif sentence[0] == old:
        return new + charchanger(sentence[1:], old, new)
    else:
        return sentence[0] + charchanger(sentence[1:], old, new)

print(charchanger("The quick green fox jumps over the lazy dog.", "x", "y"))