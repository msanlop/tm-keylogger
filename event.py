class KeyEvent:
    def __init__(self, key, time, action):
        self.key = key
        self.time = time
        # self.dt = dt
        self.action = action # p(ressed) or r(eleased)

    def __str__(self):
        return str(self.key) + " " +  str(self.action) + " at "+ str(self.time) # + " for " + str(self.dt)