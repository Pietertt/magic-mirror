
import time
import tkinter as tk
from PIL import Image, ImageTk

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

        self.downloaded = False

        file = ImageTk.PhotoImage(file='/home/pi/Desktop/magic-mirror/bin/apod.jpg')
        self.view.canvas.apod_image = file
        self.view.apod_image = self.view.canvas.create_image(120, 320, image = file, anchor = "nw")


        self.view.update_item(self.view.temperature, self.framemodel.get_temperature())

        self.view.update_item(self.view.time, self.timemodel.get_current_time())
        self.view.update_item(self.view.date, self.timemodel.get_current_date())
        self.view.update_item(self.view.seconds, self.timemodel.get_current_second())

    def execute(self, data):
        
        t = time.time()
        local = time.localtime(t)
        minute = str(local.tm_min)



        if((minute == "38") and (self.downloaded == False)):
            self.internetmodel.get_apod()
            self.internetmodel.get_apod_image()
            self.downloaded = True

        if((time.time() - self.time_timer) >= 1):
            # Update the view 
            self.view.update_item(self.view.time, self.timemodel.get_current_time())
            self.view.update_item(self.view.date, self.timemodel.get_current_date())
            self.view.update_item(self.view.seconds, self.timemodel.get_current_second())
             
            self.time_timer = time.time()

        if((time.time() - self.internet_timer) >= 5):
            self.internet_timer = time.time()

            self.view.update_item(self.view.temperature, self.framemodel.get_temperature())