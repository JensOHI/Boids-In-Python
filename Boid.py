class Boid:
    def __init__(self):
        self.pos = [0,0,0]
        self.direction = [1,0,0]
        self.velocity = self.direction
        self.acceleration = [0,0,0]

    def get_position(self):
        return self.pos

    def update(self, dt):
        self.pos = self.velocity * dt

