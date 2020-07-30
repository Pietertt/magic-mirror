
import time
import tkinter as tk

from models.timemodel import TimeModel
from models.framemodel import FrameModel
from models.spotifymodel import SpotifyModel

from views.mainview import MainView

from .controller import Controller

class MainController(Controller):
    NEXT_SENSOR = 2
    PREVIOUS_SENSOR = 3
    LINE_SENSOR = 4

    def __init__(self, view, tk):
        Controller.__init__(self, view, tk)
        self.timemodel = TimeModel()
        self.spotifymodel = SpotifyModel()

        self.spotify_timer = time.time()
        self.time_timer = time.time()

        self.spotifymodel.get_current_track()
        self.spotifymodel.get_device()

        self.view.update_item(self.view.current_track, self.spotifymodel.get_current_track_title())
        self.view.update_item(self.view.current_artist, self.spotifymodel.get_current_track_artists()[0])
        self.view.update_item(self.view.current_device, self.spotifymodel.get_devices_name()[0])
        self.view.update_item(self.view.current_time, str(self.spotifymodel.get_current_track_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))
        
    def execute(self, data):
        print(data)

        # Previous
        if((data[self.PREVIOUS_SENSOR] < 200) and (data[self.LINE_SENSOR] < 200)):
            if(self.cooldown == False):
                self.set_cooldown()
                self.spotifymodel.skip_to_previous_track()
                self.update_spotify_data()
                self.view.disable_previous_button()
                self.tk.after(self.COOLDOWN_TIME, lambda: self.view.enable_previous_button())
                self.tk.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())
        
        # Next
        if((data[self.NEXT_SENSOR] < 250) and (data[self.LINE_SENSOR] < 250)):
            if(self.cooldown == False):
                self.set_cooldown()
                self.spotifymodel.skip_to_next_track()
                self.update_spotify_data()
                self.view.disable_next_button()
                self.tk.after(self.COOLDOWN_TIME, lambda: self.view.enable_next_button())
                self.tk.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())

        
        if((time.time() - self.spotify_timer) >= 5):
        
            self.update_spotify_data()
            self.view.update_item(self.view.current_time, str(self.spotifymodel.get_current_track_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))
                                
            self.spotify_timer = time.time()

        if((time.time() - self.time_timer) >= 1):
            
            # Update the spotify timer with +1
            self.spotifymodel.update_progress(self.spotifymodel.print_update_progress() + 1)

            # Update the view
            self.view.update_item(self.view.current_time, str(self.spotifymodel.convert_to_readable(self.spotifymodel.print_update_progress())) + " / " + str(self.spotifymodel.get_current_track_duration()))
                
            #     # Update the view 
            self.view.update_item(self.view.time, self.timemodel.get_current_time())
            self.view.update_item(self.view.date, self.timemodel.get_current_date())
            self.view.update_item(self.view.seconds, self.timemodel.get_current_second())
            
            self.time_timer = time.time()

    def update_spotify_data(self):
        self.spotifymodel.get_current_track()
        self.view.update_item(self.view.current_track, self.spotifymodel.get_current_track_title())
        self.view.update_item(self.view.current_artist, self.spotifymodel.get_current_track_artists()[0])
        self.view.update_item(self.view.current_device, self.spotifymodel.get_devices_name()[0])
        self.view.update_item(self.view.current_time, str(self.spotifymodel.get_current_track_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))

    def set_cooldown(self):
        self.cooldown = True

    def reset_cooldown(self):
        self.cooldown = False