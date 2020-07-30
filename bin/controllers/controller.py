class Controller:
    cooldown = False
    COOLDOWN_TIME = 1500

    def __init__(self, view, tk):
        self.view = view
        self.tk = tk
  
        
    def execute(self, data):
        pass