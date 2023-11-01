import random
import time
from datetime import datetime, timedelta
from nation_data.coordination.retreive_and_convert import retreive_coords
import json as js
from game.ai.nation_ai import NationAI
import os
chancellors = {
    "1910": "Theobald von Bethmann Hollweg",
    "1914": "Theobald von Bethmann Hollweg",
    "1918": "Friedrich Ebert",
    "1932": "Kurt von Schleicher",
    "1936": "Adolf Hitler",
    "1939": "Adolf Hitler"
}

kaisers = {
    "1910": "Wilhelm II",
    "1914": "Wilhelm II",
    "1918": "None",
    "1932": "None",
    "1936": "None",
    "1939": "None"
}
"""Dictionary for population
    Population selection will be in sync with time frame selection
    Population will then be set up to grow or shrink in random amounts"""
population = {

    "1910": 64060000,
    "1914": 64030000,
    "1918": 63310000,
    "1932": 68180000,
    "1936": 70130000,
    "1939": 71500000
}

# economic variables and dictionaries
gdp = {
    "1910": 15783763158,
    "1914": 17856842105,
    "1918": 23873207895,
    "1932": 44371994737,
    "1936": 53157368421,
    "1939": 54936947368
}
flags = {"1910": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1914": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1918": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1932": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1936": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1939": "../flags/japan/Flag_of_Japan_(1870–1999).jpg"}

leader_images = {
    "1910": "../leaders/germany/holleg_1917.jpeg",
    "1914": "../leaders/germany/holleg_1917.jpeg",
    "1918": "../leaders/germany/von_herling-1918.jpg",
    "1932": "../leaders/germany/bruning-1932.jpg",
    "1936": "../leaders/germany/hitler-1936-1945.jpg",
    "1939": "../leaders/germany/hitler-1936-1945.jpg"
}

class GermanAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.spare_color = self.nation_color
        self.region = "europe"
        self.name = "Germany"
        self.date = datetime(globe.date.year, 1, 1)
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = chancellors[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        if globe.date.year <= 1918:
            self.political_typology = "Autocratic"
        else:
            self.political_typology = "Fascist"
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
        self.land_1910_1914 = ["German Empire", "German South-West Africa", "German E. Africa (Tanganyika)",
                               "French Cameroons"]
        self.land_1918 = ["German Empire"]
        self.land_1932_1936 = ["Germany", "East Prussia"]
        self.land_1939 = ["Germany", "East Prussia", "Czechoslovakia"]

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        if self.date.year <= 1914:
            for land in range(0, len(self.land_1910_1914)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1910_1914[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year == 1918:
            for land in range(0, len(self.land_1918)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1918[land] == nation_json['countries'][i]['nation_name']:
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
    def main(self, globe, network):
        #super().establishing_beginning_objectives()
        while self.population > 2000000:
            """super().check_economic_growth(globe.date)
                        super().check_population_growth()
                        # random_functions.random_functions(self, globe)
                        super().stability_happiness_change(globe)
                        super().political_power_growth()
                        super().determine_diplomatic_approach(globe.nations, globe, network)
                        super().change_relations(globe.nations)
                        chance = random.randrange(1, 50)
                        if chance % 8 == 2 or chance % 5 == 4:
                            super().protests()"""
            super().pop_growth()
            super().check_economic_state(globe.date)
            self.date += timedelta(days=1)
            break
