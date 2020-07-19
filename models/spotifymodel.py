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
    SCOPE = 'user-read-currently-playing, user-read-playback-state,user-modify-playback-state, app-remote-control' 

    allow_skip = time.time()

    def __init__(self):
        self.token = util.prompt_for_user_token(username = self.USERNAME, scope = self.SCOPE, client_id = self.CLIENT_ID, client_secret = self.CLIENT_SECRET, redirect_uri = self.REDIRECT_URI)
        self.sp = spotipy.Spotify(auth = self.token)

    def get_current_track(self):
        self.current_track = self.sp.current_user_playing_track()

    def get_current_track_title(self):
        return self.current_track["item"]["name"]

    def get_current_track_progress(self):
        time =  int(self.current_track["progress_ms"] / 1000)
        minutes = int(time / 60)
        seconds = time % 60

        return str(minutes) + ":" + str(seconds)

    def get_current_track_duration(self):
        time = int(self.current_track["item"]["duration_ms"] / 1000)
        minutes = int(time / 60)
        seconds = time % 60

        return str(minutes) + ":" + str(seconds)

    def get_current_track_artists(self):
        returns = []
        arists = self.current_track["item"]["artists"]
        for artist in arists:
            returns.append(artist["name"])
        
        return returns

    def get_current_track_album(self):
        return self.current_track["item"]["album"]["name"]

    def get_device(self):
        self.devices = self.sp.devices()["devices"]

    def get_devices_name(self):
        devices = []
        for device in self.devices:
            devices.append(device["name"])
        
        return devices

    def skip_to_next_track(self):
        if((time.time() - self.allow_skip) > 5):
            self.sp.next_track()
            self.allow_skip = time.time()

