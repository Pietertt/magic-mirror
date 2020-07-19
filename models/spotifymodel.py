import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep
import spotipy.util as util
import os

class SpotifyModel:
    USERNAME = 'drjzrg9lstsquvizucpgl8knp' 
    CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
    REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
    SCOPE = 'user-read-currently-playing, user-read-playback-state,user-modify-playback-state, app-remote-control' 

    def __init__(self):
        self.token = util.prompt_for_user_token(username = self.USERNAME, scope = self.SCOPE, client_id = self.CLIENT_ID, client_secret = self.CLIENT_SECRET, redirect_uri = self.REDIRECT_URI)
        self.sp = spotipy.Spotify(auth = self.token)

        self.sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])
    
if __name__ == '__main__':
    s = SpotifyModel()