import pygame


class Atmosphere:
    def __init__(self, density: float, scaling: float, color=pygame.color.Color(0, 0, 0)):
        self.density = density
        self.scaling = scaling
        self.color = color
