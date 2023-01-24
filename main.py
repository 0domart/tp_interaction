import threading
import json
import random

import pygame.time
from pygame import Vector2, time
import core
from agent import Agent

import matplotlib.pyplot as plt

from vegetal import Vegetal


def loadPath(param):
    # Open the file and read its contents
    with open(param, 'r') as f:
        data = json.load(f)

    # Access the values
    nb_super_predateur = data['SuperPredateur']['nb']
    vitesse_max_super_predateur_min = data['SuperPredateur']['parametres']['vitesseMax'][0]
    vitesse_max_super_predateur_max = data['SuperPredateur']['parametres']['vitesseMax'][1]
    acceleration_max_super_predateur_min = data['SuperPredateur']['parametres']['accelerationMax'][0]
    acceleration_max_super_predateur_max = data['SuperPredateur']['parametres']['accelerationMax'][1]
    MaxFaim_super_predateur_min = data['SuperPredateur']['parametres']['MaxFaim'][0]
    MaxFaim_super_predateur_max = data['SuperPredateur']['parametres']['MaxFaim'][1]
    MaxFatigue_super_predateur_min = data['SuperPredateur']['parametres']['MaxFatigue'][0]
    MaxFatigue_super_predateur_max = data['SuperPredateur']['parametres']['MaxFatigue'][1]
    MaxReproduction_super_predateur_min = data['SuperPredateur']['parametres']['MaxReproduction'][0]
    MaxReproduction_super_predateur_max = data['SuperPredateur']['parametres']['MaxReproduction'][1]
    MaxEndormi_super_predateur_min = data['SuperPredateur']['parametres']['MaxEndormi'][0]
    MaxEndormi_super_predateur_max = data['SuperPredateur']['parametres']['MaxEndormi'][1]
    MaxEsperance_super_predateur_min = data['SuperPredateur']['parametres']['MaxEsperance'][0]
    MaxEsperance_super_predateur_max = data['SuperPredateur']['parametres']['MaxEsperance'][1]

    for i in range(0, nb_super_predateur):
        core.memory('agents').append(Agent("SUPER_PREDATEUR",
                                           Vector2(random.randint(20, core.WINDOW_SIZE[0] - 20),
                                                   random.randint(20, core.WINDOW_SIZE[1] - 20)),
                                           vitesse_max_super_predateur_min
                                           , vitesse_max_super_predateur_max
                                           , acceleration_max_super_predateur_min
                                           , acceleration_max_super_predateur_max
                                           , MaxFaim_super_predateur_min
                                           , MaxFaim_super_predateur_max
                                           , MaxFatigue_super_predateur_min
                                           , MaxFatigue_super_predateur_max
                                           , MaxReproduction_super_predateur_min,
                                           MaxReproduction_super_predateur_max,
                                           MaxEndormi_super_predateur_min,
                                           MaxEndormi_super_predateur_max,
                                           MaxEsperance_super_predateur_min,
                                           MaxEsperance_super_predateur_max))

    nb_super_predateur = data['Herbivore']['nb']
    vitesse_max_super_predateur_min = data['Herbivore']['parametres']['vitesseMax'][0]
    vitesse_max_super_predateur_max = data['Herbivore']['parametres']['vitesseMax'][1]
    acceleration_max_super_predateur_min = data['Herbivore']['parametres']['accelerationMax'][0]
    acceleration_max_super_predateur_max = data['Herbivore']['parametres']['accelerationMax'][1]
    MaxFaim_super_predateur_min = data['Herbivore']['parametres']['MaxFaim'][0]
    MaxFaim_super_predateur_max = data['Herbivore']['parametres']['MaxFaim'][1]
    MaxFatigue_super_predateur_min = data['Herbivore']['parametres']['MaxFatigue'][0]
    MaxFatigue_super_predateur_max = data['Herbivore']['parametres']['MaxFatigue'][1]
    MaxReproduction_super_predateur_min = data['Herbivore']['parametres']['MaxReproduction'][0]
    MaxReproduction_super_predateur_max = data['Herbivore']['parametres']['MaxReproduction'][1]
    MaxEndormi_super_predateur_min = data['Herbivore']['parametres']['MaxEndormi'][0]
    MaxEndormi_super_predateur_max = data['Herbivore']['parametres']['MaxEndormi'][1]
    MaxEsperance_super_predateur_min = data['Herbivore']['parametres']['MaxEsperance'][0]
    MaxEsperance_super_predateur_max = data['Herbivore']['parametres']['MaxEsperance'][1]

    for i in range(0, nb_super_predateur):
        core.memory('agents').append(Agent("HERBIVORE",
                                           Vector2(random.randint(20, core.WINDOW_SIZE[0] - 20),
                                                   random.randint(20, core.WINDOW_SIZE[1] - 20)),
                                           vitesse_max_super_predateur_min
                                           , vitesse_max_super_predateur_max
                                           , acceleration_max_super_predateur_min
                                           , acceleration_max_super_predateur_max
                                           , MaxFaim_super_predateur_min
                                           , MaxFaim_super_predateur_max
                                           , MaxFatigue_super_predateur_min
                                           , MaxFatigue_super_predateur_max
                                           , MaxReproduction_super_predateur_min,
                                           MaxReproduction_super_predateur_max,
                                           MaxEndormi_super_predateur_min,
                                           MaxEndormi_super_predateur_max,
                                           MaxEsperance_super_predateur_min,
                                           MaxEsperance_super_predateur_max))

    nb_super_predateur = data['Carnivore']['nb']
    vitesse_max_super_predateur_min = data['Carnivore']['parametres']['vitesseMax'][0]
    vitesse_max_super_predateur_max = data['Carnivore']['parametres']['vitesseMax'][1]
    acceleration_max_super_predateur_min = data['Carnivore']['parametres']['accelerationMax'][0]
    acceleration_max_super_predateur_max = data['Carnivore']['parametres']['accelerationMax'][1]
    MaxFaim_super_predateur_min = data['Carnivore']['parametres']['MaxFaim'][0]
    MaxFaim_super_predateur_max = data['Carnivore']['parametres']['MaxFaim'][1]
    MaxFatigue_super_predateur_min = data['Carnivore']['parametres']['MaxFatigue'][0]
    MaxFatigue_super_predateur_max = data['Carnivore']['parametres']['MaxFatigue'][1]
    MaxReproduction_super_predateur_min = data['Carnivore']['parametres']['MaxReproduction'][0]
    MaxReproduction_super_predateur_max = data['Carnivore']['parametres']['MaxReproduction'][1]
    MaxEndormi_super_predateur_min = data['Carnivore']['parametres']['MaxEndormi'][0]
    MaxEndormi_super_predateur_max = data['Carnivore']['parametres']['MaxEndormi'][1]
    MaxEsperance_super_predateur_min = data['Carnivore']['parametres']['MaxEsperance'][0]
    MaxEsperance_super_predateur_max = data['Carnivore']['parametres']['MaxEsperance'][1]

    for i in range(0, nb_super_predateur):
        core.memory('agents').append(Agent("CARNIVORE",
                                           Vector2(random.randint(20, core.WINDOW_SIZE[0] - 20),
                                                   random.randint(20, core.WINDOW_SIZE[1] - 20)),
                                           vitesse_max_super_predateur_min
                                           , vitesse_max_super_predateur_max
                                           , acceleration_max_super_predateur_min
                                           , acceleration_max_super_predateur_max
                                           , MaxFaim_super_predateur_min
                                           , MaxFaim_super_predateur_max
                                           , MaxFatigue_super_predateur_min
                                           , MaxFatigue_super_predateur_max
                                           , MaxReproduction_super_predateur_min,
                                           MaxReproduction_super_predateur_max,
                                           MaxEndormi_super_predateur_min,
                                           MaxEndormi_super_predateur_max,
                                           MaxEsperance_super_predateur_min,
                                           MaxEsperance_super_predateur_max))

    nb_super_predateur = data['Decompositeur']['nb']
    vitesse_max_super_predateur_min = data['Decompositeur']['parametres']['vitesseMax'][0]
    vitesse_max_super_predateur_max = data['Decompositeur']['parametres']['vitesseMax'][1]
    acceleration_max_super_predateur_min = data['Decompositeur']['parametres']['accelerationMax'][0]
    acceleration_max_super_predateur_max = data['Decompositeur']['parametres']['accelerationMax'][1]
    MaxFaim_super_predateur_min = data['Decompositeur']['parametres']['MaxFaim'][0]
    MaxFaim_super_predateur_max = data['Decompositeur']['parametres']['MaxFaim'][1]
    MaxFatigue_super_predateur_min = data['Decompositeur']['parametres']['MaxFatigue'][0]
    MaxFatigue_super_predateur_max = data['Decompositeur']['parametres']['MaxFatigue'][1]
    MaxReproduction_super_predateur_min = data['Decompositeur']['parametres']['MaxReproduction'][0]
    MaxReproduction_super_predateur_max = data['Decompositeur']['parametres']['MaxReproduction'][1]
    MaxEndormi_super_predateur_min = data['Decompositeur']['parametres']['MaxEndormi'][0]
    MaxEndormi_super_predateur_max = data['Decompositeur']['parametres']['MaxEndormi'][1]
    MaxEsperance_super_predateur_min = data['Decompositeur']['parametres']['MaxEsperance'][0]
    MaxEsperance_super_predateur_max = data['Decompositeur']['parametres']['MaxEsperance'][1]

    for i in range(0, nb_super_predateur):
        core.memory('agents').append(Agent("DECOMPOSITEUR",
                                           Vector2(random.randint(20, core.WINDOW_SIZE[0] - 20),
                                                   random.randint(20, core.WINDOW_SIZE[1] - 20)),
                                           vitesse_max_super_predateur_min
                                           , vitesse_max_super_predateur_max
                                           , acceleration_max_super_predateur_min
                                           , acceleration_max_super_predateur_max
                                           , MaxFaim_super_predateur_min
                                           , MaxFaim_super_predateur_max
                                           , MaxFatigue_super_predateur_min
                                           , MaxFatigue_super_predateur_max
                                           , MaxReproduction_super_predateur_min,
                                           MaxReproduction_super_predateur_max,
                                           MaxEndormi_super_predateur_min,
                                           MaxEndormi_super_predateur_max,
                                           MaxEsperance_super_predateur_min,
                                           MaxEsperance_super_predateur_max))
        for i in range(0,  data['Vegetal']['nb']):
            core.memory('vegetals').append(Vegetal())

def setup():
    core.memory("last_call", pygame.time.get_ticks())
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]

    core.memory("agents", [])
    core.memory("vegetals", [])

    # Recuperer les parametres du fichier JSON
    loadPath('parameters.json')

    x = threading.Thread(target=draw_graph, args=())
    x.start()

    print("Setup END-----------")


def computePerception():
    for a in core.memory('agents'):
        a.body.fustrum.perceptionList = []
        for b in core.memory('vegetals'):
            if a.body.fustrum.vision(b):
                a.body.fustrum.perceptionList.append(b)
        for b in core.memory('agents'):
            if a.uuid != b.uuid:
                if a.body.fustrum.vision(b.body):
                    a.body.fustrum.perceptionList.append(b.body)


def computeDecision():
    for a in core.memory('agents'):
        a.update()


def applyDecision(agent):
    agent.body.update()


# Ajout d'un super predateur quand on clique avec la souris
def predateurManuelle():
    mousex, mousey = pygame.mouse.get_pos()

    agent_le_plus_proche = 0
    agent_distance_le_plus_proche = 99999

    for agent in core.memory("agents"):
        if agent_le_plus_proche == 0:
            agent_le_plus_proche = agent
        else:
            nouvelle_distance = agent.body.position.distance_to(Vector2(mousex, mousey))

            if agent_distance_le_plus_proche > nouvelle_distance:
                agent_le_plus_proche = agent
                agent_distance_le_plus_proche = nouvelle_distance

    agent_le_plus_proche.statut = "SUPER_PREDATEUR"
    agent_le_plus_proche.timer_contagion = 0
    agent_le_plus_proche.timer_die = pygame.time.get_ticks()
    agent_le_plus_proche.timer_guerison = pygame.time.get_ticks()


def show_stats_console():
    status_counts = {}

    genetique_vmax = {"title": "Meilleure VMAX", "value": 0, "agent_id": 0, "agent_statut": ""}
    genetique_jauge_faim_max = {"title": "Meilleure Jauge de Faim", "value": 0, "agent_id": 0, "agent_statut": ""}
    genetique_jauge_fatigue_max = {"title": "Meilleure Jauge de Fatigue", "value": 0, "agent_id": 0, "agent_statut": ""}
    genetique_jauge_reproduction_max = {"title": "Meilleure Jauge de Reproduction", "value": 0, "agent_id": 0, "agent_statut": ""}
    genetique_jauge_esperance_vie_max = {"title": "Meilleure Esperance de Vie", "value": 0, "agent_id": 0, "agent_statut": ""}

    for obj in core.memory("agents"):
        status = obj.body.statut
        if genetique_vmax["value"] < obj.body.vMax:
            genetique_vmax["value"] = obj.body.vMax
            genetique_vmax["agent_id"] = obj.uuid
            genetique_vmax["agent_statut"] = status

        if genetique_jauge_faim_max["value"] < obj.body.jauge_faim_max:
            genetique_jauge_faim_max["value"] = obj.body.jauge_faim_max
            genetique_jauge_faim_max["agent_id"] = obj.uuid
            genetique_jauge_faim_max["agent_statut"] = status

        if genetique_jauge_fatigue_max["value"] < obj.body.jauge_fatigue_max:
            genetique_jauge_fatigue_max["value"] = obj.body.jauge_fatigue_max
            genetique_jauge_fatigue_max["agent_id"] = obj.uuid
            genetique_jauge_fatigue_max["agent_statut"] = status

        if genetique_jauge_reproduction_max["value"] < obj.body.jauge_reproduction_max:
            genetique_jauge_reproduction_max["value"] = obj.body.jauge_reproduction_max
            genetique_jauge_reproduction_max["agent_id"] = obj.uuid
            genetique_jauge_reproduction_max["agent_statut"] = status

        if genetique_jauge_esperance_vie_max["value"] < obj.body.esperance_vie:
            genetique_jauge_esperance_vie_max["value"] = obj.body.esperance_vie
            genetique_jauge_esperance_vie_max["agent_id"] = obj.uuid
            genetique_jauge_esperance_vie_max["agent_statut"] = status

        if status not in status_counts:
            status_counts[status] = 0
        status_counts[status] += 1

    status_counts["VEGETAL"] = 0
    status_counts["VEGETAL_DEAD"] = 0
    for obj in core.memory("vegetals"):
        if obj.vivant:
            status_counts["VEGETAL"] += 1
        else :
            status_counts["VEGETAL_DEAD"] += 1

    print(status_counts)
    print(genetique_vmax)
    print(genetique_jauge_faim_max)
    print(genetique_jauge_fatigue_max)
    print(genetique_jauge_reproduction_max)
    print(genetique_jauge_esperance_vie_max)
    print("\n")
    print("\n")


# This function will be called every 1 sec

history_time = []
history_data = {"HERBIVORE": [], "CARNIVORE": [], "SUPER_PREDATEUR": [], "VEGETAL": [], "VEGETAL_DEAD": [], "DEAD": [], 'DECOMPOSITEUR': []}


def draw_graph():
    while True:
        global history_data
        global history_time

        data = {'HERBIVORE': 0, 'CARNIVORE': 0, 'SUPER_PREDATEUR': 0, 'VEGETAL': 0, 'VEGETAL_DEAD': 0, 'DEAD': 0, 'DECOMPOSITEUR': 0}
        for agent in core.memory("agents"):
            data[agent.body.statut] += 1

        for obj in core.memory("vegetals"):
            if obj.vivant:
                data["VEGETAL"] += 1
            else:
                data["VEGETAL_DEAD"] += 1

        plt.cla()  # Clear axis
        current_time = pygame.time.get_ticks() / 1000
        history_time.append(current_time)
        for key in history_data.keys():
            history_data[key].append(data[key])
            if key == "VEGETAL":
                plt.plot(history_time, history_data[key], 'g', label=key)
            elif key == "VEGETAL_DEAD":
                plt.plot(history_time, history_data[key], 'y', label=key)
            elif key == "SUPER_PREDATEUR":
                plt.plot(history_time, history_data[key], 'r', label=key)
            elif key == "CARNIVORE":
                plt.plot(history_time, history_data[key], 'orange', label=key)
            elif key == "DEAD":
                plt.plot(history_time, history_data[key], 'k', label=key)
            elif key == "HERBIVORE":
                plt.plot(history_time, history_data[key], 'grey', label=key)
            elif key == "DECOMPOSITEUR":
                plt.plot(history_time, history_data[key], 'blue', label=key)

        plt.xlabel('Temps (s)')
        plt.ylabel('Nombre de cas')
        plt.legend(loc="center left")
        plt.title("Evolution du statut des animaux à travers le temps")
        plt.ion()
        plt.draw()
        plt.show()
        plt.pause(0.001)


def run(last_call=None):
    core.cleanScreen()

    if core.getMouseLeftClick():
        predateurManuelle()

    if core.getKeyPressList('r'):
        show_stats_console()

    # Display
    for vegetal in core.memory("vegetals"):
        vegetal.show()

    for agent in core.memory("agents"):
        agent.show()

    computePerception()

    computeDecision()

    for agent in core.memory("agents"):
        applyDecision(agent)


core.main(setup, run)
