from classes.celestial_body import CelestialBody
from classes.atmosphere import Atmosphere


class Planet(CelestialBody):
    def __init__(self, mass, radius, x, y, velocity_x, velocity_y, atm: Atmosphere):
        super().__init__(mass, radius, x, y, velocity_x, velocity_y)
        self.atmosphere = atm
