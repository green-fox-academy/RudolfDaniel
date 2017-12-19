from tkinter import *
from PIL import ImageTk, Image

images = []

class Draw(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width="720", height="720")
        self.canvas.pack()
        self.useful_image = "overwrite"

    def drawer(self, thing):
        useful_image = Image.open(thing.image)
        image_obj = ImageTk.PhotoImage(useful_image)
        images.append(image_obj)
        self.canvas.create_image(thing.coordinate_x + 72, thing.coordinate_y, anchor=NE, image=image_obj)
