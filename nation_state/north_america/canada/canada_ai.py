import random
import time
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

from random_functions import random_functions

"""Population Dictionaries"""
population = {
    "1910": 7041174,
    "1914": 7614382,
    "1918": 8252357,
    "1932": 10467365,
    "1936": 10927346,
    "1939": 11303434
}

"""Political Dictionaries"""
pms = {
    "1910": "Wilfrid Laurier",
    "1914": "Robert Borden",
    "1918": "Robert Borden",
    "1932": "R. B. Bennett",
    "1936": "William Mackenzie King",
    "1939": "William Mackenzie King"
}
monarchs = {
    """Dictionary for english monarchs
    Leader selection will be in sync with time frame selection
    Unlike population, leader dictionary will be setup to be as historically accurate as possible"""

    "1910": "Edward VII",
    "1914": "George V",
    "1918": "George V",
    "1932": "George V",
    "1936": "Edward VIII",
    "1939": "George VI"
}

gdp = {
    "1910": 50000000,
    "1914": 65993945,
    "1918": 73348873,
    "1932": 72348873,
    "1936": 72348873,
    "1939": 74348873
}

flags = {"1910": "../flags/canada/canada_flag_1920.jpg",
         "1914": "../flags/canada/canada_flag_1920.jpg",
         "1918": "../flags/canada/canada_flag_1920.jpg",
         "1932": "../flags/canada/Can-Red-Ensign-after-1921-green-leaves.jpg",
         "1936": "../flags/canada/Can-Red-Ensign-after-1921-green-leaves.jpg",
         "1939": "../flags/canada/Can-Red-Ensign-after-1921-green-leaves.jpg"}

leader_images = {
    "1910": "../leaders/canada/wilfred_laurier_1910.jpeg",
    "1914": "../leaders/canada/robert_borden_1914-1920.jpeg",
    "1918": "../leaders/canada/robert_borden_1914-1920.jpeg",
    "1932": "../leaders/canada/Wm_Lyon_Mackenzie_King_1932-1940.jpg",
    "1936": "../leaders/canada/Wm_Lyon_Mackenzie_King_1932-1940.jpg",
    "1939": "../leaders/canada/Wm_Lyon_Mackenzie_King_1932-1940.jpg"
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class Canada(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "North America"
        self.name = "Dominion of Canada"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = pms[str(globe.date.year)]
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

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for i in range(len(nation_json['countries'])):
            # print(nation_json['countries'][i]['nation_name'])
            if (nation_json['countries'][i]['nation_name'] == "Canada"):
                # print(nation_json['countries'][i]['coordinates'])
                self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))

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
