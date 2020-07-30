
import time
import tkinter as tk

from models.timemodel import TimeModel

from .controller import Controller

class SecondController(Controller):

    def __init__(self, view, tk):
        Controller.__init__(self, view, tk)
        
    def execute(self, data):
        print("Second controller")