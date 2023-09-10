import random
import time
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI


"""Population Dictionaries"""
population = {
    "1910": 2286981,
    "1914": 2618301,
    "1918": 2916220,
    "1932": 4147085,
    "1936": 4409675,
    "1939": 4620766
}

"""Political Dictionaries"""
leaders = {
    "1910": "José Miguel Gómez",
    "1914": "Mario García Menocal",
    "1918": "Mario García Menocal",
    "1932": "Gerardo Machado",
    "1936": "Federico Laredo Brú",
    "1939": "Federico Laredo Brú"
}

gdp = {
    "1910": 75000000,
    "1914": 76346343,
    "1918": 77648543,
    "1932": 76573434,
    "1936": 77346224,
    "1939": 78347343
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class CubaAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.region = "North America"
        self.name = "Republic of Cuba"
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
            self.stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break
