import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font

from .view import View

import time

class MainView(View):
    def __init__(self, canvas):
        View.__init__(self, canvas)
        
    def render(self):
        #self._make_label(690, 140, 50, "white")

        self.temperature = self.canvas.create_text(790, 165, fill = "white", font = tkinter.font.Font(family = "Helvetica", size = 50), text = "Hoi")

        self.date = self.canvas.create_text(310, 105, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 25), text = "Hoi")
        self.time = self.canvas.create_text(220, 165, fill = "white", font = tkinter.font.Font(family = "Helvetica", size = 50), text = "Hoi")
        self.seconds = self.canvas.create_text(325, 150, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 25), text = "Hoi")


        self.current_track = self.canvas.create_text(40, 1295, fill = "white", font = tkinter.font.Font(family = "Helvetica", size = 18), text = "Hoi")
        self.current_artist = self.canvas.create_text(40, 1325, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 18), text = "Hoi")
        self.current_device = self.canvas.create_text(40, 1355, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 18), text = "Hoi")
        self.current_time = self.canvas.create_text(40, 1385, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 18), text = "Hoi")

        #self.current_track = self._make_label(40, 1295, 18, "white")
        #self.current_artist = self._make_label(40, 1325, 18, "#%02x%02x%02x" % (100, 100, 100))
        #self.current_device = self._make_label(40, 1355, 18, "#%02x%02x%02x" % (100, 100, 100))
        #self.current_time = self._make_label(40, 1385, 18, "#%02x%02x%02x" % (100, 100, 100))

        # self._make_label(self.temperature, 690, 140, "black", "white", 50)

        # self._make_label(self.date, 120, 100, "black", "#%02x%02x%02x" % (100, 100, 100), 25)
        # self._make_label(self.time, 120, 140, "black", "white", 50)
        # self._make_label(self.seconds, 288, 140, "black", "#%02x%02x%02x" % (100, 100, 100), 25)

        # self._make_label(self.current_track, 40, 1295, "black", "white", 18)
        # self._make_label(self.current_artist, 40, 1325, "black", "#%02x%02x%02x" % (100, 100, 100), 18)
        # self._make_label(self.current_device, 40, 1355, "black", "#%02x%02x%02x" % (100, 100, 100), 18)
        # self._make_label(self.current_time, 40, 1385, "black", "#%02x%02x%02x" % (100, 100, 100), 18)

        # file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/previous.png"))
        # self.previous = tk.Label(self.frame, image = file, borderwidth = 0, highlightthickness = 0)
        # self.previous.image = file
        # self.previous.place(x= 40, y= 1435)

        # file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/pause.png"))
        # self.pause = tk.Label(self.frame, image = file, borderwidth = 0, highlightthickness = 0)
        # self.pause.image = file
        # self.pause.place(x= 103, y= 1435)

        # file = image = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/next.png"))
        # self.next = tk.Label(self.frame, image = file, borderwidth = 0, highlightthickness = 0)
        # self.next.image = file
        # self.next.place(x= 160, y= 1435)

        # file = image = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/coffee.png"))
        # self.coffee = tk.Label(self.frame, image = file, borderwidth = 0, highlightthickness = 0)
        # self.coffee.image = file
        # self.coffee.place(x= 220, y= 1435)

        # file = image = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        # self.dot1 = tk.Label(self.frame, image = file, borderwidth = 0, highlightthickness = 0)
        # self.dot1.image = file
        # self.dot1.place(x= 470, y= 1435)

        # file = image = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        # self.dot2 = tk.Label(self.frame, image = file, borderwidth = 0, highlightthickness = 0)
        # self.dot2.image = file
        # self.dot2.place(x= 510, y= 1435)

        # file = image = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        # self.dot3 = tk.Label(self.frame, image = file, borderwidth = 0, highlightthickness = 0)
        # self.dot3.image = file
        # self.dot3.place(x= 550, y= 1435)