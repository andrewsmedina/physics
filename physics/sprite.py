class Sprite(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def step(self, x_velocity=0, y_velocity=0):
        self.x += x_velocity
        self.y += y_velocity
