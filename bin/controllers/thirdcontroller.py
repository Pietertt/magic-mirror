
import time
import tkinter as tk
import threading

from models.timemodel import TimeModel
from models.internetmodel import InternetModel
from models.framemodel import FrameModel

from .controller import Controller

class ThirdController(Controller):

    def __init__(self, view, tk):
        Controller.__init__(self, view, tk)

        self.timemodel = TimeModel()
        self.internetmodel = InternetModel()
        self.framemodel = FrameModel()

        self.internet_timer = time.time()
        self.time_timer = time.time()
        self.speed_timer = time.time()

        x = threading.Thread(target = self.internetmodel.execute_speed_test)
        x.start()

        self.view.update_item(self.view.temperature, self.framemodel.get_temperature())
        self.view.update_item(self.view.time, self.timemodel.get_current_time())
        self.view.update_item(self.view.date, self.timemodel.get_current_date())
        self.view.update_item(self.view.seconds, self.timemodel.get_current_second())
        self.view.update_item(self.view.download_text, self.internetmodel.download_speed)
        self.view.update_item(self.view.upload_text, self.internetmodel.upload_speed)
        self.view.update_item(self.view.ping_text, self.internetmodel.ping)
        self.view.update_item(self.view.internet, self.internetmodel.get_wifi_name())
        self.view.update_item(self.view.ip_text, self.internetmodel.get_ip_address())
        self.view.update_item(self.view.disk_text, self.internetmodel.get_available_disk_space() + " GB / " + self.internetmodel.get_total_disk_space() + " GB")
        self.view.update_item(self.view.ram_text, self.internetmodel.get_used_ram() + " MB / " + self.internetmodel.get_total_ram() + " MB")



    def execute(self, data):
        print(data)

        if((data[3] < 150) and (data[4] < 100)):
            self.internetmodel.shutdown()

        if((data[2] < 150) and (data[4] < 100)):
            self.internetmodel.restart()


        if((time.time() - self.time_timer) >= 1):
            # Update the view 
            self.view.update_item(self.view.time, self.timemodel.get_current_time())
            self.view.update_item(self.view.date, self.timemodel.get_current_date())
            self.view.update_item(self.view.seconds, self.timemodel.get_current_second())

            self.view.update_item(self.view.download_text, self.internetmodel.download_speed)
            self.view.update_item(self.view.upload_text, self.internetmodel.upload_speed)
            self.view.update_item(self.view.ping_text, self.internetmodel.ping)

            self.view.update_item(self.view.disk_text, self.internetmodel.get_available_disk_space() + " GB / " + self.internetmodel.get_total_disk_space() + " GB")
            self.view.update_item(self.view.ram_text, self.internetmodel.get_used_ram() + " MB / " + self.internetmodel.get_total_ram() + " MB")
            
            self.time_timer = time.time()

        if((time.time() - self.internet_timer) >= 5):
            #self.internetmodel.execute_speed_test()
            self.internet_timer = time.time()

            self.view.update_item(self.view.temperature, self.framemodel.get_temperature())

            try:
                self.view.update_item(self.view.internet, self.internetmodel.get_wifi_name())
                # self.view.update_item(self.view.download_text, self.internetmodel.download_speed)
                # self.view.update_item(self.view.upload_text, self.internetmodel.upload_speed)
                # self.view.update_item(self.view.ping_text, self.internetmodel.ping)
                self.view.update_item(self.view.ip_text, self.internetmodel.get_ip_address())

            except AttributeError:
                print("Oops")

        if((time.time() - self.speed_timer) >= 300):
            x = threading.Thread(target = self.internetmodel.execute_speed_test)
            x.start()

            self.speed_timer = time.time()