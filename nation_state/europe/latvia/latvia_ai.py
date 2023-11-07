import random
import time
from datetime import datetime, timedelta
import json as js
from game.ai.nation_ai import NationAI
from nation_data.coordination.retreive_and_convert import retreive_coords
from enum import Enum

leader_images = {
    "1910": "",
    "1914": "",
    "1918": "",
    "1932": "../leaders/latvia/330px-Konstantin_Pats_1934.jpg",
    "1936": "../leaders/latvia/330px-Konstantin_Pats_1934.jpg",
    "1939": "../leaders/latvia/330px-Konstantin_Pats_1934.jpg"
}
flags = {
    "1910": "../flags/latvia/330px-KFlag_of_Latvia.svg.jpg",
    "1914": "../flags/latvia/330px-KFlag_of_Latvia.svg.jpg",
    "1918": "../flags/latvia/330px-KFlag_of_Latvia.svg.jpg",
    "1932": "../flags/latvia/330px-KFlag_of_Latvia.svg.jpg",
    "1936": "../flags/latvia/330px-KFlag_of_Latvia.svg.jpg",
    "1939": "../flags/latvia/330px-KFlag_of_Latvia.svg.jpg"
}

leaders = {
    "1910" : None,
    "1914" : None,
    "1918" : "Konstantin Päts",
    "1932" : "Konstantin Päts",
    "1936" : "Konstantin Päts",
    "1939" : "Konstantin Päts"
}

population = {
    "1910": 2450000,
    "1914": 2200000,
    "1918": 1950000,
    "1932": 1880000,
    "1936": 1910000,
    "1939": 1920000
}
gdp = {
    "1910": 4659663,
    "1914": 4847024,
    "1918": 4953286,
    "1932": 5037403,
    "1936": 5228000,
    "1939": 7037894
}

class LatviaAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.date_checker = globe.date + timedelta(days=3)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Latvia"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.political_typology = "Autocratic"
        self.political_power = 200
        self.political_exponent = 1.56
        # economic
        self.current_gdp = gdp[str(globe.date.year)]
        """Components of GDP"""
        self.consumer_spending = 200
        self.investment = 300
        self.government_spending = 350
        self.exports = 1000
        self.imports = 1200
        self.coordinates = []
        self.foreign_relations = {"foreign relations": [
            {"nation name": "Afghanistan",
             "relations": 60.56,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Iran",
             "relations": 70.56,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Iraq",
             "relations": 65.56,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Turkey",
             "relations": 57.56,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "China",
             "relations": 67.46,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Austria",
             "relations": 87.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Russia",
             "relations": 75.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Great Britain",
             "relations": 78.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Belgium",
             "relations": 68.34,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Bulgaria",
             "relations": 78.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Estonia",
             "relations": 48.34,
             "relation status": "enemy",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "France",
             "relations": 76.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Germany",
             "relations": 34.34,
             "relation status": "enemy",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Greece",
             "relations": 65.34,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Hungary",
             "relations": 48.34,
             "relation status": "enemy",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Denmark",
             "relations": 75.34,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Italy",
             "relations": 66.65,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Lithuania",
             "relations": 48.34,
             "relation status": "enemy",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Luxembourg",
             "relations": 88.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Netherlands",
             "relations": 88.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Norway",
             "relations": 78.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Poland",
             "relations": 54.45,
             "relation status": "enemy",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Portugal",
             "relations": 78.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Romania",
             "relations": 78.94,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Spain",
             "relations": 65.34,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Sweden",
             "relations": 75.54,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Switzerland",
             "relations": 98.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Canada",
             "relations": 88.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Cuba",
             "relations": 78.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Mexico",
             "relations": 79.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "United States",
             "relations": 65.34,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Argentina",
             "relations": 74.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Bolivia",
             "relations": 65.45,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Brazil",
             "relations": 76.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Chile",
             "relations": 79.56,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Columbia",
             "relations": 72.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Peru",
             "relations": 74.54,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Venezuela",
             "relations": 74.54,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False}
        ]}

    def establish_foreign_objectives(self):
        objectives_enemy = ["Contain Russia", "Contain Lithuania", "Contain Estonia"]
        objectives_allies = ["Improve relations with United States", "Improve relations with France",
                             "Improve relations with Great Britain"]

        for enemy in objectives_enemy:
            self.objectives["objectives"][0]['foreign'].append(enemy)

        for ally in objectives_allies:
            self.objectives["objectives"][0]['foreign'].append(ally)
    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
            for i in range(0, len(nation_json['countries'])):
                if nation_json['countries'][i]['nation_name'] == "Latvia":
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]