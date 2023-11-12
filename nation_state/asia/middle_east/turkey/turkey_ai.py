import random
import time
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
from nation_data.coordination.retreive_and_convert import retreive_coords
import json as js

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

leaders = {
    "1910": "Mehmed V",
    "1914": "Mehmed V",
    "1918": "Mehmed V",
    "1932": "Mustafa Kemal Atatürk",
    "1936": "Mustafa Kemal Atatürk",
    "1939": "Mustafa Kemal Atatürk"
}


population = {
    "1910": 14680000,
    "1914": 14340000,
    "1918": 13890000,
    "1932": 15250000,
    "1936": 16370000,
    "1939": 17260000
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": 12003528421,
    "1914": 15085307368,
    "1918": 14723268421,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

flags = {"1910": "../flags/turkey/Flag_of_the_Ottoman_Empire_(1844–1922).jpg",
         "1914": "../flags/turkey/Flag_of_the_Ottoman_Empire_(1844–1922).jpg",
         "1918": "../flags/turkey/Flag_of_the_Ottoman_Empire_(1844–1922).jpg",
         "1932": "../flags/turkey/Flag_of_the_Ottoman_Empire_(1844–1922).jpg",
         "1936": "../flags/turkey/Flag_of_the_Ottoman_Empire_(1844–1922).jpg",
         "1939": "../flags/turkey/Flag_of_the_Ottoman_Empire_(1844–1922).jpg"
         }

leader_images = {
    "1910": "../leaders/turkey/Sultan_Muhammed_Chan_V.,_Kaiser_der_Osmanen_1915_C._Pietzner-1918.jpg",
    "1914": "../leaders/turkey/Sultan_Muhammed_Chan_V.,_Kaiser_der_Osmanen_1915_C._Pietzner-1918.jpg",
    "1918": "../leaders/turkey/Sultan_Muhammed_Chan_V.,_Kaiser_der_Osmanen_1915_C._Pietzner-1918.jpg",
    "1932": "../leaders/turkey/Ataturk1930s-1939.jpg",
    "1936": "../leaders/turkey/Ataturk1930s-1939.jpg",
    "1939": "../leaders/turkey/Ataturk1930s-1939.jpg"
}

class TurkeyAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "asia"
        self.name = "Turkey"
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
        objectives_enemy = ['Contain Greece', "Contain Bulgaria"]
        objectives_allies = ["Improve relations with Germany",
                             "Improve relations with Russia",
                             "Improve relations with Great Britain",
                             "Improve relations with France"]
        for enemy in objectives_enemy:
            self.objectives["objectives"][0]['foreign'].append(enemy)

        for ally in objectives_allies:
            self.objectives["objectives"][0]['foreign'].append(ally)

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        if self.date.year <= 1918:
            for i in range(len(nation_json['countries'])):
                if (nation_json['countries'][i]['nation_name'] == "Ottoman Empire"):
                    # print(retreive_coords((nation_json['countries'][i]['coordinates'])))
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates.append(retreive_coords(self.coordinates))

        if self.date.year == 1932 or self.date.year == 1936:
            for i in range(len(nation_json['countries'])):
                if (nation_json['countries'][i]['nation_name'] == "Ottoman Sultanate"):
                    # print(retreive_coords((nation_json['countries'][i]['coordinates'])))
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates.append(retreive_coords(self.coordinates))

        if self.date.year > 1936:
            for i in range(len(nation_json['countries'])):
                if (nation_json['countries'][i]['nation_name'] == "Turkey"):
                    # print(retreive_coords((nation_json['countries'][i]['coordinates'])))
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))
