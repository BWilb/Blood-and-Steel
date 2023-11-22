import random
import time
from datetime import datetime, timedelta
from enum import Enum
from game.ai import playable_nation
from nation_data.coordination.retreive_and_convert import retreive_coords
import json as js


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

leaders = {
    "1910": "Ahmad Shah Qajar",
    "1914": "Ahmad Shah Qajar",
    "1918": "Ahmad Shah Qajar",
    "1932": "Reza shah",
    "1936": "Reza shah",
    "1939": "Reza shah"
}


population = {
    "1910": 5500000,
    "1914": 7120000,
    "1918": 9530000,
    "1932": 6410000,
    "1936": 6410000,
    "1939": 6430000
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

flags = {"1910": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1914": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1918": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1932": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1936": "../flags/iran/1920px-State_flag_of_Iran_(1933–1964).jpg",
         "1939": "../flags/iran/1920px-State_flag_of_Iran_(1933–1964).jpg"
         }

leader_images = {
    "1910": "../leaders/iran/330px-AhmadShahQajar2_1910-1918.jpg",
    "1914": "../leaders/iran/330px-AhmadShahQajar2_1910-1918.jpg",
    "1918": "../leaders/iran/330px-AhmadShahQajar2_1910-1918.jpg",
    "1932": "../leaders/iran/Reza_shah_uniform-1932-1939.jpg",
    "1936": "../leaders/iran/Reza_shah_uniform-1932-1939.jpg",
    "1939": "../leaders/iran/Reza_shah_uniform-1932-1939.jpg"
}

class Afghanistan(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "asia"
        self.name = "Afghanistan"
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
        """Economic"""
        self.current_gdp = gdp[str(globe.date.year)]
        """Components of GDP"""
        self.consumer_spending = 200
        self.investment = 300
        self.government_spending = 350
        self.exports = 1000
        self.imports = 1200
        # other
        self.coordinates = []

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        for i in range(len(nation_json['countries'])):
            if (nation_json['countries'][i]['nation_name'] == "Afghanistan"):
                # print(retreive_coords((nation_json['countries'][i]['coordinates'])))
                self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]
