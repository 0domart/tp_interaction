import random

from pygame import Vector2

import core


class Vegetal(object):
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.mass = 5
        self.color = (124,252,0)
        self.statut = "VEGETAL"
        self.vivant = True

    def show(self):
        if self.vivant:
            core.Draw.circle(self.color, self.position, self.mass)
