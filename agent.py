import random

import pygame.time
from pygame import Vector2
import itertools

import core
from body import Body
from vegetal import Vegetal


class Agent(object):
    def __init__(self, statut, position, vmin, vmax, accmin, accmax, faim_min, faim_max, fatigue_min, fatigue_max,
                 reproduction_min, reproduction_max, endormi_min, endormi_max, esperance_min, esperance_max):
        self.body = Body(self, statut, position, vmin, vmax, accmin, accmax, faim_min, faim_max, fatigue_min,
                         fatigue_max, reproduction_min, reproduction_max, endormi_min, endormi_max, esperance_min,
                         esperance_max)
        self.uuid = random.randint(100000, 999999999)

    def filtrePerception(self):
        carnivore = []
        super_predateur = []
        herbivore = []
        decompositeur = []
        vegetal = []
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, Vegetal):
                vegetal.append(i)
            if isinstance(i, Body):
                if i.statut == "CARNIVORE":
                    carnivore.append(i)
                elif i.statut == "HERBIVORE":
                    herbivore.append(i)
                elif i.statut == "SUPER_PREDATEUR":
                    super_predateur.append(i)
                elif i.statut == "DECOMPOSITEUR":
                    decompositeur.append(i)

        carnivore.sort(key=lambda x: x.dist, reverse=False)
        herbivore.sort(key=lambda x: x.dist, reverse=False)
        super_predateur.sort(key=lambda x: x.dist, reverse=False)
        decompositeur.sort(key=lambda x: x.dist, reverse=False)
        vegetal.sort(key=lambda x: x.dist, reverse=False)

        return carnivore, super_predateur, herbivore, decompositeur, vegetal

    def faireUnEnfant(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
        core.memory('agents').append(Agent(a,
                                           b
                                           , c
                                           , d
                                           , e
                                           , f
                                           , g
                                           , h
                                           , i
                                           , j,
                                           k,
                                           l,
                                           m,
                                           n,
                                           o
                                           , p))

    def computeForce(self, preys, predators, friend):
        fuite = self.fuite(predators) * 2
        hunt = self.hunt(preys) * 1
        symbiose = self.symbiose(friend) * 2

        if fuite + hunt + symbiose == (0,0):
            self.body.acc += Vector2(random.randint(-5,5), random.randint(-5,5))
        else: self.body.acc = self.body.acc + hunt + fuite + symbiose

    def fuite(self, predators):
        steering = Vector2()
        if len(predators) > 0:
            prey = sorted(predators, key=lambda x: x.position.distance_to(self.body.position), reverse=True)[0]
            steering = prey.position + self.body.position
        return steering

    def symbiose(self, friends):
        steering = Vector2()
        if len(friends) > 0:
            prey = sorted(friends, key=lambda x: x.position.distance_to(self.body.position), reverse=True)[0]
            steering = prey.position - self.body.position
        return steering

    def hunt(self, preys):
        steering = Vector2()
        if len(preys) > 0:
            prey = sorted(preys, key=lambda x: x.position.distance_to(self.body.position), reverse=True)[0]
            steering = prey.position - self.body.position
        return steering

    def eat(self,preys):
        for p in preys:
            if p.position.distance_to(self.body.position) < 15:
                p.vivant = False
                p.statut = "DEAD"
                if p.statut == "CARNIVORE":
                    self.body.timer_faim = pygame.time.get_ticks() # On regarde toute sa jauge secondes en mangeant
                if p.statut == "HERBIVORE":
                    self.body.timer_faim -= 10000 # On gagne 10 secondes en mangeant un herbivore
                if p.statut == "DECOMPOSITEUR":
                    self.body.timer_faim -= 3000  # On gagne 3 secondes en mangeant un decompositeur
                if p.statut == "VEGETAL":
                    self.body.timer_faim -= 1000  # On gagne 1 secondes en mangeant un vegetal

    def update(self):

        carnivore, super_predateur, herbivore, decompositeur, vegetal = self.filtrePerception()

        if self.body.vivant:
            if self.body.endormi:
                self.body.vitesse = Vector2()
            elif self.body.statut == "SUPER_PREDATEUR":
                self.eat(list(itertools.chain(carnivore, decompositeur, vegetal)))
                self.computeForce(list(itertools.chain(carnivore, decompositeur, vegetal)), [], [])
            elif self.body.statut == "CARNIVORE":
                self.eat(list(itertools.chain(herbivore, decompositeur, vegetal)))
                self.computeForce(list(itertools.chain(herbivore, decompositeur, vegetal)), super_predateur, [])
            elif self.body.statut == "HERBIVORE":
                self.eat(list(itertools.chain(vegetal, decompositeur)))
                self.computeForce(list(itertools.chain(vegetal, decompositeur, vegetal)), carnivore, super_predateur)
            elif self.body.statut == "DECOMPOSITEUR":
                self.eat(vegetal)
                self.computeForce(vegetal, list(itertools.chain(super_predateur, carnivore, herbivore)), [])
        else:
            self.body.vitesse = Vector2()

    def show(self):
        self.body.show()
