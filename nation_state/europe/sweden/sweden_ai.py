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
    "1910" : "Gustaf V",
    "1914" : "Gustaf V",
    "1918" : "Gustaf V",
    "1932" : "Gustaf V",
    "1936" : "Gustaf V",
    "1939" : "Gustaf V"
}

population = {
    "1910": 5460000,
    "1914": 5639111,
    "1918": 5846841,
    "1932": 6192343,
    "1936": 6289363,
    "1939": 6355505
}
gdp = {
    "1910": 1765677700,
    "1914": 1035207385,
    "1918": 2754193594,
    "1932": 1911933808,
    "1936": 2344127797,
    "1939": 2892814865
}

leader_images = {
    "1910": "../leaders/sweden/330px-Arvid_Lindman_1910.jpg",
    "1914": "../leaders/sweden/Karl_Staaff_1914.jpg",
    "1918": "../leaders/sweden/Nils_Eden_1918.jpg",
    "1932": "../leaders/sweden/330px-Carl_Gustaf_Ekman_1932.jpg",
    "1936": "../leaders/sweden/330px-Per_Albin_Hansson_-_Sveriges_styresmän_1936-1939.jpg",
    "1939": "../leaders/sweden/330px-Per_Albin_Hansson_-_Sveriges_styresmän_1936-1939.jpg"
}
flags = {
    "1910": "../flags/sweden/Flag_of_Sweden.jpg",
    "1914": "../flags/sweden/Flag_of_Sweden.jpg",
    "1918": "../flags/sweden/Flag_of_Sweden.jpg",
    "1932": "../flags/sweden/Flag_of_Sweden.jpg",
    "1936": "../flags/sweden/Flag_of_Sweden.jpg",
    "1939": "../flags/sweden/Flag_of_Sweden.jpg"
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


class SwedenAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Sweden"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.political_typology = "Democratic"
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
        self.land = ['Sweden']
        self.coordinates = []

        self.foreign_relations = {"foreign relations": []}

    def establish_foreign_objectives(self):
        if self.date.year > 1918:
            objectives_enemy = ["Contain Germany", "Contain Italy", "Contain Russia"]
            objectives_allies = ["Improve relations with Great Britain", "Improve relations with United States",
                                 "Improve relations with France", "Improve relations with Denmark", "Improve relations with Norway"]

            for enemy in objectives_enemy:
                self.objectives["objectives"][0]['foreign'].append(enemy)

            for ally in objectives_allies:
                self.objectives["objectives"][0]['foreign'].append(ally)

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        if self.date.year >= 1918:
            for land in range(0, len(self.land)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year == 1932:
            for land in range(0, len(self.land)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append(nation_json['countries'][i]['coordinates'])
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year == 1936:
            for land in range(0, len(self.land)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land[land] == nation_json['countries'][i]['nation_name']:
                        #print(nation_json['countries'][i]['coordinates'])
                        self.coordinates.append(nation_json['countries'][i]['coordinates'])
            coordinates = retreive_coords(self.coordinates)
            print(coordinates)
            self.coordinates.clear()
            self.coordinates += coordinates

        if self.date.year >= 1939:
            for land in range(0, len(self.land)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))