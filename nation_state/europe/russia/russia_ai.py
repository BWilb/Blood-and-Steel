import random
import time
from datetime import datetime, timedelta
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
alternate_monarchs = ["Olga I", "Peter of Oldenburg", "Nikolai III", "Alexandra I",
                      "Olga II", "Tatiana", "Maria", "Anastasia", "Alexei"]

lenin_successors = ["Leon Trotsky", "Joseph Stalin", "Vladimir Milyutin", "Nikolai Krylenko",
                    "Pavel Dybenko", "Alexei Rykov", "Anatoly Lunacharsky"]

stalin_successors = ["Vyacheslav Molotov", "Anastas Mikoyan", "Lavrentiy Beria", "Nikolai Bulganin", "Georgy Malenkov",]

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
        self.leader = dictators[str(globe.date.year)]
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
        """self.foreign_relations = {
            "Austria": 77.67,
            "Great Britain": 89.56,
            "Kingdom of Denmark": 80.56,
            "Republic of France": 88.45,
            "Germany": 75.56,
            "Kingdom of Greece": 80.56,
            "Kingdom of Italy": 88.00,
            "Kingdom of Luxembourg": 94.56,
            "Kingdom of Netherlands": 92.34,
            "Kingdom of Norway": 88.88,
            "Poland": 90.56,
            "Kingdom of Romania": 91.24,
            "Kingdom of Belgium": 88.45,
            "Kingdom of Sweden": 85.56,
            "Republic of Switzerland": 100,
            "Dominion of Canada": 98.56,
            "Republic of Cuba": 100,
            "Republic of Mexico": 89.98,
            "Afghanistan": 89.45,
            "Iran": 88.23,
            "Iraq": 89.12,
            "Turkey": 78.45,
            "China": 82.34,
            "Japanese Empire": 75.67,
            "Brazil": 56.65,
            "Venezuela": 86.45,
            "Argentina": 67.45
        }"""
    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
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

    # main function
    def main(self, globe, network, user_nation):
        #super().establishing_beginning_objectives()
        while self.population > 2000000:
            super().check_economic_growth(globe.date)
            super().check_population_growth()
            super().political_power_growth()
            super().stability_happiness_change(globe)
            #super().determine_diplomatic_approach(globe.nations, globe, network, user_nation)
            super().change_relations(globe.nations)
            chance = random.randrange(1, 50)
            if chance % 8 == 2 or chance % 5 == 4:
                super().protests()
            super().pop_growth()
            super().check_economic_state(globe.date)
            self.date += timedelta(days=1)
            break
