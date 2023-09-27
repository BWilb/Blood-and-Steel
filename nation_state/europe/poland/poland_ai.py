import random
import time
from datetime import timedelta, datetime
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

leaders = {
    "1910": None,
    "1914": None,
    "1918": "Józef Piłsudski",
    "1932": "Ignacy Mościcki",
    "1936": "Ignacy Mościcki",
    "1939": "Ignacy Mościcki"
}

population = {
    "1910": None,
    "1914": None,
    "1918": 10128121,
    "1932": 13962629,
    "1936": 14620667,
    "1939": 15128000
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": None,
    "1914": None,
    "1918": 14723268421,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

class PolandAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Kingdom of Belgium"
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
        self.coordinates = []
        self.land = ["Poland"]

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for land in range(0, len(self.land)):
            for i in range(0, len(nation_json['countries'])):
                if self.land[land] == nation_json['countries'][i]['nation_name']:
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))

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
