import serial
import json

class FrameModel:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.flush()

        self.temperature = None

    def read_serial(self):
        if self.ser.in_waiting > 0:
            try:
                line = self.ser.readline().decode('utf-8').rstrip()
                if len(line) > 0:
                    if(line[0] == "{"):
                        try:
                            data = json.loads(line)
                            try:
                                temperature = str(data["temperature"])
                                if(len(temperature) == 4):
                                    self.temperature = temperature + "0" + "\N{DEGREE SIGN}"
                                else:
                                    self.temperature = temperature + "\N{DEGREE SIGN}"
                            except KeyError:
                                print("Wrong format")

                            return data["data"]
                        except ValueError:
                            print("Wrong format")
                        except UnicodeDecodeError:
                            print("Unicode error")
            except ValueError:
                print("Unicode error")

    def get_temperature(self):
        return self.temperature