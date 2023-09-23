import random
from datetime import timedelta
from enum import Enum
from nation_data.coordination.retreive_and_convert import retreive_coords, convert_coords
import json as js

from game.ai.nation_ai import NationAI
import geopandas as grosdp

"""Population Dictionaries"""
population = {
    "1910": 5893247,
    "1914": 6274226,
    "1918": 6687933,
    "1932": 8052797,
    "1936": 8441838,
    "1939": 8788112
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

grosdp = {
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
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Kingdom of Netherlands"
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
        self.current_gdp = grosdp[str(globe.date.year)]
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
            if nation_json['countries'][i]['nation_name'] == "Netherlands":
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

