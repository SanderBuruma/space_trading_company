import unittest

from classes.celestial_body import CelestialBody


class TestCelestialBody(unittest.TestCase):
    def setUp(self):
        self.earth = CelestialBody(5.972e24, 6371e3, 0, 0, 0, 0)
        self.moon = CelestialBody(7.34767309e22, 1737.1e3, 0, 0, 0, 0)
        self.mercury = CelestialBody(3.3011e23, 2439.7e3, 0, 0, 0, 0)
        self.venus = CelestialBody(4.8675e24, 6051.8e3, 0, 0, 0, 0)
        self.mars = CelestialBody(6.4185e23, 3389.5e3, 0, 0, 0, 0)

    def test_surface_gravity(self):
        self.assertAlmostEqual(self.earth.surface_gravity, 9.807, delta=0.1)
        self.assertAlmostEqual(self.moon.surface_gravity, 1.622, delta=0.1)
        self.assertAlmostEqual(self.mercury.surface_gravity, 3.7, delta=0.1)
        self.assertAlmostEqual(self.venus.surface_gravity, 8.87, delta=0.1)
        self.assertAlmostEqual(self.mars.surface_gravity, 3.711, delta=0.1)


if __name__ == '__main__':
    unittest.main()
