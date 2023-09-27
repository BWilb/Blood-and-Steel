import random
from datetime import timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

leaders = {
    "1910" : "Paul Eyschen",
    "1914" : "Paul Eyschen",
    "1918" : "Léon Kauffman",
    "1932" : "Pierre Dupong",
    "1936" : "Pierre Dupong",
    "1939" : "Pierre Dupong"
}
monarchs = {
    "1910" : "Guillaume IV",
    "1914" : "Marie-Adélaïde",
    "1918" : "Marie-Adélaïde",
    "1932" : "Charlotte",
    "1936" : "Charlotte",
    "1939" : "Charlotte"
}

population = {
    "1910": 225970,
    "1914": 246026,
    "1918": 267135,
    "1932": 354988,
    "1936": 387357,
    "1939": 410366
}
gdp = {
    "1910": 465966372,
    "1914": 484702474,
    "1918": 495328640,
    "1932": 503740350,
    "1936": 522800000,
    "1939": 703789473
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class LuxembourgAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Kingdom of Luxembourg"
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
        self.land = ["Luxembourg"]
    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for land in range(0, len(self.land)):
            for i in range(0, len(nation_json['countries'])):
                if self.land[land] == nation_json['countries'][i]['nation_name']:
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]

    # main function
    def main(self, globe):
        while self.population > 100000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break
