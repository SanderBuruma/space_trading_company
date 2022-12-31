import celestial_body


class Star(celestial_body.CelestialBody):
    def __init__(self, mass, radius, x, y, velocity_x, velocity_y):
        super().__init__(mass, radius, x, y, velocity_x, velocity_y)

