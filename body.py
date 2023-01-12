import random

import pygame.time
from pygame import Vector2

import core
from fustrum import Fustrum

class Body(object):
    def __init__(self, parent, statut, position, vmin, vmax, accmin, accmax, faim_min, faim_max, fatigue_min, fatigue_max,reproduction_min, reproduction_max, endormi_min, endormi_max, esperance_min, esperance_max):
        self.position = position
        self.vitesse = Vector2(random.uniform(-10, 10), random.uniform(-10, 10))
        self.vMax = random.randint(vmin, vmax)
        self.accMax = random.randint(accmin, accmax)
        self.mass = 10
        self.color = 1, 128, 1
        self.fustrum = Fustrum(10, self)
        self.acc = Vector2()
        self.parent = parent
        self.timer_faim = pygame.time.get_ticks()
        self.jauge_faim_max = random.randint(faim_min, faim_max)
        self.timer_fatigue = pygame.time.get_ticks()
        self.jauge_fatigue_max = random.randint(fatigue_min, fatigue_max)
        self.timer_endormi = 0
        self.jauge_endormi_max = random.randint(endormi_min, endormi_max)
        self.timer_reproduction = pygame.time.get_ticks()
        self.jauge_reproduction_max = random.randint(reproduction_min, reproduction_max)
        self.esperance_vie = random.randint(esperance_min, esperance_max)
        self.date_naissance = pygame.time.get_ticks()
        self.statut = statut

        self.vivant = True
        self.endormi = False

    def update(self):

        current_time = pygame.time.get_ticks()

        # Question 4 - Quand le body est trop vieux, l’agent meure
        if current_time - self.date_naissance > self.esperance_vie * 1000:
            self.statut = "DEAD"
            self.vivant = False

        # Question 4 - Quand la jauge de fatigue est pleine, l’agent dort
        elif current_time - self.timer_fatigue > self.jauge_fatigue_max * 1000:
            self.endormi = True
            self.timer_fatigue = current_time
            self.timer_endormi = pygame.time.get_ticks()

        # Question 4 - Reveiller après un long terme en train de dormir
        elif current_time - self.timer_endormi > self.jauge_endormi_max * 1000 and not self.timer_endormi == 0:
            self.endormi = False
            self.timer_endormi = 0

        # Question 4 - Quand la jauge de reproduction est pleine
        elif current_time - self.timer_reproduction > self.jauge_reproduction_max * 1000:
            self.timer_reproduction = current_time
            # reproduction
            self.parent.faireUnEnfant(self.statut,
                                      self.position,
                                               self.vMax
                                               , self.vMax+1
                                               , self.accMax
                                               , self.accMax+1
                                               , self.jauge_faim_max - 1
                                               , self.jauge_faim_max + 3
                                               , self.jauge_fatigue_max - 1
                                               , self.jauge_fatigue_max + 2
                                               , self.jauge_reproduction_max,
                                               self.jauge_reproduction_max + 5,
                                               self.endormi - 1,
                                               self.endormi + 1,
                                               self.esperance_vie - 1,
                                               self.esperance_vie + 1)


        # Question 4 - Quand la jauge de faim est pleine, l’agent meure de faim
        elif current_time - self.timer_faim > self.jauge_faim_max * 1000:
            self.endormi = True
            self.timer_faim = current_time
            self.timer_endormi = pygame.time.get_ticks()

        if self.acc.length() > self.accMax / self.mass:
            self.acc.scale_to_length(self.accMax / self.mass)

        self.vitesse = self.vitesse + self.acc

        if self.vitesse.length() > self.vMax:
            self.vitesse.scale_to_length(self.vMax)

        self.position = self.position + self.vitesse
        self.acc = Vector2()

        self.edge()

    def show(self):
        if self.statut == "HERBIVORE":
            core.Draw.circle((128, 128, 128), self.position, self.mass)
        elif self.statut == "CARNIVORE":
            core.Draw.circle((255, 165, 0), self.position, self.mass)
        elif self.statut == "SUPER_PREDATEUR":
            core.Draw.circle((255, 0, 0), self.position, self.mass)
        elif self.statut == "DECOMPOSITEUR":
            core.Draw.circle((0, 128, 255), self.position, self.mass)
        elif self.statut == "DEAD":
            a = 0 - self.vitesse.angle_to(Vector2(0, 1))
            p1 = self.position + Vector2(0, 0).rotate(a)
            p2 = self.position + Vector2(0, 45).rotate(a) - Vector2(35, 0)
            p3 = self.position + Vector2(45, 0).rotate(a) - Vector2(0, -35)
            #core.Draw.line((255, 255, 255), p1 + Vector2(-10,0), p2, 3)
            #core.Draw.line((255, 255, 255), p1 + Vector2(0,10), p3, 3)

    def edge(self):
        if self.position.x <= self.mass:
            self.vitesse.x *= -1
        if self.position.x + self.mass >= core.WINDOW_SIZE[0]:
            self.vitesse.x *= -1
        if self.position.y <= self.mass:
            self.vitesse.y *= -1
        if self.position.y + self.mass >= core.WINDOW_SIZE[1]:
            self.vitesse.y *= -1
