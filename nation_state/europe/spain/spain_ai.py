import random
import time
from datetime import datetime, timedelta
from enum import Enum
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

from game.ai.nation_ai import NationAI

leaders = {
    "1910" : "Segismundo Moret",
    "1914" : "Eduardo Dato",
    "1918" : "Manuel García Prieto",
    "1932" : "Niceto Alcalá-Zamora",
    "1936" : "Manuel Azaña",
    "1939" : "Manuel Azaña"
}
monarchs = {
    "1910" : "Alfonso XIII",
    "1914" : "Alfonso XIII",
    "1918" : "Alfonso XIII",
    "1932" : "Henri VII/Jacques II",
    "1936" : "Henri VII/Jacques II",
    "1939" : "Henri VII/Jacques II"
}

population = {
    "1910": 19681917,
    "1914": 20400000,
    "1918": 20950000,
    "1932": 23890000,
    "1936": 24810000,
    "1939": 25510000
}
gdp = {
    "1910": 2159663720,
    "1914": 2547024746,
    "1918": 5653286406,
    "1932": 2940653248,
    "1936": 3978738880,
    "1939": 4366978929
}

flags = {"1910": "../flags/spain/spain_flag_1910-1930.png",
         "1914": "../flags/spain/spain_flag_1910-1930.png",
         "1918": "../flags/spain/spain_flag_1910-1930.png",
         "1932": "../flags/spain/spanish_flag_1932_1936.jpg",
         "1936": "../flags/spain/spanish_flag_1932_1936.jpg",
         "1939": "../flags/spain/nationalist_spain_1939.jpg"}

leader_images = {
    "1910": "../leaders/spain/alfonso_xiii.jpg",
    "1914": "../leaders/spain/alfonso_xiii.jpg",
    "1918": "../leaders/spain/alfonso_xiii.jpg",
    "1932": "../leaders/spain/330px-Niceto_Alcalá-Zamora_(cropped)1932-1936.jpg",
    "1936": "../leaders/spain/330px-Niceto_Alcalá-Zamora_(cropped)1932-1936.jpg",
    "1939": "../leaders/spain/franco.jpg"
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


class SpainAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.date_checker = globe.date + timedelta(days=3)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Spain"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.political_typology = "Autocratic"
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.political_power = 200
        self.political_exponent = 1.56
        self.current_gdp = gdp[str(globe.date.year)]
        """Components of GDP"""
        self.consumer_spending = 200
        self.investment = 300
        self.government_spending = 350
        self.exports = 1000
        self.imports = 1200
        # other
        self.coordinates = []
        self.foreign_relations = {"foreign relations": []}

    def establish_foreign_objectives(self):


        if self.date.year > 1918:
            objectives_enemy = ["Contain Great Britain", "Contain France", "Contain Russia"]
            objectives_allies = ["Improve relations with Germany", "Improve relations with Italy", "Improve relations with Portugal"]

            for enemy in objectives_enemy:
                self.objectives["objectives"][0]['foreign'].append(enemy)

            for ally in objectives_allies:
                self.objectives["objectives"][0]['foreign'].append(ally)

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for i in range(len(nation_json['countries'])):
            # print(nation_json['countries'][i]['nation_name'])
            if (nation_json['countries'][i]['nation_name'] == "Spain"):
                # print(nation_json['countries'][i]['coordinates'])
                self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))