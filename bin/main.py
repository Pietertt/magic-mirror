import tkinter as tk
from tkinter import ttk

import threading

from controllers.controller import Controller

class Main(tk.Tk):
    def __init__(self):
        super().__init__()

    def run(self):
        window = tk.Tk()
        frame = tk.Frame()
        frame.config(bg = "black", width = 1016, height = 1856)
        frame.pack()

        calculator = Controller(frame)

        frame_thread = threading.Thread(target = calculator.execute)
        frame_thread.start()

        calculator.main()

        self.main()

if __name__ == "__main__":
    main = Main()
    main.run()