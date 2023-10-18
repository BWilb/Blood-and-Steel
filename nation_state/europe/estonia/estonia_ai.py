import random
import time
from datetime import datetime, timedelta
import json as js
from game.ai.nation_ai import NationAI
from nation_data.coordination.retreive_and_convert import retreive_coords
from enum import Enum

leader_images = {
    "1910": "",
    "1914": "",
    "1918": "",
    "1932": "../leaders/estonia/330px-Konstantin_Pats_1934.jpg",
    "1936": "../leaders/estonia/330px-Konstantin_Pats_1934.jpg",
    "1939": "../leaders/estonia/330px-Konstantin_Pats_1934.jpg"
}
flags = {
    "1910": "../flags/estonia/Flag_of_Estonia.svg.jpg",
    "1914": "../flags/estonia/Flag_of_Estonia.svg.jpg",
    "1918": "../flags/estonia/Flag_of_Estonia.svg.jpg",
    "1932": "../flags/estonia/Flag_of_Estonia.svg.jpg",
    "1936": "../flags/estonia/Flag_of_Estonia.svg.jpg",
    "1939": "../flags/estonia/Flag_of_Estonia.svg.jpg"
}

leaders = {
    "1910" : None,
    "1914" : None,
    "1918" : "Konstantin Päts",
    "1932" : "Konstantin Päts",
    "1936" : "Konstantin Päts",
    "1939" : "Kaarel Eenpalu"
}

population = {
    "1910": 984000,
    "1914": 1030000,
    "1918": 1090000,
    "1932": 1120000,
    "1936": 1120000,
    "1939": 1120000
}
gdp = {
    "1910": 4659663,
    "1914": 4847024,
    "1918": 4953286,
    "1932": 5037403,
    "1936": 5228000,
    "1939": 7037894
}

class EstoniaAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Hungary"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        if globe.date.year < 1932:
            self.political_typology = ""
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

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
            for i in range(0, len(nation_json['countries'])):
                if nation_json['countries'][i]['nation_name'] == "Estonia":
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]

    def main(self, globe):
        while self.population > 100000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break