import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font

from .view import View

import time

class MainView(View):
    def __init__(self, canvas):
        View.__init__(self, canvas)
        
    def render(self):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/lock.png"))
        self.canvas.lock = file
        self.lock = self.canvas.create_image(250, 1150, image = file, anchor = "sw")
