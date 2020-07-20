import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class View(tk.Tk):

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title("Magic Mirror")


        self.temperature = tk.StringVar()
        self.date = tk.StringVar()
        self.time = tk.StringVar()
        self.seconds = tk.StringVar()

        self.current_track = tk.StringVar()
        self.current_artist = tk.StringVar()
        self.current_device = tk.StringVar()
        self.current_time = tk.StringVar()

        self._make_main_frame()

        self._make_label(self.temperature, 790, 380, "black", "white", 50)
        self._make_label(self.date, 30, 340, "black", "#%02x%02x%02x" % (100, 100, 100), 25)
        self._make_label(self.time, 30, 380, "black", "white", 50)
        self._make_label(self.seconds, 198, 380, "black", "#%02x%02x%02x" % (100, 100, 100), 25)

        self._make_label(self.current_track, 30, 1170, "black", "white", 18)
        self._make_label(self.current_artist, 30, 1200, "black", "#%02x%02x%02x" % (100, 100, 100), 18)
        self._make_label(self.current_device, 30, 1230, "black", "#%02x%02x%02x" % (100, 100, 100), 18)
        self._make_label(self.current_time, 30, 1260, "black", "#%02x%02x%02x" % (100, 100, 100), 18)

        load = Image.open("assets/images/pause.png")
        render = ImageTk.PhotoImage(load)

        self.pause = tk.Label(self, image = render, borderwidth = 0, highlightthickness = 0)
        self.pause.image = render
        self.pause.place(x= 30, y= 1310)

        load = Image.open("assets/images/next.png")
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image = render, borderwidth = 0, highlightthickness = 0)
        img.image = render
        img.place(x= 90, y= 1310)

        self._enlarge_window()

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