import random
import time
from datetime import timedelta, datetime
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

leaders = {
    "1910": None,
    "1914": None,
    "1918": None,
    "1932": "Ignacy Mościcki",
    "1936": "Ignacy Mościcki",
    "1939": "Ignacy Mościcki"
}

population = {
    "1910": None,
    "1914": None,
    "1918": 23910000,
    "1932": 27890000,
    "1936": 28600000,
    "1939": 28990000
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": None,
    "1914": None,
    "1918": 14723268421,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

class PolandAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.spare_color = self.nation_color
        self.region = "europe"
        self.name = "Poland"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.political_typology = "Autocratic"
        self.leader = leaders[str(globe.date.year)]
        self.political_power = 200
        self.political_exponent = 1.56
        self.current_gdp = gdp[str(globe.date.year)]
        """Components of GDP"""
        self.consumer_spending = 200
        self.investment = 300
        self.government_spending = 350
        self.exports = 1000
        self.imports = 1200
        self.coordinates = []
        self.land = ["Poland"]
        self.foreign_relations = {"foreign relations": []}

    def establish_foreign_objectives(self):

        objectives_enemy = ["Contain Germany", "Contain Italy", "Contain Russia", "Contain Japan"]
        objectives_allies = ["Improve relations with United States", "Improve relations with Britain",
                             "Improve relations with France"]

        for enemy in objectives_enemy:
            self.objectives["objectives"][0]['foreign'].append(enemy)

        for ally in objectives_allies:
            self.objectives["objectives"][0]['foreign'].append(ally)

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for land in range(0, len(self.land)):
            for i in range(0, len(nation_json['countries'])):
                if self.land[land] == nation_json['countries'][i]['nation_name']:
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]