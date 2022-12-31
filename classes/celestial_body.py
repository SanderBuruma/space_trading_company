import entity


class CelestialBody(entity.Entity):
    def __init__(self, mass, radius, x, y, velocity_x, velocity_y):
        super().__init__(x, y, velocity_x, velocity_y)
        self.mass = mass
        self.radius = radius

    @property
    def surface_gravity(self):
        # Calculate surface gravity using Newton's law of gravitation
        g = 6.67430e-11  # gravitational constant
        return g * self.mass / (self.radius ** 2)
