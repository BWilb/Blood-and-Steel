import time
from datetime import datetime, timedelta
import random
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class PopulationState(Enum):
    LOW_GROWTH = 1
    HIGH_GROWTH = 2
    STABLE = 3

leaders = {
    "1910": "Katsura Tarō",
    "1914": "Ōkuma Shigenobu",
    "1918": "Hara Takashi",
    "1932": "Saitō Makoto",
    "1936": "Kōki Hirota",
    "1939": "Kiichirō Hiranuma"
}
monarchs = {
    "1910": "Emperor Meiji",
    "1914": "Emperor Taishō",
    "1918": "Emperor Taishō",
    "1932": "Emperor Shōwa",
    "1936": "Emperor Shōwa",
    "1939": "Emperor Shōwa"
}

population = {
    "1910": 49880000,
    "1914": 52340000,
    "1918": 54930000,
    "1932": 66390000,
    "1936": 69870000,
    "1939": 72630000
}
gdp = {
    "1910": 6366802632,
    "1914": 7851127368,
    "1918": 9901977895,
    "1932": 15995421053,
    "1936": 18197631579,
    "1939": 23894736842
}

flags = {"1910": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1914": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1918": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1932": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1936": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1939": "../flags/japan/Flag_of_Japan_(1870–1999).jpg"}

leader_images = {
    "1910": "../leaders/japan/330px-11_KatsuraT-1910.jpg",
    "1914": "../leaders/japan/330px-Gonbee_Yamamoto_later_years-1914.jpg",
    "1918": "../leaders/japan/330px-Masatake_Terauchi_2-1918.jpg",
    "1932": "../leaders/japan/Inukai_Tsuyoshi-1932.jpg",
    "1936": "../leaders/japan/Prime_Minister_Keisuke_Okada-1936.jpg",
    "1939": "../leaders/japan/Fumimaro_Konoe(cropped)-1939.jpg"
}

class JapanAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "asia"
        self.name = "Japan"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        if globe.date.year <= 1932:
            self.political_typology = "Autocratic"

        else:
            self.political_typology = "Fascist"
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
        # other
        self.coordinates = []
        self.foreign_relations = {"foreign relations": []}

    def establish_foreign_objectives(self):
        if self.date.year <= 1918:
            objectives_enemy = ["Contain Germany", "Contain Turkey", "Contain Austria", "Contain Bulgaria"]
            objectives_allies = ["Improve relations with France", "Improve relations with Russia",
                                 "Improve relations with United States",
                                 "Improve relations with Great Britain", "Improve relations with Belgium"]
            for enemy in objectives_enemy:
                self.objectives["objectives"][0]['foreign'].append(enemy)

            for ally in objectives_allies:
                self.objectives["objectives"][0]['foreign'].append(ally)

        else:
            objectives_enemy = ["Contain France", "Contain Great Britain", "Contain Russia", "Contain United States",
                                "Contain Belgium",
                                "Contain Netherlands", "Contain Mexico"]
            objectives_allies = ["Improve relations with Germany", "Improve relations with Hungary",
                                 "Improve relations with Italy"]

            for enemy in objectives_enemy:
                self.objectives["objectives"][0]['foreign'].append(enemy)

            for ally in objectives_allies:
                self.objectives["objectives"][0]['foreign'].append(ally)

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for i in range(len(nation_json['countries'])):
            # print(nation_json['countries'][i]['nation_name'])
            if (nation_json['countries'][i]['nation_name'] == "Empire of Japan"):
                # print(nation_json['countries'][i]['coordinates'])
                self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))

