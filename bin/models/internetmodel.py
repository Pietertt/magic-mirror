import time
import os

class InternetModel:
    def __init__(self):
        pass

    def execute_speed_test(self):
        os.system("speedtest --simple")
        print("Speed test executed")