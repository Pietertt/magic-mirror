import time
import Adafruit_DHT

class TimeModel:
    def __init__(self):
        self.days = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag"]
        self.months = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]
        self.sensor = Adafruit_DHT.DHT11

    def get_current_second(self):
        t = time.time()
        local = str(time.localtime(t).tm_sec)
        if(len(local) == 1):
            local = "0" + local

        return local

    def get_current_date(self):
        t = time.time()
        local = time.localtime(t)
        return self.days[local.tm_wday] + ", " + str(local.tm_mday) + " " + self.months[local.tm_mon - 1] + " " + str(local.tm_year)

    def get_current_time(self):
        t = time.time()
        local = time.localtime(t)
        hour = str(local.tm_hour)
        minute = str(local.tm_min)

        if(len(hour) == 1):
            hour = "0" + hour

        if(len(minute) == 1):
            minute = "0" + minute

        return hour + ":" + minute

    def get_temperature(self):
        humidity, temperature = Adafruit_DHT.read(self.sensor, 4)
        return temperature