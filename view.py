import tkinter as tk
from tkinter import ttk

class View(tk.Tk):

    #PADDING = 10


    # button_captions = [
    #     "C", "+/-", "%", "/", 
    #     7, 8, 9, '*',
    #     4, 5, 6, "-",
    #     1, 2, 3, "+",
    #     0, ".", "="
    # ]

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title("Magic Mirror")


        self.temperature = tk.StringVar()
        self.date = tk.StringVar()
        self.time = tk.StringVar()
        self.seconds = tk.StringVar()

        self._make_main_frame()

        self._make_label(self.temperature, 825, 380, "black", "white", 50)
        self._make_label(self.date, 30, 340, "black", "white", 25)
        self._make_label(self.time, 30, 380, "black", "white", 50)
        self._make_label(self.seconds, 198, 380, "black", "white", 25)

        self._enlarge_window()



    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.frame = tk.Frame(self)
        self.frame.config(bg = "black", width = 1016, height = 1856)
        self.frame.pack()
        

    def _make_label(self, variable, x, y, backgroundcolor, foregroundcolor, fontsize):
        label = tk.Label(master = self.frame, bg = backgroundcolor, textvariable = variable)
        label.config(font = ("Helvetica", fontsize), fg = foregroundcolor)
        label.place(x = x, y = y)


    

    # def _make_entry(self):
    #     entry = ttk.Entry(self.frame, textvariable = self.value_var, justify = "right", state = "disabled")
    #     entry.pack(fill = "x")

    # def _make_buttons(self):
    #     outer_frame = ttk.Frame(self.frame)
    #     outer_frame.pack()

    #     frame = ttk.Frame(outer_frame)
    #     frame.pack()

    #     buttons_in_row = 0

    #     for caption in self.button_captions:
    #         if(buttons_in_row == self.MAX_BUTTONS_PER_ROW):
    #             frame = ttk.Frame(outer_frame)
    #             frame.pack()
    #             buttons_in_row = 0
            
    #         button = ttk.Button(frame, text = caption, command = (lambda button = caption: self.controller.on_button_click(button)))
    #         button.pack(side = "left")

    #         buttons_in_row += 1

    def _enlarge_window(self):
        self.update()
        self.geometry(str(1016) + "x" + str(1856) + "+0+0")