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

        self.internet = self.canvas.create_text(180, 260, fill = "white", font = tkinter.font.Font(family = "Helvetica", size = 25), text = "Invictus hotspot", anchor="sw")
        self.download_text = self.canvas.create_text(205, 295, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 25), text = "35.65", anchor="sw")
        self.upload_text = self.canvas.create_text(340, 295, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 25), text = "6.65", anchor="sw")
        self.ping_text = self.canvas.create_text(475, 295, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 25), text = "35 ms", anchor="sw")
        self.ip_text = self.canvas.create_text(205, 330, fill = "#%02x%02x%02x" % (100, 100, 100), font = tkinter.font.Font(family = "Helvetica", size = 25), text = "192.168.2.6", anchor="sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.canvas.dot3 = file
        self.dot3 = self.canvas.create_image(550, 1455, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/wifi.png"))
        self.canvas.wifi = file
        self.wifi = self.canvas.create_image(120, 280, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/download.png"))
        self.canvas.download = file
        self.download = self.canvas.create_image(175, 290, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/upload.png"))
        self.canvas.upload = file
        self.upload = self.canvas.create_image(310, 290, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/ping.png"))
        self.canvas.ping = file
        self.ping = self.canvas.create_image(445, 290, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/ip.png"))
        self.canvas.ip = file
        self.ip = self.canvas.create_image(175, 325, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.canvas.dot1 = file
        self.dot1 = self.canvas.create_image(470, 1455, image = file, anchor = "sw")

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.canvas.dot2 = file
        self.dot2 = self.canvas.create_image(510, 1455, image = file, anchor = "sw")

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