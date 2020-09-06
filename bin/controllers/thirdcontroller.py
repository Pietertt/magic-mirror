
import time
import tkinter as tk
import threading
from PIL import Image, ImageTk

from models.timemodel import TimeModel
from models.internetmodel import InternetModel
from models.framemodel import FrameModel

from .controller import Controller

class ThirdController(Controller):

    files = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27"]
    i = 0

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

        # file = ImageTk.PhotoImage(file='/home/pi/Desktop/magic-mirror/assets/gif/activity/frame_' + self.files[self.i] + '_delay-0.04s.gif')
        # self.view.canvas.activity = file

        # file = ImageTk.PhotoImage(file='/home/pi/Desktop/magic-mirror/assets/gif/activity/frame_' + self.files[self.i] + '_delay-0.04s.gif')
        # self.view.canvas.activity = file
        # self.view.activity = self.view.canvas.create_image(120, 580, image = file, anchor = "sw")
        
        # self.i = self.i + 1

        # if(self.i >= 27):
        #     self.i = 0

        if((data[3] < 300) and (data[4] < 100)):
            #self.internetmodel.shutdown()
            pass

        if((data[2] < 400) and (data[4] < 100)):
            #self.internetmodel.restart()
            pass

        self.view.update_item(self.view.ir_text, (str(data[0]) + " - " + str(data[1]) + " - " + str(data[2]) + " - " + str(data[3]) + " - " + str(data[4])))
        self.view.update_item(self.view.light_text, (str(data[5]) + " / 1024"))


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
            self.internet_timer = time.time()

            self.view.update_item(self.view.temperature, self.framemodel.get_temperature())

            try:
                self.view.update_item(self.view.internet, self.internetmodel.get_wifi_name())
                self.view.update_item(self.view.ip_text, self.internetmodel.get_ip_address())

            except AttributeError:
                pass

        if((time.time() - self.speed_timer) >= 300):
            x = threading.Thread(target = self.internetmodel.execute_speed_test)
            x.start()

            self.speed_timer = time.time()