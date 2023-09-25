import time
from datetime import datetime, timedelta
import random
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


class PopulationState(Enum):
    LOW_GROWTH = 1
    HIGH_GROWTH = 2
    STABLE = 3


leaders = {
    "1910": "Katsura Tarō",
    "1914": "Ōkuma Shigenobu",
    "1918": "Hara Takashi",
    "1932": "Saitō Makoto",
    "1936": "Kōki Hirota",
    "1939": "Kiichirō Hiranuma"
}
monarchs = {
    "1910": "Emperor Meiji",
    "1914": "Emperor Taishō",
    "1918": "Emperor Taishō",
    "1932": "Emperor Shōwa",
    "1936": "Emperor Shōwa",
    "1939": "Emperor Shōwa"
}

population = {
    "1910": 49600000,
    "1914": 52500000,
    "1918": 55000000,
    "1932": 66300000,
    "1936": 70400000,
    "1939": 72500000
}
gdp = {
    "1910": 6366802632,
    "1914": 7851127368,
    "1918": 9901977895,
    "1932": 15995421053,
    "1936": 18197631579,
    "1939": 23894736842
}


class JapanAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "asia"
        self.name = "Japanese Empire"
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

        for i in range(len(nation_json['countries'])):
            if nation_json['countries'][i]['nation_name'] == "Japan":
                # print(retreive_coords((nation_json['countries'][i]['coordinates'])))
                self.coordinates = (retreive_coords(nation_json['countries'][i]['coordinates']))

    # main function
    def main(self, globe):
        while self.population > 2000000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            self.stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break