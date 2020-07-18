import tkinter as tk
from tkinter import ttk

class View(tk.Tk):

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title("Magic Mirror")


        self.temperature = tk.StringVar()
        self.date = tk.StringVar()
        self.time = tk.StringVar()
        self.seconds = tk.StringVar()

        self._make_main_frame()

        self._make_label(self.temperature, 790, 380, "black", "white", 50)
        self._make_label(self.date, 30, 340, "black", "#%02x%02x%02x" % (100, 100, 100), 25)
        self._make_label(self.time, 30, 380, "black", "white", 50)
        self._make_label(self.seconds, 198, 380, "black", "#%02x%02x%02x" % (100, 100, 100), 25)

        self.make_button()

        self._enlarge_window()

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.frame = tk.Frame(self)
        self.frame.config(bg = "black", width = 1016, height = 1856)
        self.frame.pack()

    def make_button(self):
        self.button = tk.Button(master = self.frame, bg = "white", text = "Klik mij")
        self.button.place(x = 30, y = 1310)
        

    def _make_label(self, variable, x, y, backgroundcolor, foregroundcolor, fontsize):
        self.label = tk.Label(master = self.frame, bg = backgroundcolor, textvariable = variable)
        self.label.config(font = ("Helvetica", fontsize), fg = foregroundcolor)
        self.label.place(x = x, y = y)

    def _change_label(self):
        self.button.config(bg = "red")
    
    def _change_button(self):
        self.button.config(bg = "white")

    def _enlarge_window(self):
        self.update()
        self.geometry(str(1016) + "x" + str(1856) + "+0+0")