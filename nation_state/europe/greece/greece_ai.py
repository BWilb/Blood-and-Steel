import random
import time
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

flags = {"1910": "../flags/greece/Flag_of_Greece.jpg",
         "1914": "../flags/greece/Flag_of_Greece.jpg",
         "1918": "../flags/greece/Flag_of_Greece.jpg",
         "1932": "../flags/greece/Flag_of_Greece.jpg",
         "1936": "../flags/greece/Flag_of_Greece.jpg",
         "1939": "../flags/greece/Flag_of_Greece.jpg"}

leader_images = {
    "1910": "../leaders/greece/george_i.jpeg",
    "1914": "../leaders/greece/constantine_i_1914-1918.jpeg",
    "1918": "../leaders/greece/King_Alexander_of_Greece_1918.jpg",
    "1932": "../leaders/greece/330px-Zaimis37216v_1932.jpg",
    "1936": "../leaders/greece/Georgeiiofgreece_1936-1939.jpg",
    "1939": "../leaders/greece/Georgeiiofgreece_1936-1939.jpg"
}

"""Population Dictionaries"""
population = {
    "1910": 5370000,
    "1914": 5520000,
    "1918": 5680000,
    "1932": 6590000,
    "1936": 6960000,
    "1939": 7240000
}

"""Political Dictionaries"""
leaders = {
    "1910": "Stephanos Dragoumis",
    "1914": "Eleftherios Venizelos",
    "1918": "Eleftherios Venizelos",
    "1932": "Eleftherios Venizelos",
    "1936": "Ioannis Metaxas",
    "1939": "Ioannis Metaxas"
}

monarchs = {
    "1910": "George I",
    "1914": "Constantine I",
    "1918": "Alexander",
    "1932": "Alexandros Zaimis",
    "1936": "George II",
    "1939": "George II"
}

gdp = {
    "1910": 340698411,
    "1914": 364431387,
    "1918": 417467307,
    "1932": 98539364,
    "1936": 103462352,
    "1939": 113434839
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class Greece(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Kingdom of Greece"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.political_typology = "Autocratic"
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
        self.land = ["Greece"]
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
    def main(self, globe, network):
        super().establishing_beginning_objectives()
        while self.population > 2000000:
            super().check_economic_growth(globe.date)
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            super().political_power_growth()
            super().determine_diplomatic_approach(globe.nations, globe, network)
            super().change_relations(globe.nations)
            chance = random.randrange(1, 50)
            if chance % 8 == 2 or chance % 5 == 4:
                super().protests()
            self.date += timedelta(days=1)
            break
