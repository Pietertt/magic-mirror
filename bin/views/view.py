import tkinter as tk
from PIL import Image, ImageTk

import time

class View():
    def __init__(self, frame):
        self.frame = frame

    def render(self):
        pass

    def white(self, button, image):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/" + image))
        button.config(image = file)
        button.image = file

    def grayscale(self, button, image):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/grayscale/" + image))
        button.config(image = file)
        button.image = file

    def _make_label(self, variable, x, y, backgroundcolor, foregroundcolor, fontsize):
        self.label = tk.Label(master = self.frame, bg = backgroundcolor, textvariable = variable)
        self.label.config(font = ("Helvetica", fontsize), fg = foregroundcolor)
        self.label.place(x = x, y = y)

    def remove_all_widgets(self):
        for widget in self.frame.winfo_children():
            widget.destroy()