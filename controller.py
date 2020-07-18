import threading
import time

from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        seconds_thread = threading.Thread(target = self.seconds_handler)
        seconds_thread.start()

        time_thread = threading.Thread(target = self.time_handler)
        time_thread.start()

        date_thread = threading.Thread(target = self.date_handler)
        date_thread.start()

        self.view.main()

    def seconds_handler(self):
        seconds = self.model.get_current_second()
        self.view.seconds.set(seconds)

        t = time.time()
        while True:
            if(time.time() - t >= 1):
                seconds = self.model.get_current_second()
                self.view.seconds.set(seconds)
                t = time.time()
    
    def time_handler(self):
        times = self.model.get_current_time()
        self.view.time.set(times)

        t = time.time()
        while True:
            if(time.time() - t >= 1):
                times = self.model.get_current_time()
                self.view.time.set(times)
                t = time.time()

    def date_handler(self):
        date = self.model.get_current_date()
        self.view.date.set(date)

        t = time.time()
        while True:
            if(time.time() - t >= 60):
                date = self.model.get_current_date()
                self.view.date.set(date)
                t = time.time()


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
