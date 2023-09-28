import random
import time
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

from random_functions import random_functions


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


leaders = {
    "1910": "Emperor Xuantong",
    "1914": "Yuan Shikai",
    "1918": "Xu Shichangi",
    "1932": "Lin Sen",
    "1936": "Lin Sen",
    "1939": "Lin Sen"
}
monarchs = {
    "1910": "Emperor Xuantong",
    "1914": "Emperor Xuantong",
    "1918": "Emperor Xuantong",
    "1932": "Emperor Xuantong",
    "1936": "Emperor Xuantong",
    "1939": "Emperor Xuantong"
}

population = {
    "1910": 422250794,
    "1914": 438552995,
    "1918": 457741400,
    "1932": 494506632,
    "1936": 506322173,
    "1939": 514761109
}
gdp = {
    "1910": 17340421053,
    "1914": 19231073684,
    "1918": 23090862632,
    "1932": 48070526316,
    "1936": 60420631579,
    "1939": 54934157895
}


class ChinaAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "asia"
        self.name = "Republic of China"
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
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        if self.date.year <= 1918:
#Xinjiang
#Tibet
#Mongolia
            for i in range(len(nation_json['countries'])):
                if (nation_json['countries'][i]['nation_name'] == "Manchu Empire" or nation_json['countries'][i]['nation_name'] ==
                "Xinjiang" or nation_json['countries'][i]['nation_name'] == "Mongolia" or nation_json['countries'][i]['nation_name'] ==
                "Tibet"):
                    # print(retreive_coords((nation_json['countries'][i]['coordinates'])))
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))
        if self.date.year > 1918:

            for i in range(len(nation_json['countries'])):
                if (nation_json['countries'][i]['nation_name'] == "Chinese warlords"):
                    # print(retreive_coords((nation_json['countries'][i]['coordinates'])))
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

    # main function
    def main(self, globe):
        while self.population > 5000000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            self.stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break
