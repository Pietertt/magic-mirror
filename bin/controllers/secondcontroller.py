
import time
import tkinter as tk

from models.timemodel import TimeModel
from models.internetmodel import InternetModel
from models.framemodel import FrameModel

from .controller import Controller

class SecondController(Controller):

    def __init__(self, view, tk):
        Controller.__init__(self, view, tk)

        self.timemodel = TimeModel()
        self.internetmodel = InternetModel()
        self.framemodel = FrameModel()

        self.time_timer = time.time()
        self.internet_timer = time.time()

        self.view.update_item(self.view.temperature, self.framemodel.get_temperature())

        self.view.update_item(self.view.time, self.timemodel.get_current_time())
        self.view.update_item(self.view.date, self.timemodel.get_current_date())
        self.view.update_item(self.view.seconds, self.timemodel.get_current_second())

    def execute(self, data):
        print(data)

        if((time.time() - self.time_timer) >= 1):
            # Update the view 
            self.view.update_item(self.view.time, self.timemodel.get_current_time())
            self.view.update_item(self.view.date, self.timemodel.get_current_date())
            self.view.update_item(self.view.seconds, self.timemodel.get_current_second())
             
            self.time_timer = time.time()

        if((time.time() - self.internet_timer) >= 5):
            self.internet_timer = time.time()

            self.view.update_item(self.view.temperature, self.framemodel.get_temperature())