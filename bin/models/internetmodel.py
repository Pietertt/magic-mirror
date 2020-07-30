import time
import os

class InternetModel:
    def __init__(self):
        upload_speed = None
        download_speed = None
        ping = None

    def get_ip_address(self):
        ip = os.system("hostname -I | cut -d' ' -f1 > ip.txt")
        file = open("/home/pi/Desktop/magic-mirror/bin/ip.txt", "r")
        return file.read().rstrip("\n")

    def get_wifi_name(self):
        ip = os.system("iwgetid -r > wifi.txt")
        file = open("/home/pi/Desktop/magic-mirror/bin/wifi.txt", "r")
        return file.read().rstrip("\n")


    def execute_speed_test(self):
        file = open("/home/pi/Desktop/magic-mirror/bin/speed.txt", "r")
        lines = file.readlines() 

        output = []

        for line in lines:
            splitted = line.split()
            for split in splitted:
                output.append(split)
        
        try:
            self.upload_speed = output[7]
            self.download_speed = output[4]
            self.ping = output[1]
        except IndexError:
            print("Index error")


    