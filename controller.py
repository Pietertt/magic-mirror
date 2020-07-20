import threading
import time
import tkinter
from tkinter import messagebox as mb

from models.timemodel import TimeModel
from models.framemodel import FrameModel
from models.spotifymodel import SpotifyModel

from view import View

class Controller:
    def __init__(self):
        self.timemodel = TimeModel()
        self.framemodel = FrameModel()
        self.spotifymodel = SpotifyModel()
        self.view = View(self)

    def main(self):
        time_thread = threading.Thread(target = self.time_handler)
        time_thread.start()

        # temperature_thread = threading.Thread(target = self.temperature_handler)
        # temperature_thread.start()

        frame_thread = threading.Thread(target = self.frame_handler)
        frame_thread.start()

        spotify_thread = threading.Thread(target = self.spotify_handler)
        spotify_thread.start()

        self.view.main()

    def time_handler(self):
        self.view.seconds.set(self.timemodel.get_current_second())
        self.view.time.set(self.timemodel.get_current_time())
        self.view.date.set(self.timemodel.get_current_date())

        t = time.time()
        while True:
            if(time.time() - t >= 1):
                self.view.seconds.set(self.timemodel.get_current_second())
                self.view.time.set(self.timemodel.get_current_time())
                self.view.date.set(self.timemodel.get_current_date())

                t = time.time()

    def temperature_handler(self):
        self.view.temperature.set(self.sensormodel.get_temperature())

        t = time.time()
        while True:
            if(time.time() - t >= 5):
                self.view.temperature.set(self.sensormodel.get_temperature())
                t = time.time()

            if((time.time() - t >= 0) and (time.time() - t <= 0.5)):
                self.sensormodel.set_led(1)

            if((time.time() - t >= 0.5) and (time.time() - t <= 1)):
                self.sensormodel.set_led(0)

            t = time.time()

    def frame_handler(self):
        t = time.time()
        
        while True:
            data = self.framemodel.read_serial()
            if data:

                if((data[1] == 0) and (data[2] == 0)):
                    print("Next track")
                elif((data[1] == 0) and (data[3] == 0)):
                    print("Liked")
                    # self.spotifymodel.skip_to_next_track()
                    # self.spotifymodel.get_current_track()
                    # self.spotifymodel.get_device()

                    # self.view.current_track.set(self.spotifymodel.get_current_track_title())
                    # self.view.current_artist.set(self.spotifymodel.get_current_track_artists()[0])
                    # self.view.current_device.set(self.spotifymodel.get_devices_name()[0])
                    # self.view.current_time.set(str(self.spotifymodel.get_current_track_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))


            
            if(time.time() - t) >= 5:
                self.view.temperature.set(self.framemodel.get_temperature())
                t = time.time()
    
                # if(data[0] == 0):
                #     mb.showinfo("Test", "Test")

    def spotify_handler(self):
        self.spotifymodel.get_current_track()
        self.spotifymodel.get_device()

        self.view.current_track.set(self.spotifymodel.get_current_track_title())
        self.view.current_artist.set(self.spotifymodel.get_current_track_artists()[0])
        self.view.current_device.set(self.spotifymodel.get_devices_name()[0])
        self.view.current_time.set(str(self.spotifymodel.get_current_track_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))


        t = time.time()
        a = time.time()

        while True:
            if((time.time() - t) >= 5):
                self.spotifymodel.get_current_track()
                self.view.current_track.set(self.spotifymodel.get_current_track_title())
                self.view.current_artist.set(self.spotifymodel.get_current_track_artists()[0])
                self.view.current_device.set(self.spotifymodel.get_devices_name()[0])
                self.view.current_time.set(str(self.spotifymodel.get_current_track_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))
            
                t = time.time()
                a = time.time()
            else: # smaller than 5
                if(time.time() - a) >= 1:
                    self.spotifymodel.update_progress(self.spotifymodel.print_update_progress() + 1)
                    self.view.current_time.set(self.spotifymodel.convert_to_readable(self.spotifymodel.print_update_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))

                    a = time.time()

if __name__ == '__main__':
    calculator = Controller()
    calculator.main()


# if __name__ == '__main__':
#     s = SpotifyModel()
#     s.get_current_track()
#     s.get_device()

#     s.skip_to_next_track()

#     print(s.get_current_track_title())
#     print(s.get_current_track_ms())
#     print(s.get_current_track_duration_ms())
#     print(s.get_current_track_artists())
#     print(s.get_current_track_album())
#     print(s.get_devices_name())