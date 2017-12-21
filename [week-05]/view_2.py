from tkinter import *
from PIL import ImageTk, Image
from model_2 import *

images = []

class Draw(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width="720", height="750")
        self.canvas.pack()
        self.canvas.focus_set()

    def drawer(self, thing_to_draw):
            image_to_draw = Image.open(thing_to_draw.image)
            image_obj = ImageTk.PhotoImage(image_to_draw)
            images.append(image_obj)
            self.canvas.create_image(thing_to_draw.coordinate_x + 72, thing_to_draw.coordinate_y, anchor=NE, image=image_obj)
