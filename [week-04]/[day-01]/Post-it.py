class PostIt(object):
    background_color = None
    text = None
    text_color = None

orange = PostIt()
pink = PostIt()
yellow = PostIt()

orange.text_color = "blue"
orange.text = "Idea 1"
pink.text_color = "black"
pink.text = "Awasome"
yellow.text_color = "green"
yellow.text = "Superb!"

print(orange.text)
print(pink.text)
print(yellow.text)