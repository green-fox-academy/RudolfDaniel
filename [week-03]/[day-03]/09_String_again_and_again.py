def charchanger(sentence, star):
    if sentence == "": #base case
        return ""
    else:
        return sentence[0] + star + charchanger(sentence[1:], star)

print(charchanger("The quick green fox jumps over the lazy dog.", "*"))