import tkinter as tk
import time
from tkinter import ttk

from threading import Thread

from controllers.maincontroller import MainController

from views.mainview import MainView
from views.secondview import SecondView

from models.timemodel import TimeModel
from models.framemodel import FrameModel
from models.spotifymodel import SpotifyModel

class Main(tk.Tk):
    
    cooldown = False
    COOLDOWN_TIME = 1500

    DOT_2_SENSOR = 0
    DOT_1_SENSOR = 1
    NEXT_SENSOR = 2
    PREVIOUS_SENSOR = 3
    LINE_SENSOR = 4

    spotify_timer = time.time()
    spotify_second_timer = time.time()
    time_timer = time.time()

    def __init__(self):
        super().__init__()
        self.frame = tk.Frame()
        self.title("Magic Mirror")

        self.wm_attributes('-type', 'splash')

        self.frame.config(bg = "black", width = 1016, height = 1856)
        self.frame.pack()

        self.timemodel = TimeModel()
        self.framemodel = FrameModel()
        self.spotifymodel = SpotifyModel()

        self.view = MainView(self.frame)
        self.view.render()

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
            self.update()
            data = self.framemodel.read_serial()
            if data:
                print(data)

                # Dot 1
                if(data[self.DOT_1_SENSOR] < 300):
                    if(self.cooldown == False):
                        self.set_cooldown()
                        self.view.grayscale(self.view.dot1, "dot.png")
                        self.after(self.COOLDOWN_TIME, lambda: self.view.white(self.view.dot1, "dot.png"))
                        self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())

                # Dot 2
                if(data[self.DOT_2_SENSOR] < 300):
                    if(self.cooldown == False):
                        self.set_cooldown()
                        self.view.grayscale(self.view.dot3, "dot.png")
                        self.after(self.COOLDOWN_TIME, lambda: self.view.white(self.view.dot3, "dot.png"))
                        self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())

                # Previous
                if((data[self.PREVIOUS_SENSOR] < 400) and (data[self.LINE_SENSOR] < 600)):
                    if(self.cooldown == False):
                        #self.set_cooldown()
                        #self.spotifymodel.skip_to_previous_track()
                        #self.update_spotify_data()
                        #self.view.grayscale(self.view.previous, "previous.png")
                        #self.after(self.COOLDOWN_TIME, lambda: self.view.white(self.view.previous, "previous.png"))
                        #self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())
                        pass
                
                # Next
                if((data[self.NEXT_SENSOR] < 400) and (data[self.LINE_SENSOR] < 600)):
                    if(self.cooldown == False):
                        #self.set_cooldown()
                        #self.spotifymodel.skip_to_next_track()
                        #self.update_spotify_data()
                        #self.view.grayscale(self.view.next, "next.png")
                        #self.after(self.COOLDOWN_TIME, lambda: self.view.white(self.view.next, "next.png"))
                        #self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())
                        pass

            if((time.time() - self.spotify_timer) >= 5):
                self.update_spotify_data()
                self.view.current_time.set(self.spotifymodel.convert_to_readable(self.spotifymodel.print_update_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))
                self.view.temperature.set(self.framemodel.get_temperature())
                self.spotify_timer = time.time()

            if((time.time() - self.time_timer) >= 1):

                # Update the view 
                self.view.seconds.set(self.timemodel.get_current_second())
                self.view.time.set(self.timemodel.get_current_time())
                self.view.date.set(self.timemodel.get_current_date())

                # Update the spotify timer with +1
                self.spotifymodel.update_progress(self.spotifymodel.print_update_progress() + 1)

                # Update the view
                self.view.current_time.set(self.spotifymodel.convert_to_readable(self.spotifymodel.print_update_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))

                self.time_timer = time.time()
        

    def update_spotify_data(self):
        self.spotifymodel.get_current_track()
        self.view.current_track.set(self.spotifymodel.get_current_track_title())
        self.view.current_artist.set(self.spotifymodel.get_current_track_artists()[0])
        self.view.current_device.set(self.spotifymodel.get_devices_name()[0])
        self.view.current_time.set(str(self.spotifymodel.get_current_track_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))

    def set_cooldown(self):
        self.cooldown = True

    def reset_cooldown(self):
        self.cooldown = False

if __name__ == "__main__":
    main = Main()
    main.loop()