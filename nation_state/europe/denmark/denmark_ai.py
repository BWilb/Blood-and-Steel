import random
import sys
import time
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

"""Population Dictionaries"""
population = {
    "1910": 2713555,
    "1914": 2905149,
    "1918": 3122049,
    "1932": 3600000,
    "1936": 3720000,
    "1939": 3810000
}

"""Political Dictionaries"""
leaders = {
    "1910": "Carl Theodor Zahle",
    "1914": "Carl Theodor Zahle",
    "1918": "Carl Theodor Zahle",
    "1932": "Thorvald Stauning",
    "1936": "Thorvald Stauning",
    "1939": "Thorvald Stauning"
}

monarchs = {
    "1910": "Frederick VIII",
    "1914": "Christian IX",
    "1918": "Christian IX",
    "1932": "Christian IX",
    "1936": "Christian IX",
    "1939": "Christian IX"
}

gdp = {
    "1910": 75000000,
    "1914": 76346343,
    "1918": 77648543,
    "1932": 76573434,
    "1936": 77346224,
    "1939": 78347343
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class Denmark(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Kingdom of Denmark"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = leaders[str(globe.date.year)]
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

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        for i in range(len(nation_json['countries'])):
            if nation_json['countries'][i]['nation_name'] == "Denmark":
                # print(retreive_coords((nation_json['countries'][i]['coordinates'])))
                self.coordinates = (retreive_coords(nation_json['countries'][i]['coordinates']))

    # main function
    def main(self, globe):
        while self.population > 2000000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break

