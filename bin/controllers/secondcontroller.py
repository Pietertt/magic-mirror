
import time
import tkinter as tk
import threading

from models.timemodel import TimeModel
from models.internetmodel import InternetModel

from .controller import Controller

class SecondController(Controller):

    def __init__(self, view, tk):
        Controller.__init__(self, view, tk)

        self.timemodel = TimeModel()
        self.internetmodel = InternetModel()

        self.internet_timer = time.time()
        self.time_timer = time.time()

        self.internetmodel.execute_speed_test()
        
    def execute(self, data):
        print(data)

        if((time.time() - self.time_timer) >= 1):
            # Update the view 
            self.view.update_item(self.view.time, self.timemodel.get_current_time())
            self.view.update_item(self.view.date, self.timemodel.get_current_date())
            self.view.update_item(self.view.seconds, self.timemodel.get_current_second())
            
            self.time_timer = time.time()

        if((time.time() - self.internet_timer) >= 5):
            self.internetmodel.execute_speed_test()
            self.internet_timer = time.time()

            try:
                self.view.update_item(self.view.download_text, self.internetmodel.download_speed)
                self.view.update_item(self.view.upload_text, self.internetmodel.upload_speed)
                self.view.update_item(self.view.ping_text, self.internetmodel.ping)
                self.view.update_item(self.view.ip_text, self.internetmodel.get_ip_address())
            except AttributeError:
                print("Oops")