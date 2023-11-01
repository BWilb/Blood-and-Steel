import random
import time
from datetime import datetime, timedelta
from enum import Enum
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords
from game.ai.nation_ai import NationAI

leaders = {
    "1910" : "Arvid Lindman",
    "1914" : "Karl Staaff",
    "1918" : "Nils Edén",
    "1932" : "Carl Gustaf Ekman",
    "1936" : "Per Albin Hansson",
    "1939" : "Per Albin Hansson"
}
monarchs = {
    "1910" : "Haakon VII",
    "1914" : "Haakon VII",
    "1918" : "Haakon VII",
    "1932" : "Haakon VII",
    "1936" : "Haakon VII",
    "1939" : "Haakon VII"
}

population = {
    "1910": 2400000,
    "1914": 2490000,
    "1918": 2600000,
    "1932": 2850000,
    "1936": 2920000,
    "1939": 2970000
}
gdp = {
    "1910": 176567770,
    "1914": 103520738,
    "1918": 275419359,
    "1932": 191193380,
    "1936": 234412779,
    "1939": 289281486
}

flags = {"1910": "../flags/norway/norway.jpeg",
         "1914": "../flags/norway/norway.jpeg",
         "1918": "../flags/norway/norway.jpeg",
         "1932": "../flags/norway/norway.jpeg",
         "1936": "../flags/norway/norway.jpeg",
         "1939": "../flags/norway/norway.jpeg"}

leader_images = {
    "1910": "../leaders/norway/330px-Gunnar_Knudsen_02-1914-1918.jpg",
    "1914": "../leaders/norway/330px-Gunnar_Knudsen_02-1914-1918.jpg",
    "1918": "../leaders/norway/330px-Gunnar_Knudsen_02-1914-1918.jpg",
    "1932": "../leaders/norway/Peder_Kolstad-1932.jpg",
    "1936": "../leaders/norway/1936-1939.jpeg",
    "1939": "../leaders/norway/1936-1939.jpeg"
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class NorwayAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Kingdom of Norway"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
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
        self.land = ["Norway"]
        self.coordinates = []
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

