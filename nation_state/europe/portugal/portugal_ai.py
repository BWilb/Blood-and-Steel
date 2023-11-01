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
    "1910": 5850000,
    "1914": 5930000,
    "1918": 5990000,
    "1932": 6940000,
    "1936": 7300000,
    "1939": 7570000
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

gdp = {
    "1910": 50000000,
    "1914": 65993945,
    "1918": 73348873,
    "1932": 72348873,
    "1936": 72348873,
    "1939": 74348873
}

flags = {"1910": "../flags/portugal/Flag_of_Portugal.svg.jpg",
         "1914": "../flags/portugal/Flag_of_Portugal.svg.jpg",
         "1918": "../flags/portugal/Flag_of_Portugal.svg.jpg",
         "1932": "../flags/portugal/Flag_of_Portugal.svg.jpg",
         "1936": "../flags/portugal/Flag_of_Portugal.svg.jpg",
         "1939": "../flags/portugal/Flag_of_Portugal.svg.jpg"}

leader_images = {
    "1910": "../leaders/portugal/1910.png",
    "1914": "../leaders/portugal/1914.png",
    "1918": "../leaders/portugal/1918.png",
    "1932": "../leaders/portugal/1932-1939.jpg",
    "1936": "../leaders/portugal/1932-1939.jpg",
    "1939": "../leaders/portugal/1932-1939.jpg"
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class Portugal(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Portugal"
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
            if (nation_json['countries'][i]['nation_name'] == "Portugal" or
            nation_json['countries'][i]['nation_name'] == "Angola (Portugal)" or
            nation_json['countries'][i]['nation_name'] == "Mozambique (Portugal)"):
                # print(nation_json['countries'][i]['coordinates'])
                self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))

    # main function
    def main(self, globe, network):
       # super().establishing_beginning_objectives()
        while self.population > 2000000:
            """super().check_economic_growth(globe.date)
                        super().check_population_growth()
                        # random_functions.random_functions(self, globe)
                        super().stability_happiness_change(globe)
                        super().political_power_growth()
                        super().determine_diplomatic_approach(globe.nations, globe, network)
                        super().change_relations(globe.nations)
                        chance = random.randrange(1, 50)
                        if chance % 8 == 2 or chance % 5 == 4:
                            super().protests()"""
            super().pop_growth()
            super().check_economic_state(globe.date)
            self.date += timedelta(days=1)
            break
