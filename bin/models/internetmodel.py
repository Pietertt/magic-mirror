import time

class InternetModel:
    def __init__(self):
        upload_speed = None
        download_speed = None
        ping = None

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


    