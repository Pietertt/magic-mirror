class Controller:
    cooldown = False
    COOLDOWN_TIME = 1500

    def __init__(self, view, tk):
        self.view = view
        self.tk = tk
    
    def set_cooldown(self):
        self.cooldown = True

    def reset_cooldown(self):
        self.cooldown = False