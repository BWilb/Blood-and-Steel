import random
import time
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI

from random_functions import random_functions

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

"""Population Dictionaries"""
population = {
    "1910": 49438166,
    "1914": 51856258,
    "1918": 52342083,
    "1932": 6692240,
    "1936": 6664400,
    "1939": None
}

"""Political Dictionaries"""
leaders = {
    "1910": "Franz Joseph",
    "1914": "Franz Joseph",
    "1918": "Otto Von Hapsburg",
    "1932": "Engelbert Dollfuss",
    "1936": "Kurt Schuschnigg",
    "1939": None
}

monarchs = {
    "1910": "Franz Joseph",
    "1914": "Franz Joseph",
    "1918": "Otto Von Habsburg",
    "1932": "Otto von Habsburg II",
    "1936": "Otto von Habsburg II",
    "1939": None
}

gdp = {
    "1910": 3406984117,
    "1914": 3644313879,
    "1918": 4174673077,
    "1932": 2118539364,
    "1936": 73462352,
    "1939": None
}

class Austria(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.region = "Europe"
        if globe.date.year < 1918:
            self.name = "Austria Hungary"
        if globe.date.year > 1918:
            self.name = "Federal Republic of Austria"
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

    # main function
    def main(self, globe):
        while self.population > 50000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break

