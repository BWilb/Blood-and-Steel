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
    "1910": "Ahmad Shah Qajar",
    "1914": "Ahmad Shah Qajar",
    "1918": "Ahmad Shah Qajar",
    "1932": "Reza shah",
    "1936": "Reza shah",
    "1939": "Reza shah"
}


population = {
    "1910": 10970000,
    "1914": 10320000,
    "1918": 9530000,
    "1932": 13270000,
    "1936": 14230000,
    "1939": 14970000
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

flags = {"1910": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1914": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1918": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1932": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1936": "../flags/iran/1920px-State_flag_of_Iran_(1933–1964).jpg",
         "1939": "../flags/iran/1920px-State_flag_of_Iran_(1933–1964).jpg"
         }

leader_images = {
    "1910": "../leaders/iran/330px-AhmadShahQajar2_1910-1918.jpg",
    "1914": "../leaders/iran/330px-AhmadShahQajar2_1910-1918.jpg",
    "1918": "../leaders/iran/330px-AhmadShahQajar2_1910-1918.jpg",
    "1932": "../leaders/iran/Reza_shah_uniform-1932-1939.jpg",
    "1936": "../leaders/iran/Reza_shah_uniform-1932-1939.jpg",
    "1939": "../leaders/iran/Reza_shah_uniform-1932-1939.jpg"
}

class Iran(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.region = "asia"
        self.name = "Iran"
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
        while self.population > 400000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            self.stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break
