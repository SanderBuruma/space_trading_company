import celestial_body
import atmosphere


class Planet(celestial_body.CelestialBody):
    def __init__(self, mass, radius, x, y, velocity_x, velocity_y, atm: atmosphere.Atmosphere):
        super().__init__(mass, radius, x, y, velocity_x, velocity_y)
        self.atmosphere = atm
