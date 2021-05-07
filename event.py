class KeyEvent:
    def __init__(self, key, time, dt):
        self.key = key
        self.time = time
        self.dt = dt

    def __str__(self):
        return str(self.key) + " at "+ str(self.time) + " for " + str(self.dt)