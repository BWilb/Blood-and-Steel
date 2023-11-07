import random
import time
from datetime import datetime, timedelta
from nation_data.coordination.retreive_and_convert import retreive_coords
import json as js
from game.ai.nation_ai import NationAI
import os
chancellors = {
    "1910": "Theobald von Bethmann Hollweg",
    "1914": "Theobald von Bethmann Hollweg",
    "1918": "Friedrich Ebert",
    "1932": "Kurt von Schleicher",
    "1936": "Adolf Hitler",
    "1939": "Adolf Hitler"
}

kaisers = {
    "1910": "Wilhelm II",
    "1914": "Wilhelm II",
    "1918": "None",
    "1932": "None",
    "1936": "None",
    "1939": "None"
}
"""Dictionary for population
    Population selection will be in sync with time frame selection
    Population will then be set up to grow or shrink in random amounts"""
population = {

    "1910": 64060000,
    "1914": 64030000,
    "1918": 63310000,
    "1932": 68180000,
    "1936": 70130000,
    "1939": 71500000
}

# economic variables and dictionaries
gdp = {
    "1910": 15783763158,
    "1914": 17856842105,
    "1918": 23873207895,
    "1932": 44371994737,
    "1936": 53157368421,
    "1939": 54936947368
}
flags = {"1910": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1914": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1918": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1932": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1936": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1939": "../flags/japan/Flag_of_Japan_(1870–1999).jpg"}

leader_images = {
    "1910": "../leaders/germany/holleg_1917.jpeg",
    "1914": "../leaders/germany/holleg_1917.jpeg",
    "1918": "../leaders/germany/von_herling-1918.jpg",
    "1932": "../leaders/germany/bruning-1932.jpg",
    "1936": "../leaders/germany/hitler-1936-1945.jpg",
    "1939": "../leaders/germany/hitler-1936-1945.jpg"
}

class GermanAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.date_checker = globe.date + timedelta(days=3)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.spare_color = self.nation_color
        self.region = "europe"
        self.name = "Germany"
        self.date = datetime(globe.date.year, 1, 1)
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = chancellors[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        if globe.date.year <= 1918:
            self.political_typology = "Autocratic"
        else:
            self.political_typology = "Fascist"
        self.political_power = 200
        self.political_exponent = 1.56
        """Stability"""
        self.stability = 95.56
        # economic
        self.corporate_taxes = 24.00
        self.income_taxes = 20.00
        self.current_gdp = gdp[str(globe.date.year)]
        """Components of GDP"""
        self.consumer_spending = 200
        self.investment = 300
        self.government_spending = 350
        self.exports = 1000
        self.imports = 1200
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # international
        self.alliance = ""
        self.us_relations = 34.56
        # other
        self.coordinates = []
        self.land_1910_1914 = ["German Empire", "German South-West Africa", "German E. Africa (Tanganyika)",
                               "French Cameroons"]
        self.land_1918 = ["German Empire"]
        self.land_1932_1936 = ["Germany", "East Prussia"]
        self.land_1939 = ["Germany", "East Prussia", "Czechoslovakia"]
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

            {"nation name": "Denmark",
             "relations": 74.34,
             "relation status": "rival",
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
             "relations": 88.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Italy",
             "relations": 65.34,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Latvia",
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

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        if self.date.year <= 1914:
            for land in range(0, len(self.land_1910_1914)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1910_1914[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year == 1918:
            for land in range(0, len(self.land_1918)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1918[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year == 1932 or self.date.year == 1936:
            for land in range(0, len(self.land_1932_1936)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1932_1936[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))


        if self.date.year >= 1939:
            for land in range(0, len(self.land_1939)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1939[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

    def establish_foreign_objectives(self):
        if self.date.year <= 1918:
            objectives_enemy = ["Contain France", "Contain Russia", "Contain Great Britain"]
            objectives_allies = ["Improve relations with Mexico", "Improve relations with Sweden", "Improve relations with Austria",
                                 "Improve relations with Turkey", "Improve relations with Bulgaria", "Improve relations with Afghanistan"]

        else:
            objectives_enemy = ["Contain France", "Contain Russia", "Contain Great Britain"]
            objectives_allies = ["Improve relations with Italy", "Improve relations with Japan", "Improve relations with Romania",
                                 "Improve relations with Hungary"]

        for enemy in objectives_enemy:
            self.objectives["objectives"][0]['foreign'].append(enemy)

        for ally in objectives_allies:
            self.objectives["objectives"][0]['foreign'].append(ally)
    # main function
    def main(self, globe, network, user_nation):
        #super().establishing_beginning_objectives()
        while self.population > 2000000:
            super().check_economic_growth(globe.date)
            super().check_population_growth()
            super().political_power_growth()
            super().stability_happiness_change(globe)
            if globe.date > self.date_checker:
                super().determine_diplomatic_approach(globe, network, user_nation)
                self.date_checker = globe.date + timedelta(days=3)
            super().change_relations(globe.nations)
            chance = random.randrange(1, 50)
            if chance % 8 == 2 or chance % 5 == 4:
                super().protests()
            super().pop_growth()
            super().check_economic_state(globe.date)
            super().adding_conscription_pool(globe)
            break