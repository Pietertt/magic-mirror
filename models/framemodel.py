import serial
import json

class FrameModel:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.flush()

    def read_serial(self):
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()
            if len(line) > 0:
                if(line[0] == "{"):
                    data = json.loads(line)
                    print(data["data"][0])
                    return line
        
        return ""