import random
import time
from datetime import datetime, timedelta
from enum import Enum
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

from game.ai.nation_ai import NationAI

leaders = {
    "1910" : "Arvid Lindman",
    "1914" : "Karl Staaff",
    "1918" : "Nils Edén",
    "1932" : "Carl Gustaf Ekman",
    "1936" : "Per Albin Hansson",
    "1939" : "Per Albin Hansson"
}
monarchs = {
    "1910" : "Gustaf V",
    "1914" : "Gustaf V",
    "1918" : "Gustaf V",
    "1932" : "Gustaf V",
    "1936" : "Gustaf V",
    "1939" : "Gustaf V"
}

population = {
    "1910": 5493302,
    "1914": 5619111,
    "1918": 5746841,
    "1932": 6172343,
    "1936": 6259363,
    "1939": 6335505
}
gdp = {
    "1910": 1765677700,
    "1914": 1035207385,
    "1918": 2754193594,
    "1932": 1911933808,
    "1936": 2344127797,
    "1939": 2892814865
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


class SwedenAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Kingdom of Sweden"
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
    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for i in range(len(nation_json['countries'])):
            if nation_json['countries'][i]['nation_name'] == "Sweden":
                return retreive_coords(nation_json['countries'][i]['coordinates'])
    # main function
    def main(self, globe):
        while self.population > 2000000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)

            self.date += timedelta(days=1)
            break
