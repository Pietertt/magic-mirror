import time
import os
import subprocess

class InternetModel:
    def __init__(self):
        self.upload_speed = 999
        self.download_speed = 999
        self.ping = 999

    def get_ip_address(self):
        ip = subprocess.check_output("hostname -I | grep -Eo '^[^ ]+'", shell=True)
        stripped = ip.rstrip()
        return stripped.decode('utf-8')

    def get_wifi_name(self):
        try:
            hostname = subprocess.check_output("iwgetid -r", shell=True)
            stripped = hostname.rstrip()
            return stripped.decode('utf-8')
        except subprocess.CalledProcessError:
            return "Unknown"

    def get_available_disk_space(self):
        disk_space = subprocess.check_output('df | awk \'$1 == "/dev/root" { print $4 }\'', shell=True)
        stripped = disk_space.rstrip()
        decoded = stripped.decode('utf-8')

        value = round((int(decoded) / 1000000), 2)
        
        return str(value)

    def get_total_ram(self):
        ram = subprocess.check_output('free -m | awk \'$1 == "Mem:" { print $2 }\'', shell=True)
        stripped = ram.rstrip()
        decoded = stripped.decode('utf-8')

        value = round((int(decoded)), 2)
        
        return str(value)

    def get_used_ram(self):
        ram = subprocess.check_output('free -m | awk \'$1 == "Mem:" { print $3 }\'', shell=True)
        stripped = ram.rstrip()
        decoded = stripped.decode('utf-8')

        value = round((int(decoded)), 2)
        
        return str(value)

    def shutdown(self):
        subprocess.Popen(["shutdown", "now"])

    def restart(self):
        subprocess.Popen(["reboot", "now"])


    def get_total_disk_space(self):
        disk_space = subprocess.check_output('df | awk \'$1 == "/dev/root" { print $2 }\'', shell=True)
        stripped = disk_space.rstrip()
        decoded = stripped.decode('utf-8')

        value = round((int(decoded) / 1000000), 2)
        
        return str(value)


    def execute_speed_test(self):
        data = subprocess.check_output('speedtest --simple', shell=True).decode("utf-8")

        output = []

        splitted = data.split()
        for split in splitted:
            output.append(split)
        
        try:
            self.upload_speed = output[7]
            self.download_speed = output[4]
            self.ping = output[1]
        except IndexError:
            print("Index error")


    