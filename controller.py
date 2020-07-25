import threading
import time
import tkinter
from tkinter import messagebox as mb

from models.timemodel import TimeModel
from models.framemodel import FrameModel
from models.spotifymodel import SpotifyModel

from view import View

class Controller:
    previous_timer_1 = time.time()
    previous_timer_2 = time.time()

    time_timer = time.time()
    temperature_timer = time.time()
    spotify_timer = time.time()
    current_track_timer = time.time()

    def __init__(self):
        self.timemodel = TimeModel()
        self.framemodel = FrameModel()
        self.spotifymodel = SpotifyModel()
        self.view = View(self)

    def main(self):
        # time_thread = threading.Thread(target = self.time_handler)
        # time_thread.start()

        # temperature_thread = threading.Thread(target = self.temperature_handler)
        # temperature_thread.start()

        frame_thread = threading.Thread(target = self.frame_handler)
        frame_thread.start()

        # spotify_thread = threading.Thread(target = self.spotify_handler)
        # spotify_thread.start()

        self.view.main()

    def frame_handler(self):
        t = time.time()

        self.view.seconds.set(self.timemodel.get_current_second())
        self.view.time.set(self.timemodel.get_current_time())
        self.view.date.set(self.timemodel.get_current_date())

        self.spotifymodel.get_current_track()
        self.spotifymodel.get_device()

        self.view.current_track.set(self.spotifymodel.get_current_track_title())
        self.view.current_artist.set(self.spotifymodel.get_current_track_artists()[0])
        self.view.current_device.set(self.spotifymodel.get_devices_name()[0])
        self.view.current_time.set(str(self.spotifymodel.get_current_track_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))
        
        while True:
            data = self.framemodel.read_serial()
            if data:

                # Previous button
                if((data[3] < 500) and (data[4] < 500)):
                    if((time.time() - self.previous_timer_1) >= 2):
                        self.view.test()
                        self.previous_timer_1 = time.time()
                        self.previous_timer_2 = time.time()
                        self.spotifymodel.skip_to_previous_track()
                        self.update_spotify_data()

                if((time.time() - self.temperature_timer) >= 5):
                    self.view.temperature.set(self.framemodel.get_temperature())
                    self.temperature_timer = time.time()

            # Make the previous number white again
            if((time.time() - self.previous_timer_2) >= 1):
                self.view.test1()

            # Update the time every second
            if((time.time() - self.time_timer) >= 1):
                self.view.seconds.set(self.timemodel.get_current_second())
                self.view.time.set(self.timemodel.get_current_time())
                self.view.date.set(self.timemodel.get_current_date())

                self.time_timer = time.time()

            # Refresh the Spotify data every 5 seconds
            if((time.time() - self.spotify_timer) >= 5):
                self.update_spotify_data()
                self.spotify_timer = time.time()
                self.current_track_timer = time.time()

            else: # smaller than 5
                if(time.time() - self.current_track_timer) >= 1:
                    if(self.spotifymodel.track_paused == False):
                        self.spotifymodel.update_progress(self.spotifymodel.print_update_progress() + 1)
                        self.view.current_time.set(self.spotifymodel.convert_to_readable(self.spotifymodel.print_update_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))

                    self.current_track_timer = time.time()

                    

            
                # if((data[3] == 1) and (data[4] == 1)):
                #     self.view.test1()
                # else:
                #     #self.view.test1()
                #     pass
                    #self.spotifymodel.pause_current_track()
                    
                #     self.spotifymodel.get_current_track()
                #     self.spotifymodel.get_device()

                #     self.view.current_track.set(self.spotifymodel.get_current_track_title())
                #     self.view.current_artist.set(self.spotifymodel.get_current_track_artists()[0])
                #     self.view.current_device.set(self.spotifymodel.get_devices_name()[0])
                #     self.view.current_time.set(str(self.spotifymodel.get_current_track_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))


            
    
                # if(data[0] == 0):
                #     mb.showinfo("Test", "Test")

    def update_spotify_data(self):
        self.spotifymodel.get_current_track()
        self.view.current_track.set(self.spotifymodel.get_current_track_title())
        self.view.current_artist.set(self.spotifymodel.get_current_track_artists()[0])
        self.view.current_device.set(self.spotifymodel.get_devices_name()[0])
        self.view.current_time.set(str(self.spotifymodel.get_current_track_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))

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
                    if(self.spotifymodel.track_paused == False):
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