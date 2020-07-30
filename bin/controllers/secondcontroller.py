
import time
import tkinter as tk

from models.timemodel import TimeModel
from models.framemodel import FrameModel
from models.spotifymodel import SpotifyModel

from views.mainview import MainView

class SecondController:

    def __init__(self, view):
        self.view = view
        
    def execute(self, data):
        print("Second controller")