from classes.celestial_body import CelestialBody


class Star(CelestialBody):
    def __init__(self, mass, radius, x, y, velocity_x, velocity_y):
        super().__init__(mass, radius, x, y, velocity_x, velocity_y)

