import tkinter as tk
import time
from tkinter import ttk

import threading

from controllers.controller import Controller

from views.mainview import MainView
from views.secondview import SecondView

from models.timemodel import TimeModel
from models.framemodel import FrameModel
from models.spotifymodel import SpotifyModel

class Main(tk.Tk):
    previous_timer_1 = time.time()
    previous_timer_2 = time.time()

    next_timer_1 = time.time()
    next_timer_2 = time.time()

    add_to_coffee_playlist_timer_1 = time.time()
    add_to_coffee_playlist_timer_2 = time.time()

    time_timer = time.time()
    temperature_timer = time.time()
    spotify_timer = time.time()
    current_track_timer = time.time()

    first_view_timer_1 = time.time()
    first_view_timer_2 = time.time()

    previous_boolean = False
    next_boolean = False
    add_coffee_boolean = False

    current_view = "main_view"

    main_view_created = True
    second_view_created = False

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

        frame_thread = threading.Thread(target = self.loop)
        frame_thread.start()

        self.update()
        self.geometry(str(1016) + "x" + str(1856) + "+0+0")

        self.mainloop()

    def loop(self):
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
        #     if(self.current_view == "main_view"):

            # Make the previous number white again
            # if((time.time() - self.previous_timer_2) >= 1.5):
            #     if(self.previous_boolean == True):
            #         self.view.white(self.view.previous, "previous.png")
            #         self.previous_boolean = False
            #         self.previous_timer_2 = time.time()
            
            # if((time.time() - self.next_timer_2) >= 1.5):
            #     if(self.next_boolean == True):
            #         self.view.white(self.view.next, "next.png")
            #         self.next_boolean = False
            #         self.next_timer_2 = time.time()

            # if((time.time() - self.add_to_coffee_playlist_timer_2) >= 1.5):
            #     if(self.add_coffee_boolean == True):
            #         self.view.white(self.view.coffee, "coffee.png")
            #         self.add_coffee_boolean = False
            #         self.add_to_coffee_playlist_timer_2 = time.time()

            # if((time.time() - self.temperature_timer) >= 5):
            #     # Get the most recent temperature from the model
            #     self.view.temperature.set(self.framemodel.get_temperature())

            #     # Reset the timer to zero
            #     self.temperature_timer = time.time()

            # # Update the time every second
            # if((time.time() - self.time_timer) >= 1):
            #     self.view.seconds.set(self.timemodel.get_current_second())
            #     self.view.time.set(self.timemodel.get_current_time())
            #     self.view.date.set(self.timemodel.get_current_date())

            #     self.time_timer = time.time()

            # # Refresh the Spotify data every 5 seconds
            # if((time.time() - self.spotify_timer) >= 5):
            #     self.update_spotify_data()

            # # Update the progress timer 
            # else: 
            #     if(time.time() - self.current_track_timer) >= 1:
            #         if(self.spotifymodel.track_paused == False):
            #             # Update the timer with +1
            #             self.spotifymodel.update_progress(self.spotifymodel.print_update_progress() + 1)
            #             # Set the progress timer
            #             self.view.current_time.set(self.spotifymodel.convert_to_readable(self.spotifymodel.print_update_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))

            #         self.current_track_timer = time.time()

            data = self.framemodel.read_serial()
            if data:
                print(data)
                # # Previous button
                # if((data[3] < 250) and (data[4] < 250)):
                #     if((time.time() - self.previous_timer_1) >= 1.5):

                #         # Grayscale the button
                #         self.view.grayscale(self.view.previous, "previous.png")

                #         # Previous can only be called every 1.5 second
                #         self.previous_timer_1 = time.time()

                #         # A timer for making the previous button white again
                #         self.previous_timer_2 = time.time()
                #         self.spotifymodel.skip_to_previous_track()
                #         self.update_spotify_data()

                #         self.previous_boolean = True
                
                # if((data[2] < 250) and (data[4] < 250)):
                #     if((time.time() - self.next_timer_1) >= 1.5):
                #     # Grayscale the button
                #         self.view.grayscale(self.view.next, "next.png")

                #         # Next can only be called every 1.5 second
                #         self.next_timer_1 = time.time()

                #         # A timer for making the next button white again
                #         self.next_timer_2 = time.time()
                #         self.spotifymodel.skip_to_next_track()
                #         self.update_spotify_data()

                #         self.next_boolean = True

                # if((data[4] < 250) and (data[3] > 250) and (data[2] > 250)):
                #     if((time.time() - self.add_to_coffee_playlist_timer_1) >= 1.5):
                #         pass

                            #self.view.grayscale(self.view.coffee, "coffee.png")

                            
                            #self.spotifymodel.add_to_coffee_playlist()
                            #self.add_to_coffee_playlist_timer_1 = time.time()

                            #self.add_to_coffee_playlist_timer_2 = time.time()

                            #self.add_coffee_boolean = True

                    # if(data[1] < 250):
                    #         self.view.move_all_widgets()
                    #     # self.view.remove_all_widgets()
                    #     # self.view = MainView(self.frame)
                    #     # self.view.render()
                    #     # self.current_view = "main_view"

                    # if(data[0] < 250):
                    #     self.view.move_all_widgets()
                    #     # self.view.remove_all_widgets()
                    #     # self.view = SecondView(self.frame)
                    #     # self.view.render()
                    #     # self.current_view = "second_view"

            # if(self.current_view == "second_view"):
            #     # Update the time every second
            #     if((time.time() - self.time_timer) >= 1):
            #         self.view.seconds.set(self.timemodel.get_current_second())
            #         self.view.time.set(self.timemodel.get_current_time())
            #         self.view.date.set(self.timemodel.get_current_date())

            #         self.time_timer = time.time()

            #     data = self.framemodel.read_serial()
            #     if data:
            #         print(data)

            #         if(data[1] < 250):
            #             self.view.move_all_widgets()
            #             # self.view.remove_all_widgets()
            #             # self.view = MainView(self.frame)
            #             # self.view.render()
            #             # self.current_view = "main_view"

            #         if(data[0] < 250):
            #             self.view.move_all_widgets()
            #             # self.view.remove_all_widgets()
            #             # self.view = SecondView(self.frame)
            #             # self.view.render()
            #             # self.current_view = "second_view"

        

    def update_spotify_data(self):
        self.spotifymodel.get_current_track()
        self.view.current_track.set(self.spotifymodel.get_current_track_title())
        self.view.current_artist.set(self.spotifymodel.get_current_track_artists()[0])
        self.view.current_device.set(self.spotifymodel.get_devices_name()[0])
        self.view.current_time.set(str(self.spotifymodel.get_current_track_progress()) + " / " + str(self.spotifymodel.get_current_track_duration()))

if __name__ == "__main__":
    main = Main()
    main.run()