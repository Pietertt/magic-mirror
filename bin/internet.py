import os
import time

while True:
    time.sleep(300)
    print("Performing internet speed...")
    os.system("speedtest --simple > speed.txt")