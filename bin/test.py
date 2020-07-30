import os
import time

while True:
    os.system("speedtest --simple > test.txt")
    time.sleep(60)