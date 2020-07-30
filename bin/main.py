import tkinter as tk
import time

from threading import Thread

from controllers.maincontroller import MainController
from controllers.secondcontroller import SecondController

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

    
    time_timer = time.time()
    internet_timer = time.time()

    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, width = 1016, height = 1856, bg = "black")
        self.canvas.pack()
        self.title("Magic Mirror")

        self.wm_attributes('-type', 'splash')

        self.timemodel = TimeModel()
        self.framemodel = FrameModel()
        self.spotifymodel = SpotifyModel()

        self.view = MainView(self.canvas)
        self.view.render()

        self.controller = MainController(self.view, self)

        self.view.update_item(self.view.temperature, self.framemodel.get_temperature())
        self.view.update_item(self.view.seconds, self.timemodel.get_current_second())
        self.view.update_item(self.view.time, self.timemodel.get_current_time())
        self.view.update_item(self.view.date, self.timemodel.get_current_date())


        while True:
            self.update()
            data = self.framemodel.read_serial()
            if data:

                # Dot 1
                if(data[self.DOT_1_SENSOR] < 250):
                    if(self.cooldown == False):
                        self.set_cooldown()
                        self.view.disable_dot1_button()
                        self.after(self.COOLDOWN_TIME, lambda: self.view.enable_dot1_button())
                        self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())

                        self.view.clear_canvas()
                        self.view = MainView(self.canvas)
                        self.view.render()

                        self.controller = MainController(self.view, self)

                # Dot 2
                if(data[self.DOT_2_SENSOR] < 250):
                    if(self.cooldown == False):
                        self.set_cooldown()
                        self.view.disable_dot3_button()
                        self.after(self.COOLDOWN_TIME, lambda: self.view.enable_dot3_button())
                        self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())
                        
                        self.view.clear_canvas()
                        self.view = SecondView(self.canvas)
                        self.view.render()

                        self.controller = SecondController(self.view, self)

                self.controller.execute(data)

            #     if(self.current_view == "mainview"):
            #         # Previous
            #         if((data[self.PREVIOUS_SENSOR] < 200) and (data[self.LINE_SENSOR] < 200)):
            #             if(self.cooldown == False):
            #                 self.set_cooldown()
            #                 self.spotifymodel.skip_to_previous_track()
            #                 self.update_spotify_data()
            #                 self.view.disable_previous_button()
            #                 self.after(self.COOLDOWN_TIME, lambda: self.view.enable_previous_button())
            #                 self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())
                    
            #         # Next
            #         if((data[self.NEXT_SENSOR] < 250) and (data[self.LINE_SENSOR] < 250)):
            #             if(self.cooldown == False):
            #                 self.set_cooldown()
            #                 self.spotifymodel.skip_to_next_track()
            #                 self.update_spotify_data()
            #                 self.view.disable_next_button()
            #                 self.after(self.COOLDOWN_TIME, lambda: self.view.enable_next_button())
            #                 self.after(self.COOLDOWN_TIME, lambda: self.reset_cooldown())

            # if((time.time() - self.spotify_timer) >= 5):
            #     if(self.current_view == "mainview"):
            #         self.update_spotify_data()
            #         self.view.update_item(self.view.current_time, str(self.spotifymodel.get_current_track_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))
                
            #     self.view.update_item(self.view.temperature, self.framemodel.get_temperature())
                
            #     self.spotify_timer = time.time()
            #     pass

            # if(self.current_view == "secondview"):
            #     if((time.time() - self.internet_timer) >= 60):
            #         self.view.update_item(self.view.download, "60 Mbps")

            # if((time.time() - self.time_timer) >= 1):
            #     if(self.current_view == "mainview"):
            #         # Update the spotify timer with +1
            #         self.spotifymodel.update_progress(self.spotifymodel.print_update_progress() + 1)

            #         # Update the view
            #         self.view.update_item(self.view.current_time, str(self.spotifymodel.convert_to_readable(self.spotifymodel.print_update_progress())) + " / " + str(self.spotifymodel.get_current_track_duration()))
                
            #     # Update the view 
            #     self.view.update_item(self.view.time, self.timemodel.get_current_time())
            #     self.view.update_item(self.view.date, self.timemodel.get_current_date())
            #     self.view.update_item(self.view.seconds, self.timemodel.get_current_second())
                
            #     self.time_timer = time.time()
        

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

if __name__ == "__main__":
    main = Main()
    main.loop()