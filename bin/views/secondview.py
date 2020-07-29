import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font

from .view import View

import time

class SecondView(View):
    def __init__(self, canvas):
        View.__init__(self, canvas)
        
    def render(self):

        self.temperature = self.canvas.create_text(700, 200, fill = "white", font = tkinter.font.Font(family = "Helvetica", size = 50), anchor="sw")

        self.date = self.canvas.create_text(120, 130, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 25), anchor="sw")
        self.time = self.canvas.create_text(120, 200, fill = "white", font = tkinter.font.Font(family = "Helvetica", size = 50), anchor="sw")
        self.seconds = self.canvas.create_text(288, 170, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 25), anchor="sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.canvas.dot1 = file
        self.dot1 = self.canvas.create_image(470, 1475, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.canvas.dot2 = file
        self.dot2 = self.canvas.create_image(510, 1475, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.canvas.dot3 = file
        self.dot3 = self.canvas.create_image(550, 1475, image = file, anchor = "sw")

    def disable_dot1_button(self):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/grayscale/dot.png"))
        self.canvas.dot1 = file
        self.canvas.itemconfig(self.dot1, image = file)

    def enable_dot1_button(self):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.canvas.dot1 = file
        self.canvas.itemconfig(self.dot1, image = file)



    def disable_dot3_button(self):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/grayscale/dot.png"))
        self.canvas.dot3 = file
        self.canvas.itemconfig(self.dot3, image = file)

    def enable_dot3_button(self):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.canvas.dot3 = file
        self.canvas.itemconfig(self.dot3, image = file)