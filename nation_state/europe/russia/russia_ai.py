import random
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

dictators = {
    "1910": "Nicolaus II",
    "1914": "Nicolaus II",
    "1918": "Vladimir Lenin",
    "1932": "Joseph Stalin",
    "1936": "Joseph Stalin",
    "1939": "Joseph Stalin"
}

population = {
    "1910": 70980000,
    "1914": 73570000,
    "1918": 76290000,
    "1932": 86770000,
    "1936": 90020000,
    "1939": 92540000
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": 12003528421,
    "1914": 15085307368,
    "1918": 14723268421,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

flags = {"1910": "../flags/russia/Flag_of_Russia.jpg",
         "1914": "../flags/russia/Flag_of_Russia.jpg",
         "1918": "../flags/russia/Flag_of_Russia.jpg",
         "1932": "../flags/russia/Flag_of_the_Soviet_Union_(1924–1936).jpg",
         "1936": "../flags/russia/Flag_of_the_Soviet_Union_(1924–1936).jpg",
         "1939": "../flags/russia/Flag_of_the_USSR_(1936-1955).jpg"}

leader_images = {
    "1910": "../leaders/russia/800px-Mikola_II_(cropped)-2.jpg",
    "1914": "../leaders/russia/800px-Mikola_II_(cropped)-2.jpg",
    "1918": "../leaders/russia/800px-Mikola_II_(cropped)-2.jpg",
    "1932": "../leaders/russia/Joseph_Stalin,_1950_(cropped).jpg",
    "1936": "../leaders/russia/Joseph_Stalin,_1950_(cropped).jpg",
    "1939": "../leaders/russia/Joseph_Stalin,_1950_(cropped).jpg"
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class RussiaAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.spare_color = self.nation_color
        self.region = "europe"
        self.name = "Russia"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        if self.date.year <= 1918:
            self.political_typology = "Autocratic"
        else:
            self.political_typology = "Communist"

        self.leader = dictators[str(globe.date.year)]
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
            objectives_enemy = ["Contain Germany", "Contain Austria", "Contain Russia"]
            objectives_allies = ["Improve relations with France", "Improve relations with Great Britain", "Improve relations with Russia"]

        else:
            objectives_enemy = ["Contain Germany", "Contain Austria", "Contain Russia"]
            objectives_allies = ["Improve relations with Great Britain", "Improve relations with United States"]

        for enemy in objectives_enemy:
            self.objectives["objectives"][0]['foreign'].append(enemy)

        for ally in objectives_allies:
            self.objectives["objectives"][0]['foreign'].append(ally)

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        if self.date.year <= 1918:
            # Azerbaijan
            # Armenia
            for i in range(len(nation_json['countries'])):
                if (nation_json['countries'][i]['nation_name'] == "Russian Empire" or nation_json['countries'][i]['nation_name']
                        == "Finland" or nation_json['countries'][i]['nation_name'] == "Azerbaijan" or
                nation_json['countries'][i]['nation_name'] == "Armenia" or nation_json['countries'][i]['nation_name'] == "Georgia"):
                    # print(nation_json['countries'][i]['coordinates'])
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
                    print(self.coordinates)
            self.coordinates = (retreive_coords(self.coordinates))
        if self.date.year > 1918 and self.date.year < 1932:
            for i in range(len(nation_json['countries'])):
                if nation_json['countries'][i]['nation_name'] == "USSR" or nation_json['countries'][i]['nation_name']\
                        == "White Russia":
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))


        if self.date.year >= 1932:
            print('hi')
            for i in range(len(nation_json['countries'])):
                if (nation_json['countries'][i]['nation_name'] == "USSR"
                    or nation_json['countries'][i]['nation_name'] == "White Russia" or
                        nation_json['countries'][i]['nation_name'] == "Ukraine"):

                    #print(nation_json['countries'][i]['coordinates'])
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))