class Sprite(object):

    def __init__(self, x, y, x_velocity=0, y_velocity=0):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def step(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def accelerate(self, x_acceleration=0, y_acceleration=0):
        self.step()

        self.x_velocity *= 0.99
        self.y_velocity *= 0.99

        self.x_velocity += x_acceleration
        self.y_velocity += y_acceleration
