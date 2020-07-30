import tkinter as tk
from PIL import Image, ImageTk

import time

class View():
    def __init__(self, canvas):
        self.canvas = canvas

    def render(self):
        pass

    def update_item(self, item, text):
        self.canvas.itemconfigure(item, text = text)

    def clear_canvas(self):
        self.canvas.delete("all")

    def spawn(self):
        print("Spawned")

        # children = self.canvas.find_withtag("all")

        # for child in children:
        #     # coordinates = self.canvas.coords(child)
        #     #self.canvas.move(child, 1, 0)
        #     self.canvas.itemconfig(child, alpha = .1)


        # self.canvas.after(100, self.spawn)
        

        # for child in children:
        #     coordinates = self.canvas.coords(child)
        #     #self.canvas.coords(child, coordinates[0] - 1016, coordinates[1] - 1016)

