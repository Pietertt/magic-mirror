import threading

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

        # print(self.model.get_current_time())
        # self.view.temperature.set("20.0")
        # self.view.date.set("Zaterdag, 18 juli 2020")
        # self.view.time.set("11:54")
        # self.view.seconds.set("46")
        self.view.main()

    def seconds_handler(self):
        while True:
            seconds = self.model.get_current_second()
            self.view.seconds.set(seconds)
    
    def time_handler(self):
        while True:
            time = self.model.get_current_time()
            self.view.time.set(time)

    def date_handler(self):
        while True:
            date = self.model.get_current_date()
            self.view.date.set(date)


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
