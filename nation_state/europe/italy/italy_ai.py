"""Political variables and dictionaries"""
import random
from datetime import datetime, timedelta
import time
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

leader_images = {
    "1910": "../leaders/italy/Sidney_sonnino_1910.jpg",
    "1914": "../leaders/italy/giolitti_1914.jpg",
    "1918": "../leaders/italy/Flag_of_Greece.jpg",
    "1932": "../leaders/italy/220px-Benito_Mussolini_uncolored.jpg",
    "1936": "../leaders/italy/220px-Benito_Mussolini_uncolored.jpg",
    "1939": "../leaders/italy/220px-Benito_Mussolini_uncolored.jpg"
}
flags = {
    "1910": "../flags/italy/Flag_of_Italy_(1861-1946)_crowned.jpg",
    "1914": "../flags/italy/Flag_of_Italy_(1861-1946)_crowned.jpg",
    "1918": "../flags/italy/Flag_of_Italy_(1861-1946)_crowned.jpg",
    "1932": "../flags/italy/Flag_of_Italy_(1861-1946)_crowned.jpg",
    "1936": "../flags/italy/Flag_of_Italy_(1861-1946)_crowned.jpg",
    "1939": "../flags/italy/Flag_of_Italy_(1861-1946)_crowned.jpg"
}

prime_ministers = {
    "1910": "Luigi Luzzatti",
    "1914": "Antonio Salandra",
    "1918": "Vittorio Emanuele Orlando",
    "1932": "Benito Mussolini",
    "1936": "Benito Mussolini",
    "1939": "Benito Mussolini"
}

monarchs = {
    "1910": "Victor Emmanuel III",
    "1914": "Victor Emmanuel III",
    "1918": "Victor Emmanuel III",
    "1932": "Victor Emmanuel III",
    "1936": "Victor Emmanuel III",
    "1939": "Victor Emmanuel III"
}
"""Economic variables and dictionaries"""
gdp = {
    "1910": 7243560000,
    "1914": 7294052632,
    "1918": 7318292632,
    "1932": 12072684211,
    "1936": 15920315789,
    "1939": 19837894737
}

"""Population variables and dictionaries"""
population = {
    "1910": 35940000,
    "1914": 36360000,
    "1918": 36660000,
    "1932": 40840000,
    "1936": 42230000,
    "1939": 43280000
}


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class ItalyAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Kingdom of Italy"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = prime_ministers[str(globe.date.year)]
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
        self.land_1910 = ["Kingfom of Italy", "Eritrea"]
        self.land_1914 = ["Kingfom of Italy", "Eritrea", "Libya"]
        self.land_1932_1936 = ["Eritrea", "Italy", "Italian Somaliland"]
        self.land_1939 = ["Eritrea (Italy)", "Ethiopia (Italy)", "Italy", "Italian Somaliland", "Libya"]
    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        if self.date.year <= 1914:
            for land in range(0, len(self.land_1914)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1914[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year == 1932 or self.date.year == 1936:
            for land in range(0, len(self.land_1932_1936)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1932_1936[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year >= 1939:
            for land in range(0, len(self.land_1939)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1939[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

    # main function
    def main(self, globe):
        while self.population > 2000000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break
