import random
from datetime import timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

leaders = {
    "1910": "Paul Eyschen",
    "1914": "Paul Eyschen",
    "1918": "Léon Kauffman",
    "1932": "Pierre Dupong",
    "1936": "Pierre Dupong",
    "1939": "Pierre Dupong"
}
monarchs = {
    "1910": "Guillaume IV",
    "1914": "Marie-Adélaïde",
    "1918": "Marie-Adélaïde",
    "1932": "Charlotte",
    "1936": "Charlotte",
    "1939": "Charlotte"
}

population = {
    "1910": 2850000,
    "1914": 2630000,
    "1918": 2360000,
    "1932": 2430000,
    "1936": 2440000,
    "1939": 2450000
}
gdp = {
    "1910": 465966372,
    "1914": 484702474,
    "1918": 495328640,
    "1932": 503740350,
    "1936": 522800000,
    "1939": 703789473
}

flags = {
    "1910": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1914": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1918": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1932": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1936": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1939": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg"
}

leader_images = {"1910": "../leaders/luxembourg/paul_eyschen_accroche_1910-1914.jpg",
                 "1914": "../leaders/luxembourg/paul_eyschen_accroche_1910-1914.jpg",
                 "1918": "../leaders/luxembourg/Léon_Kauffman_(1869-1952)_1918.jpg",
                 "1932": "../leaders/luxembourg/Joseph_Bech_(detail)_1933.jpg",
                 "1936": "../leaders/luxembourg/Pierre_Dupong,_Benelux_conference_The_Hague_March_1949,_Luxembourg_Delegation_1939.jpg",
                 "1939": "../leaders/luxembourg/Pierre_Dupong,_Benelux_conference_The_Hague_March_1949,_Luxembourg_Delegation_1939.jpg"
                 }


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


class LuxembourgAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Luxembourg"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.political_typology = "Republicanism"
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
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
        self.land = ["Luxembourg"]
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
             "relations": 34.34,
             "relation status": "enemy",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Belgium",
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

            {"nation name": "Bulgaria",
             "relations": 68.34,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Denmark",
             "relations": 98.34,
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

            {"nation name": "Spain",
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

            {"nation name": "Russia",
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
        if self.date.year <= 1918:
            objectives_enemy = ["Contain Germany", "Contain Austria", "Contain Turkey"]
            objectives_allies = ["Improve relations with Russia", "Improve relations with Great Britain"]

        else:
            objectives_enemy = ["Contain Germany", "Contain Austria", "Contain Russia"]
            objectives_allies = ["Improve relations with Great Britain", "Improve relations with United States"]

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

        for land in range(0, len(self.land)):
            for i in range(0, len(nation_json['countries'])):
                if self.land[land] == nation_json['countries'][i]['nation_name']:
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]

    # main function
    def main(self, globe, network, user_nation):
        #print(self.objectives)
        while self.population > 100000:
            super().check_economic_growth(globe.date)
            super().check_population_growth()
            super().political_power_growth()
            super().stability_happiness_change(globe)
            super().determine_diplomatic_approach(globe, network, user_nation)
            super().change_relations(globe.nations)
            chance = random.randrange(1, 50)
            if chance % 8 == 2 or chance % 5 == 4:
                super().protests()
            super().pop_growth()
            super().check_economic_state(globe.date)
            self.date += timedelta(days=1)
            break
