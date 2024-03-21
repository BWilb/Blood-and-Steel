import random
import time
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
from nation_data.coordination.retreive_and_convert import retreive_coords
import json as js


"""Population Dictionaries"""
population = {
    "1910": 2286981,
    "1914": 2578301,
    "1918": 2906220,
    "1932": 4087085,
    "1936": 4379675,
    "1939": 4610766
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

flags = {
    "1910": "../flags/cuba/cuba.jpeg",
    "1914": "../flags/cuba/cuba.jpeg",
    "1918": "../flags/cuba/cuba.jpeg",
    "1932": "../flags/cuba/cuba.jpeg",
    "1936": "../flags/cuba/cuba.jpeg",
    "1939": "../flags/cuba/cuba.jpeg"
}
leader_images = {"1910": "../leaders/cuba/Gral_de_División_José_Miguel_Gomez_Gomez_1910.jpeg",
                 "1914": "../leaders/cuba/mario-garca-menocal-1866-1941-granger_1914-1918.jpg",
                 "1918": "../leaders/cuba/mario-garca-menocal-1866-1941-granger_1914-1918.jpg",
                 "1932": "../leaders/cuba/330px-Gmachado_1932.jpg",
                 "1936": "../leaders/cuba/1936.png",
                 "1939": "../leaders/cuba/1939.jpeg"
                 }

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class CubaAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "North America"
        self.name = "Cuba"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.political_typology = "Autocratic"
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.political_power = 200
        self.political_exponent = 1.56
        self.current_gdp = gdp[str(globe.date.year)]
        """Components of GDP"""
        self.consumer_spending = 200
        self.investment = 300
        self.government_spending = 350
        self.exports = 1000
        self.imports = 1200

        self.coordinates = []

        self.foreign_relations = {"foreign relations": []}

    def establish_foreign_objectives(self):
        objectives_enemy = ['']
        objectives_allies = ["Improve relations with Russia", "Improve relations with Great Britain",
                             "Improve Relations with United States",
                             "Improve relations with Mexico", "Improve relations with France",
                             "Improve relations with Netherlands",
                             "Improve relations with Belgium", "Improve relations with Canada"]
        for enemy in objectives_enemy:
            self.objectives["objectives"][0]['foreign'].append(enemy)

        for ally in objectives_allies:
            self.objectives["objectives"][0]['foreign'].append(ally)
    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for i in range(len(nation_json['countries'])):
            print(nation_json['countries'][i]['nation_name'])
            if nation_json['countries'][i]['nation_name'] == "Cuba":
                # print(nation_json['countries'][i]['coordinates'])
                self.coordinates = [((nation_json['countries'][i]['coordinates']))]
        self.coordinates = [(retreive_coords(self.coordinates))]
