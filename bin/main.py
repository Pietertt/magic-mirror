import tkinter as tk
import time

from controllers.firstcontroller import FirstController
from controllers.secondcontroller import SecondController
from controllers.thirdcontroller import ThirdController
from controllers.maincontroller import MainController

from views.firstview import FirstView
from views.secondview import SecondView
from views.thirdview import ThirdView
from views.mainview import MainView

from models.framemodel import FrameModel

class Main(tk.Tk):
    
    cooldown = False
    COOLDOWN_TIME = 1500

    DOT_2_SENSOR = 0
    DOT_1_SENSOR = 1
    LINE_SENSOR = 4

    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, width = 1016, height = 1856, bg = "black")
        self.canvas.pack()
        self.title("Magic Mirror")
        self.wm_attributes('-type', 'splash')

        self.framemodel = FrameModel()

        self.view = ThirdView(self.canvas)
        self.view.render()
        #self.view.spawn()

        self.controller = ThirdController(self.view, self)

        self.temperature_timer = time.time()

        while True:
            self.update()
            data = self.framemodel.read_serial()
            if data:
                # Dot 1
                if((data[self.DOT_2_SENSOR] < 200) and (data[self.LINE_SENSOR] < 100)):
                    if(self.cooldown == False):
                        print("View 1")
                        self.set_cooldown()
                        #self.view.disable_dot1_button()
                        #self.after(self.COOLDOWN_TIME, lambda: self.view.enable_dot1_button())
                        self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())

                        self.view.clear_canvas()
                        self.view = FirstView(self.canvas)
                        self.view.render()

                        self.controller = FirstController(self.view, self)

                # Dot 2
                if((data[self.DOT_2_SENSOR] > 250) and (data[self.DOT_1_SENSOR] > 250) and (data[3] > 200) and (data[2] > 250) and (data[self.LINE_SENSOR] < 100)):
                    self.set_cooldown()
                    print("View 2" + str(data[self.DOT_1_SENSOR]))
            
                    #self.view.disable_dot3_button()
                    #self.after(self.COOLDOWN_TIME, lambda: self.view.enable_dot3_button())
                    self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())
                    
                    self.view.clear_canvas()
                    self.view = SecondView(self.canvas)

                    self.view.render()

                    self.controller = SecondController(self.view, self)
                # Dot 3
                if((data[self.DOT_1_SENSOR] < 200) and (data[self.LINE_SENSOR] < 100)):
                    if(self.cooldown == False):
                        self.set_cooldown()
                        #self.view.disable_dot3_button()
                        #self.after(self.COOLDOWN_TIME, lambda: self.view.enable_dot3_button())
                        self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())
                        
                        self.view.clear_canvas()
                        self.view = ThirdView(self.canvas)

                        self.view.render()

                        self.controller = ThirdController(self.view, self)

                # Update the temperature value
                if((time.time() - self.temperature_timer) >= 5):
                    
                    self.temperature_timer = time.time()

                self.controller.execute(data)


                # Execute the current controller
    
    def set_cooldown(self):
        self.cooldown = True

    def reset_cooldown(self):
        self.cooldown = False

if __name__ == "__main__":
    main = Main()
    main.loop()