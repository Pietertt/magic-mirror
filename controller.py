import threading
import time

from timemodel import TimeModel
from view import View

class Controller:
    def __init__(self):
        self.timemodel = TimeModel()
        self.view = View(self)

    def main(self):
        time_thread = threading.Thread(target = self.time_handler)
        time_thread.start()

        self.view.main()

    def time_handler(self):
        seconds = self.timemodel.get_current_second()
        self.view.seconds.set(seconds)

        t = time.time()
        while True:
            if(time.time() - t >= 1):
                seconds = self.timemodel.get_current_second()
                self.view.seconds.set(seconds)

                times = self.timemodel.get_current_time()
                self.view.time.set(times)

                date = self.timemodel.get_current_date()
                self.view.date.set(date)

                t = time.time()

if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
