import time
import tkinter as tk

from .controller import Controller

class MainController(Controller):

    def __init__(self, view, tk):
        Controller.__init__(self, view, tk)
        
        
    def execute(self, data):
        print(data)