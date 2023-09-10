import random
import time
from datetime import datetime, timedelta
from enum import Enum

from game.ai.nation_ai import NationAI

leaders = {
    "1910" : "Segismundo Moret",
    "1914" : "Eduardo Dato",
    "1918" : "Manuel García Prieto",
    "1932" : "Niceto Alcalá-Zamora",
    "1936" : "Manuel Azaña",
    "1939" : "Manuel Azaña"
}
monarchs = {
    "1910" : "Alfonso XIII",
    "1914" : "Alfonso XIII",
    "1918" : "Alfonso XIII",
    "1932" : "Henri VII/Jacques II",
    "1936" : "Henri VII/Jacques II",
    "1939" : "Henri VII/Jacques II"
}

population = {
    "1910": 19681917,
    "1914": 20250331,
    "1918": 20790497,
    "1932": 23812074,
    "1936": 24628744,
    "1939": 24892000
}
gdp = {
    "1910": 2159663720,
    "1914": 2547024746,
    "1918": 5653286406,
    "1932": 2940653248,
    "1936": 3978738880,
    "1939": 4366978929
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


class SpainAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.region = "europe"
        self.name = "Kingdom of Spain"
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
            self.stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break
