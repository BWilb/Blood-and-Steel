import random
import time
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

leaders = {
    "1910": "Mehmed V",
    "1914": "Mehmed V",
    "1918": "Mehmed V",
    "1932": "Mustafa Kemal Atatürk",
    "1936": "Mustafa Kemal Atatürk",
    "1939": "Mustafa Kemal Atatürk"
}


population = {
    "1910": 14680000,
    "1914": 14340000,
    "1918": 13890000,
    "1932": 15250000,
    "1936": 16370000,
    "1939": 17260000
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": 12003528421,
    "1914": 15085307368,
    "1918": 14723268421,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

flags = {"1910": "../flags/turkey/Flag_of_the_Ottoman_Empire_(1844–1922).jpg",
         "1914": "../flags/turkey/Flag_of_the_Ottoman_Empire_(1844–1922).jpg",
         "1918": "../flags/turkey/Flag_of_the_Ottoman_Empire_(1844–1922).jpg",
         "1932": "../flags/turkey/Flag_of_the_Ottoman_Empire_(1844–1922).jpg",
         "1936": "../flags/turkey/Flag_of_the_Ottoman_Empire_(1844–1922).jpg",
         "1939": "../flags/turkey/Flag_of_the_Ottoman_Empire_(1844–1922).jpg"
         }

leader_images = {
    "1910": "../leaders/turkey/Sultan_Muhammed_Chan_V.,_Kaiser_der_Osmanen_1915_C._Pietzner-1918.jpg",
    "1914": "../leaders/turkey/Sultan_Muhammed_Chan_V.,_Kaiser_der_Osmanen_1915_C._Pietzner-1918.jpg",
    "1918": "../leaders/turkey/Sultan_Muhammed_Chan_V.,_Kaiser_der_Osmanen_1915_C._Pietzner-1918.jpg",
    "1932": "../leaders/turkey/Ataturk1930s-1939.jpg",
    "1936": "../leaders/turkey/Ataturk1930s-1939.jpg",
    "1939": "../leaders/turkey/Ataturk1930s-1939.jpg"
}

class TurkeyAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.region = "asia"
        if globe.date.year < 1921:
            self.name = "Ottoman Empire"
        if globe.date.year > 1921:
            self.name = "Republic of Turkey"
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