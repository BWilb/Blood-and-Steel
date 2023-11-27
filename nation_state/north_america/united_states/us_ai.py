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
    "1910": 893980000000,
    "1914": 905130000000,
    "1918": 1100000000000,
    "1932": 1050000000000,
    "1936": 1360000000000,
    "1939": 1470000000000
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
        self.political_typology = "Democratic"
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
        self.foreign_relations = {"foreign relations": []}

    def establish_foreign_objectives(self):
        if self.date.year <= 1918:
            objectives_enemy = ["Contain Germany", "Contain Austria", "Contain Turkey", "Contain Bulgaria"]
            objectives_allies = ["Improve relations with Russia", "Improve relations with Great Britain",
                                 "Improve Relations with Canada",
                                 "Improve relations with Mexico", "Improve relations with France",
                                 "Improve relations with Netherlands",
                                 "Improve relations with Belgium"]
            for enemy in objectives_enemy:
                self.objectives["objectives"][0]['foreign'].append(enemy)

            for ally in objectives_allies:
                self.objectives["objectives"][0]['foreign'].append(ally)

        else:
            objectives_enemy = ["Contain Germany", "Contain Hungary", "Contain Italy", "Contain Japan"]
            objectives_allies = ["Improve relations with Russia", "Improve relations with Great Britain",
                                 "Improve Relations with Canada",
                                 "Improve relations with Mexico", "Improve relations with France",
                                 "Improve relations with Belgium",
                                 "Improve relations with Netherlands"]

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