import os
import time

while True:
    os.system("speedtest --simple > speed.txt")
    time.sleep(60)