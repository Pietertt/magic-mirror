import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from pprint import pprint

import time
import os
import json

class SpotifyModel:
    USERNAME = 'drjzrg9lstsquvizucpgl8knp' 
    CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
    REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
    SCOPE = 'user-read-currently-playing, user-read-playback-state,user-modify-playback-state, app-remote-control, playlist-modify' 

    allow_skip = time.time()
    allow_pause = time.time()
    current_track_progress = 0

    track_paused = False

    def __init__(self):
        self.token = util.prompt_for_user_token(username = self.USERNAME, scope = self.SCOPE, client_id = self.CLIENT_ID, client_secret = self.CLIENT_SECRET, redirect_uri = self.REDIRECT_URI)
        self.sp = spotipy.Spotify(auth = self.token)

    def get_current_track(self):
        self.current_track = self.sp.current_user_playing_track()

    def get_current_track_uri(self):
        uri = self.current_track["item"]["uri"]
        return uri.split(":")[2]

    def get_current_track_title(self):
        return self.current_track["item"]["name"]

    def get_current_track_progress(self):
        time =  int(self.current_track["progress_ms"] / 1000)
        self.current_track_progress = time
       
        return self.convert_to_readable(time)

    def get_current_track_duration(self):
        time = int(self.current_track["item"]["duration_ms"] / 1000)
        
        return self.convert_to_readable(time)

    def get_current_track_artists(self):
        returns = []
        arists = self.current_track["item"]["artists"]
        for artist in arists:
            returns.append(artist["name"])
        
        return returns

    def get_current_track_album(self):
        return self.current_track["item"]["album"]["name"]

    def add_to_coffee_playlist(self):
        self.sp.user_playlist_add_tracks(self.get_user_id(), "7jePUsA2BijbH2h7kXBSvD", [self.get_current_track_uri()])

    def get_user_id(self):
        user = self.sp.current_user()
        return user["id"]

    def get_device(self):
        self.devices = self.sp.devices()["devices"]

    def get_devices_name(self):
        devices = []
        for device in self.devices:
            devices.append(device["name"])
        
        return devices

    def skip_to_next_track(self):
        self.sp.next_track()

    def skip_to_previous_track(self):
        self.sp.previous_track()

    def pause_current_track(self):
        if((time.time() - self.allow_pause) > 1):
            if(self.track_paused == True):
                self.sp.start_playback()
                self.allow_pause = time.time()
                self.track_paused = False
            else:
                self.sp.pause_playback()
                self.allow_pause = time.time()
                self.track_paused = True


    def convert_to_readable(self, ms):
        minutes = str(int(ms / 60))
        seconds = str(ms % 60)

        if(len(seconds) == 1):
            seconds = "0" + seconds

        return minutes + ":" + seconds

    def update_progress(self, value):
        self.current_track_progress = value

    def print_update_progress(self):
        return self.current_track_progress