import threading
import time
import tkinter
from tkinter import messagebox as mb

from models.timemodel import TimeModel
from models.framemodel import FrameModel

from view import View

class Controller:
    def __init__(self):
        self.timemodel = TimeModel()
        self.framemodel = FrameModel()
        self.view = View(self)

    def main(self):
        time_thread = threading.Thread(target = self.time_handler)
        time_thread.start()

        # temperature_thread = threading.Thread(target = self.temperature_handler)
        # temperature_thread.start()

        frame_thread = threading.Thread(target = self.frame_handler)
        frame_thread.start()

        self.view.main()

    def time_handler(self):
        self.view.seconds.set(self.timemodel.get_current_second())
        self.view.time.set(self.timemodel.get_current_time())
        self.view.date.set(self.timemodel.get_current_date())

        t = time.time()
        while True:
            if(time.time() - t >= 1):
                self.view.seconds.set(self.timemodel.get_current_second())
                self.view.time.set(self.timemodel.get_current_time())
                self.view.date.set(self.timemodel.get_current_date())

                t = time.time()

    def temperature_handler(self):
        self.view.temperature.set(self.sensormodel.get_temperature())

        t = time.time()
        while True:
            if(time.time() - t >= 5):
                self.view.temperature.set(self.sensormodel.get_temperature())
                t = time.time()

            if((time.time() - t >= 0) and (time.time() - t <= 0.5)):
                self.sensormodel.set_led(1)

            if((time.time() - t >= 0.5) and (time.time() - t <= 1)):
                self.sensormodel.set_led(0)

    def frame_handler(self):
        while True:
            data = self.framemodel.read_serial()
            self.view.temperature.set(self.framemodel.get_temperature())
            if data:
                print(data)
                if(data[1] == 0):
                    self.view._change_label()
                
                if(data[1] == 1):
                    self.view._change_button()
                # if(data[0] == 0):
                #     mb.showinfo("Test", "Test")

if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
