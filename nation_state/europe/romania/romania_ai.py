import random
from datetime import timedelta
from enum import Enum
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

from game.ai.nation_ai import NationAI

# Romania
"""Population Dictionaries"""
population = {
    "1910": 11830000,
    "1914": 12040000,
    "1918": 12230000,
    "1932": 14470000,
    "1936": 15170000,
    "1939": 15680000
}

"""Political Dictionaries"""
leaders = {
    "1910": "Ion I. C. Brătianu",
    "1914": "Ion I. C. Brătianu",
    "1918": "Ion I. C. Brătianu",
    "1932": "Nicolae Iorga",
    "1936": "Gheorghe Tătărescu",
    "1939": "rmand Călinescu"
}

monarchs = {
    "1910": "Carol I",
    "1914": "Carol I",
    "1918": "Ferdinand I",
    "1932": "Carol II",
    "1936": "Carol II",
    "1939": "Carol II"
}

gdp = {
    "1910": 11882323232,
    "1914": 11982323232,
    "1918": 12182323232,
    "1932": 14212323232,
    "1936": 18882323232,
    "1939": 19882323232
}

flags = {"1910": "../flags/romania/romania.jpeg",
         "1914": "../flags/romania/romania.jpeg",
         "1918": "../flags/romania/romania.jpeg",
         "1932": "../flags/romania/romania.jpeg",
         "1936": "../flags/romania/romania.jpeg",
         "1939": "../flags/romania/romania.jpeg"}

leader_images = {
    "1910": "../leaders/romania/Carp_(The_Road_to_Romanian_Independence)_1910.jpeg",
    "1914": "../leaders/romania/IonelBratianu3b40761r_1914-1918.jpg",
    "1918": "../leaders/romania/IonelBratianu3b40761r_1914-1918.jpg",
    "1932": "../leaders/romania/Iorga_at_his_desk_Luceaferul_2,_1914-1932.jpg",
    "1936": "../leaders/romania/255px-Gheorghe_Tătărescu-1936.jpg",
    "1939": "../leaders/romania/Miron_Cristia_patriach_of_Romania-1939.jpeg"
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class RomaniaAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Romania"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
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
            objectives_enemy = ["Contain Germany", "Contain Turkey", "Contain Austria"]
            objectives_allies = ["Improve relations with France", "Improve relations with Russia", "Improve relations with United States",
                                 "Improve relations with Belgium", "Improve relations with Luxembourg"]

        else:
            objectives_enemy = ["Contain Hungary", "Contain Russia", "Contain Bulgaria"]
            objectives_allies = [""]

        for enemy in objectives_enemy:
            self.objectives["objectives"][0]['foreign'].append(enemy)

        for ally in objectives_allies:
            self.objectives["objectives"][0]['foreign'].append(ally)

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        for i in range(len(nation_json['countries'])):
            if (nation_json['countries'][i]['nation_name'] == "Romania"):
                self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]

        return self.coordinates
