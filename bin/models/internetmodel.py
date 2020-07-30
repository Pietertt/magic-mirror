import time
import os
import subprocess

class InternetModel:
    def __init__(self):
        upload_speed = None
        download_speed = None
        ping = None

    def get_ip_address(self):
        #ip = os.system("hostname -I | cut -d' ' -f1 > ip.txt")
        #file = open("/home/pi/Desktop/magic-mirror/bin/ip.txt", "r")
        

        ip = subprocess.check_output("hostname -I | grep -Eo '^[^ ]+'", shell=True)
        stripped = ip.rstrip()
        return stripped.decode('utf-8')

    def get_wifi_name(self):
        hostname = subprocess.check_output("iwgetid -r", shell=True)
        stripped = hostname.rstrip()
        return stripped.decode('utf-8')


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


    