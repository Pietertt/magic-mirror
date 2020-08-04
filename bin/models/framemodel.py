import serial
import json

class FrameModel:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.flush()

        self.temperature = str(20) + ".0" + "\N{DEGREE SIGN}"
        self.light_level = 0

    def read_serial(self):
        if self.ser.in_waiting > 0:
            try:
                line = self.ser.readline().decode('utf-8').rstrip()
                if len(line) > 0:
                    if(line[0] == "{"):
                        try:
                            data = json.loads(line)
                            try:
                                self.light_level = str(data["temperature"])
                            
                            except KeyError:
                                print("Wrong format")
                            
                            d = data["data"]
                            d.append(self.light_level)
                            return d
                        except ValueError:
                            print("Wrong format")
                        except UnicodeDecodeError:
                            print("Unicode error")
            except ValueError:
                print("Unicode error")

    def get_temperature(self):
        return self.temperature

    def get_light_level(self):
        return self.light_level