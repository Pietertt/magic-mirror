import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font

from .view import View

import time

class FirstView(View):
    def __init__(self, canvas):
        View.__init__(self, canvas)
                
    def render(self):

        self.temperature = self.canvas.create_text(700, 200, fill = "white", font = tkinter.font.Font(family = "Helvetica", size = 50), anchor="sw")

        self.date = self.canvas.create_text(120, 130, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 25), anchor="sw")
        self.time = self.canvas.create_text(120, 200, fill = "white", font = tkinter.font.Font(family = "Helvetica", size = 50), anchor="sw")
        self.seconds = self.canvas.create_text(288, 170, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 25), anchor="sw")

        self.current_track = self.canvas.create_text(40, 1315, fill = "white", font = tkinter.font.Font(family = "Helvetica", size = 18), anchor="sw")
        self.current_artist = self.canvas.create_text(40, 1345, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 18), anchor="sw")
        self.current_device = self.canvas.create_text(40, 1375, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 18), anchor="sw")
        self.current_time = self.canvas.create_text(40, 1405, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 18), anchor="sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/previous.png"))
        self.canvas.previous = file
        self.previous = self.canvas.create_image(40, 1455, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/pause.png"))
        self.canvas.pause = file
        self.pause = self.canvas.create_image(103, 1455, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/next.png"))
        self.canvas.next = file
        self.next = self.canvas.create_image(160, 1455, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.canvas.dot1 = file
        self.dot1 = self.canvas.create_image(470, 1455, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/grayscale/dot.png"))
        self.canvas.dot2 = file
        self.dot2 = self.canvas.create_image(510, 1455, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/grayscale/dot.png"))
        self.canvas.dot3 = file
        self.dot3 = self.canvas.create_image(550, 1455, image = file, anchor = "sw")

    def disable_previous_button(self):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/grayscale/previous.png"))
        self.canvas.previous = file
        self.canvas.itemconfig(self.previous, image = file)

    def enable_previous_button(self):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/previous.png"))
        self.canvas.previous = file
        self.canvas.itemconfig(self.previous, image = file)



    def disable_next_button(self):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/grayscale/next.png"))
        self.canvas.next = file
        self.canvas.itemconfig(self.next, image = file)

    def enable_next_button(self):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/next.png"))
        self.canvas.next = file
        self.canvas.itemconfig(self.next, image = file)



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