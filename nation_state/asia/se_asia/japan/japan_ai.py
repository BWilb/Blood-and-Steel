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
        self.name = "Japanese Empire"
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
        self.coordinates = []
    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for i in range(len(nation_json['countries'])):
            # print(nation_json['countries'][i]['nation_name'])
            if (nation_json['countries'][i]['nation_name'] == "Empire of Japan"):
                # print(nation_json['countries'][i]['coordinates'])
                self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))

    # main function
    def main(self, globe):
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