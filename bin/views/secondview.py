import tkinter as tk
from PIL import Image, ImageTk

from .view import View

import time

class SecondView(View):
    def __init__(self, frame):
        View.__init__(self, frame)
        
        self.date = tk.StringVar()
        self.time = tk.StringVar()
        self.seconds = tk.StringVar()
        
    def render(self):
        self._make_label(self.date, 120, 100, "black", "#%02x%02x%02x" % (100, 100, 100), 25)
        self._make_label(self.time, 120, 140, "black", "white", 50)
        self._make_label(self.seconds, 288, 140, "black", "#%02x%02x%02x" % (100, 100, 100), 25)

        file = image = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.dot1 = tk.Label(self.frame, image = file, borderwidth = 0, highlightthickness = 0)
        self.dot1.image = file
        self.dot1.place(x= 470, y= 1500)

        file = image = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.dot2 = tk.Label(self.frame, image = file, borderwidth = 0, highlightthickness = 0)
        self.dot2.image = file
        self.dot2.place(x= 550, y= 1500)

        