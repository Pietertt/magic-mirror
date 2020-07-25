import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import time

class MainView(tk.Tk):

    t = time.time()

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title("Magic Mirror")

        self.wm_attributes('-type', 'splash')


        self.temperature = tk.StringVar()
        self.date = tk.StringVar()
        self.time = tk.StringVar()
        self.seconds = tk.StringVar()

        self.current_track = tk.StringVar()
        self.current_artist = tk.StringVar()
        self.current_device = tk.StringVar()
        self.current_time = tk.StringVar()

        self._make_main_frame()

        self._make_label(self.temperature, 690, 140, "black", "white", 50)

        self._make_label(self.date, 120, 100, "black", "#%02x%02x%02x" % (100, 100, 100), 25)
        self._make_label(self.time, 120, 140, "black", "white", 50)
        self._make_label(self.seconds, 288, 140, "black", "#%02x%02x%02x" % (100, 100, 100), 25)

        self._make_label(self.current_track, 40, 1295, "black", "white", 18)
        self._make_label(self.current_artist, 40, 1325, "black", "#%02x%02x%02x" % (100, 100, 100), 18)
        self._make_label(self.current_device, 40, 1355, "black", "#%02x%02x%02x" % (100, 100, 100), 18)
        self._make_label(self.current_time, 40, 1385, "black", "#%02x%02x%02x" % (100, 100, 100), 18)

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/previous.png"))
        self.previous = tk.Label(self, image = file, borderwidth = 0, highlightthickness = 0)
        self.previous.image = file
        self.previous.place(x= 40, y= 1435)

        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/pause.png"))
        self.pause = tk.Label(self, image = file, borderwidth = 0, highlightthickness = 0)
        self.pause.image = file
        self.pause.place(x= 103, y= 1435)

        file = image = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/next.png"))
        self.next = tk.Label(self, image = file, borderwidth = 0, highlightthickness = 0)
        self.next.image = file
        self.next.place(x= 160, y= 1435)

        file = image = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/coffee.png"))
        self.coffee = tk.Label(self, image = file, borderwidth = 0, highlightthickness = 0)
        self.coffee.image = file
        self.coffee.place(x= 220, y= 1435)

        file = image = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.dot1 = tk.Label(self, image = file, borderwidth = 0, highlightthickness = 0)
        self.dot1.image = file
        self.dot1.place(x= 470, y= 1500)

        file = image = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/dot.png"))
        self.dot2 = tk.Label(self, image = file, borderwidth = 0, highlightthickness = 0)
        self.dot2.image = file
        self.dot2.place(x= 550, y= 1500)

        self._enlarge_window()

    def white(self, button, image):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/white/" + image))
        button.config(image = file)
        button.image = file

    def grayscale(self, button, image):
        file = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/magic-mirror/assets/images/grayscale/" + image))
        button.config(image = file)
        button.image = file

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.frame = tk.Frame(self)
        self.frame.config(bg = "black", width = 1016, height = 1856)
        self.frame.pack()

    def _make_label(self, variable, x, y, backgroundcolor, foregroundcolor, fontsize):
        self.label = tk.Label(master = self.frame, bg = backgroundcolor, textvariable = variable)
        self.label.config(font = ("Helvetica", fontsize), fg = foregroundcolor)
        self.label.place(x = x, y = y)

    def _pause_button_pause(self):
        self.pause.config(bg = "red")
    
    def _pause_button_play(self):
        self.pause.config(bg = "white")

    def _enlarge_window(self):
        self.update()
        self.geometry(str(1016) + "x" + str(1856) + "+0+0")