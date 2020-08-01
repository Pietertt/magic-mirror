import tkinter as tk
import time

from controllers.maincontroller import MainController
from controllers.secondcontroller import SecondController

from views.mainview import MainView
from views.secondview import SecondView

from models.framemodel import FrameModel

class Main(tk.Tk):
    
    cooldown = False
    COOLDOWN_TIME = 1500

    DOT_2_SENSOR = 0
    DOT_1_SENSOR = 1

    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, width = 1016, height = 1856, bg = "black")
        self.canvas.pack()
        self.title("Magic Mirror")
        self.wm_attributes('-type', 'splash')

        self.framemodel = FrameModel()

        self.view = SecondView(self.canvas)
        self.view.render()
        #self.view.spawn()

        self.controller = SecondController(self.view, self)

        self.temperature_timer = time.time()

        while True:
            self.update()
            data = self.framemodel.read_serial()
            self.controller.execute(data)
            if data:

                # Dot 1
                if(data[self.DOT_1_SENSOR] < 200):
                    if(self.cooldown == False):
                        pass
                        # self.set_cooldown()
                        # self.view.disable_dot1_button()
                        # self.after(self.COOLDOWN_TIME, lambda: self.view.enable_dot1_button())
                        # self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())

                        # self.view.clear_canvas()
                        # self.view = MainView(self.canvas)
                        # self.view.render()

                        # self.controller = MainController(self.view, self)

                # Dot 2
                if(data[self.DOT_2_SENSOR] < 200):
                    if(self.cooldown == False):
                        pass
                        # self.set_cooldown()
                        # self.view.disable_dot3_button()
                        # self.after(self.COOLDOWN_TIME, lambda: self.view.enable_dot3_button())
                        # self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())
                        
                        # self.view.clear_canvas()
                        # self.view = SecondView(self.canvas)

                        # self.view.render()

                        # self.controller = SecondController(self.view, self)

                # Update the temperature value
                if((time.time() - self.temperature_timer) >= 5):
                    self.view.update_item(self.view.temperature, self.framemodel.get_temperature())
                    self.temperature_timer = time.time()

                # Execute the current controller

if __name__ == "__main__":
    main = Main()
    main.loop()