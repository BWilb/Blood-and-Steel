import random
import time
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI

"""Population Dictionaries"""
population = {
    "1910": 39446500,
    "1914": 39364666,
    "1918": 39213999,
    "1932": 41349803,
    "1936": 40478600,
    "1939": 39726646
}

"""Political Dictionaries"""
leaders = {
    "1910": "Armand Fallières",
    "1914": "Raymond Poincaré",
    "1918": "Raymond Poincaré",
    "1932": "Albert Lebrun",
    "1936": "Albert Lebrun",
    "1939": "Albert Lebrun"
}

gdp = {
    "1910": 7893726221,
    "1914": 8926821140,
    "1918": 13427143793,
    "1932": 10660656638,
    "1936": 14707806582,
    "1939": 11957073084
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class FranceAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.region = "europe"
        self.name = "Republic of France"
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
        while self.population > 2000000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break

