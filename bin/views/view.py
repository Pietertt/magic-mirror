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