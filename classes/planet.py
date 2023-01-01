from classes.celestial_body import CelestialBody
from classes.atmosphere import Atmosphere


class Planet(CelestialBody):
    def __init__(self, mass: float, radius: float, x: float, y: float, velocity_x: float, velocity_y: float, atm: Atmosphere):
        super().__init__(mass, radius, x, y, velocity_x, velocity_y)
        self.atmosphere = atm
