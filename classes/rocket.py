import math
from typing import Type

from classes.celestial_body import CelestialBody


class Rocket:
    def __init__(self,
                 parent_body: CelestialBody,
                 fuel_mass,
                 empty_mass,
                 exhaust_velocity,
                 fuel_flow_rate,
                 ballistic_coefficient,
                 next_stage: Type['Rocket']):
        self.parent_body = parent_body
        self.fuel_mass = fuel_mass
        self.empty_mass = empty_mass
        self.exhaust_velocity = exhaust_velocity
        self.fuel_flow_rate = fuel_flow_rate
        self.next_stage = next_stage
        self.ballistic_coefficient = ballistic_coefficient

    @property
    def mass(self):
        return self.empty_mass + self.fuel_mass + self.next_stage.mass if self.next_stage else 0

    @property
    def dv(self):
        return math.log(self.mass / self.empty_mass, math.e) * self.exhaust_velocity + self.next_stage.dv if self.next_stage else 0

    @property
    def thrust(self):
        return self.fuel_flow_rate * self.exhaust_velocity

    @property
    def acceleration(self):
        return self.thrust / self.mass
