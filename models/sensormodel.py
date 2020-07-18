import Adafruit_DHT
import wiringpi as GPIO

import time

class SensorModel:
    SENSOR = 4
    previous_value = None

    def __init__(self):
        GPIO.wiringPiSetupGpio() 
        GPIO.pinMode(17, 1) 

    def get_temperature(self):
        humidity, temperature = Adafruit_DHT.read(Adafruit_DHT.DHT11, self.SENSOR)
        if(temperature is None):
            return str(self.previous_value) + "\N{DEGREE SIGN}"
        else:
            self.previous_value = temperature
            return str(temperature) + "\N{DEGREE SIGN}"

    def set_led(self, value):
        GPIO.digitalWrite(17, value)