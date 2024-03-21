import random
from datetime import timedelta
from enum import Enum
from nation_data.coordination.retreive_and_convert import retreive_coords, convert_coords
import json as js

from game.ai.nation_ai import NationAI

flags = {
    "1910": "../flags/netherlands/vector-illustration-of-netherlands-flag.jpg",
    "1914": "../flags/netherlands/vector-illustration-of-netherlands-flag.jpg",
    "1918": "../flags/netherlands/vector-illustration-of-netherlands-flag.jpg",
    "1932": "../flags/netherlands/vector-illustration-of-netherlands-flag.jpg",
    "1936": "../flags/netherlands/vector-illustration-of-netherlands-flag.jpg",
    "1939": "../flags/netherlands/vector-illustration-of-netherlands-flag.jpg"
}

leader_images = {"1910": "../leaders/netherlands/skirmer_1910.png",
                 "1914": "../leaders/netherlands/250px-Pieter_Cort_van_der_Linden_1914-1918.jpg",
                 "1918": "../leaders/netherlands/250px-Pieter_Cort_van_der_Linden_1914-1918.jpg",
                 "1932": "../leaders/netherlands/Beerenbrouck_1932.jpg",
                 "1936": "../leaders/netherlands/Hendrik_Colijn_(1925)_1936-1939.jpg",
                 "1939": "../leaders/netherlands/Hendrik_Colijn_(1925)_1936-1939.jpg"
                 }

"""Population Dictionaries"""
population = {
    "1910": 5910000,
    "1914": 6270000,
    "1918": 6640000,
    "1932": 8060000,
    "1936": 8450000,
    "1939": 8760000
}

"""Political Dictionaries"""
leaders = {
    "1910": "Theo Heemskerk",
    "1914": "Pieter Cort der Linden",
    "1918": "Pieter Cort van der Linden",
    "1932": "Charles Ruijs de Beerenbrouck",
    "1936": "Hendrikus Colijn",
    "1939": "Hendrikus Colijn"
}

monarchs = {
    "1910": "Wilhelmina",
    "1914": "Wilhelmina",
    "1918": "Wilhelmina",
    "1932": "Wilhelmina",
    "1936": "Wilhelmina",
    "1939": "Wilhelmina"
}

gdp = {
    "1910": 865645049,
    "1914": 1111426098,
    "1918": 1844390540,
    "1932": 2118539364,
    "1936": 3213537630,
    "1939": 3201339327
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class Netherlands(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.date_checker = globe.date + timedelta(days=3)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Netherlands"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.political_typology = "Democratic"
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
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
        # other
        self.coordinates = []
        self.land = ["Dutch East Indies", "Netherlands", "Netherlands Antilles"]
        self.foreign_relations = {"foreign relations": []}
    def establish_foreign_objectives(self):
        if self.date.year > 1918:
            objectives_enemy = ["Contain Germany", "Contain Italy", "Contain Russia", "Contain Bulgaria",
                                "Contain Japan"]
            objectives_allies = ["Improve relations with United States", "Improve relations with France",
                                 "Improve relations with Canada", "Improve relations with Belgium",
                                 "Improve relations with Luxembourg", "Improve relations with Great Britain"]

            for enemy in objectives_enemy:
                self.objectives["objectives"][0]['foreign'].append(enemy)

            for ally in objectives_allies:
                self.objectives["objectives"][0]['foreign'].append(ally)
    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for land in range(0, len(self.land)):
            for i in range(0, len(nation_json['countries'])):
                if self.land[land] == nation_json['countries'][i]['nation_name']:
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))