import random
import time
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI

from random_functions import random_functions

"""Population Dictionaries"""
population = {
    "1910": 7041174,
    "1914": 7674382,
    "1918": 8302357,
    "1932": 10477365,
    "1936": 10957346,
    "1939": 11413434
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

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class Canada(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.region = "North America"
        self.name = "Dominion of Canada"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = pms[str(globe.date.year)]
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
