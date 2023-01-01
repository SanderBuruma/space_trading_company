import math
from typing import Type

from classes.celestial_body import CelestialBody


class Rocket:
    def __init__(self,
                 parent_body: CelestialBody,
                 fuel_mass: float,
                 empty_mass: float,
                 exhaust_velocity: float,
                 fuel_flow_rate: float,
                 ballistic_coefficient: float,
                 next_stage: Type['Rocket']):
        self.parent_body = parent_body
        self.fuel_mass = fuel_mass
        self.structural_mass = empty_mass
        self.exhaust_velocity = exhaust_velocity
        self.fuel_flow_rate = fuel_flow_rate
        self.ballistic_coefficient = ballistic_coefficient
        self.next_stage = next_stage

    @property
    def mass(self) -> float:
        return self.structural_mass + self.fuel_mass + self.next_stage.mass if self.next_stage else 0

    @property
    def dv(self) -> float:
        return math.log(self.mass / self.structural_mass, math.e) * self.exhaust_velocity + self.next_stage.dv if self.next_stage else 0

    @property
    def thrust(self) -> float:
        return self.fuel_flow_rate * self.exhaust_velocity

    @property
    def acceleration(self) -> float:
        return self.thrust / self.mass

    @property
    def thrust_to_weight_ratio(self) -> float:
        return self.parent_body.surface_gravity / self.acceleration
