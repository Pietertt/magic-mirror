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


    def white(self, button, image):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/" + image))
        self.canvas.itemconfig(button, image = file)

    def grayscale(self, button, image):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/grayscale/" + image))
        self.canvas.itemconfig(button, image = file)

    # def _make_label(self, variable, x, y, backgroundcolor, foregroundcolor, fontsize):
    #     self.label = tk.Label(master = self.frame, bg = backgroundcolor, textvariable = variable)
    #     self.label.config(font = ("Helvetica", fontsize), fg = foregroundcolor)
    #     self.label.place(x = x, y = y)

    # def remove_all_widgets(self):
    #     for widget in self.frame.winfo_children():
    #         widget.destroy()

    # def move_all_widgets(self):
    #     for i in range(500):
    #         for widget in self.frame.winfo_children():
    #             widget.place(x = widget.winfo_rootx() + 3, y = widget.winfo_rooty())
    #             time.sleep(0.01)