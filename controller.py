import threading
import time

from models.timemodel import TimeModel
from models.sensormodel import SensorModel 
from models.framemodel import FrameModel

from view import View

class Controller:
    def __init__(self):
        self.timemodel = TimeModel()
        self.sensormodel = SensorModel()
        self.framemodel = FrameModel()
        self.view = View(self)

    def main(self):
        # time_thread = threading.Thread(target = self.time_handler)
        # time_thread.start()

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
            self.framemodel.read_serial()

if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
