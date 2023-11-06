import random

from datetime import datetime, timedelta
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords
flags = {"1910": "../flags/united_states/Flag_of_the_United_States_(1908–1912).jpg",
         "1914": "../flags/united_states/Flag_of_the_United_States_(1912-1959).jpg",
         "1918": "../flags/united_states/Flag_of_the_United_States_(1912-1959).jpg",
         "1932": "../flags/united_states/Flag_of_the_United_States_(1912-1959).jpg",
         "1936": "../flags/united_states/Flag_of_the_United_States_(1912-1959).jpg",
         "1939": "../flags/united_states/Flag_of_the_United_States_(1912-1959).jpg"}

leader_images = {
    "1910": "../leaders/united_states/taft-1913.jpeg",
    "1914": "../leaders/united_states/wilson-1914-1918.jpg",
    "1918": "../leaders/united_states/wilson-1914-1918.jpg",
    "1932": "../leaders/united_states/President_Hoover_portrait-1932.jpg",
    "1936": "../leaders/united_states/fdr-1936-1939.jpg",
    "1939": "../leaders/united_states/fdr-1936-1939.jpg"
}
"""Population Dictionaries"""

population = {
    "1910": 90150000,
    "1914": 95530000,
    "1918": 100970000,
    "1932": 121860000,
    "1936": 125320000,
    "1939": 128160000
}
presidents = {
    "1910": "William Howard Taft",
    "1914": "Woodrow Wilson",
    "1918": "Woodrow Wilson",
    "1932": "Herbert Hoover",
    "1936": "Franklin D. Roosevelt",
    "1939": "Franklin D. Roosevelt"
}
gdp = {
    "1910": 50000000,
    "1914": 65993945,
    "1918": 73348873,
    "1932": 72348873,
    "1936": 72348873,
    "1939": 74348873
}

vice_presidents = {
    # dictionary of vice presidents incase president gets assassinated
    "1910": "James S. Sherman",
    "1914": "Thomas R. Marshall",
    "1918": "Thomas R. Marshall",
    "1932": "Charles Curtis",
    "1936": "John Garner",
    "1939": "Henry Wallace"
}

class USAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "North America"
        self.name = "United States"
        self.date = datetime(globe.date.year, 1, 1)
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = presidents[str(globe.date.year)]
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
        self.foreign_relations = {"foreign relations": [
            {"nation name": "Afghanistan",
             "relations": 60.56,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Iran",
             "relations": 70.56,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Iraq",
             "relations": 65.56,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Turkey",
             "relations": 57.56,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "China",
             "relations": 67.46,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Austria",
             "relations": 87.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Russia",
             "relations": 75.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Great Britain",
             "relations": 78.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Belgium",
             "relations": 68.34,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Bulgaria",
             "relations": 78.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Estonia",
             "relations": 48.34,
             "relation status": "enemy",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "France",
             "relations": 76.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Germany",
             "relations": 34.34,
             "relation status": "enemy",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Greece",
             "relations": 65.34,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Hungary",
             "relations": 48.34,
             "relation status": "enemy",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Denmark",
             "relations": 75.34,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Latvia",
             "relations": 66.65,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Lithuania",
             "relations": 48.34,
             "relation status": "enemy",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Luxembourg",
             "relations": 88.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Netherlands",
             "relations": 88.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Norway",
             "relations": 78.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Poland",
             "relations": 54.45,
             "relation status": "enemy",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Italy",
             "relations": 58.34,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Romania",
             "relations": 78.94,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Spain",
             "relations": 65.34,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Sweden",
             "relations": 75.54,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Switzerland",
             "relations": 98.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Canada",
             "relations": 88.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Portugal",
             "relations": 78.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Mexico",
             "relations": 79.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Cuba",
             "relations": 76.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Argentina",
             "relations": 74.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Bolivia",
             "relations": 65.45,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Brazil",
             "relations": 76.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Chile",
             "relations": 79.56,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Columbia",
             "relations": 72.34,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Peru",
             "relations": 74.54,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False},

            {"nation name": "Venezuela",
             "relations": 74.54,
             "relation status": "ally",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False}
        ]}

    def establish_foreign_objectives(self):
        objectives_enemy = ['Contain Germany', "Contain Japan"]

        objectives_allies = ["Improve relations with France",
                             "Improve relations with Mexico",
                             "Improve relations with Great Britain"]
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
                #print(nation_json['countries'][i]['nation_name'])
                if (nation_json['countries'][i]['nation_name'] == "United States" or
                        nation_json['countries'][i]['nation_name'] == "Philippines"):
                    # print(nation_json['countries'][i]['coordinates'])
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
            if globe.date > self.date_checker:
                super().determine_diplomatic_approach(globe, network, user_nation)
                self.date_checker = globe.date + timedelta(days=3)
            super().change_relations(globe.nations)
            chance = random.randrange(1, 50)
            if chance % 8 == 2 or chance % 5 == 4:
                super().protests()
            super().pop_growth()
            super().check_economic_state(globe.date)
            self.date += timedelta(days=1)
            break