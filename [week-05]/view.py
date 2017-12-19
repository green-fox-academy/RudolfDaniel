from tkinter import *
from PIL import ImageTk, Image
from model import *

images = []

class Draw(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width="720", height="720")
        self.canvas.pack()
        self.useful_image = "overwrite"
        self.canvas.focus_set()

    def drawer(self, thing):
        if isinstance(thing, Character):
            useful_image = Image.open(thing.image)
            image_obj = ImageTk.PhotoImage(useful_image)
            images.append(image_obj)
            self.canvas.create_image(thing.coordinate_x + 72, thing.coordinate_y, anchor=NE, image=image_obj)
        else:
            useful_image = Image.open(thing.image)
            image_obj = ImageTk.PhotoImage(useful_image)
            images.append(image_obj)
            self.canvas.create_image(thing.coordinate_x + 72, thing.coordinate_y, anchor=NE, image=image_obj)

