import random
from enum import Enum
from game.ai import playable_nation
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

leaders = {
    "1910": None,
    "1914": None,
    "1918": None,
    "1932": "Nuri al-Said",
    "1936": "Yasin al-Hashimi",
    "1939": "Yasin al-Hashimi"
}


population = {
    "1910": 2850000,
    "1914": 3090000,
    "1918": 3340000,
    "1932": 3980000,
    "1936": 4020000,
    "1939": 4080000
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": None,
    "1914": None,
    "1918": None,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

flags = {"1910": "../flags/iraq/Flag_of_Iraq_(1924–1959).jpg",
         "1914": "../flags/iraq/Flag_of_Iraq_(1924–1959).jpg",
         "1918": "../flags/iraq/Flag_of_Iraq_(1924–1959).jpg",
         "1932": "../flags/iraq/Flag_of_Iraq_(1924–1959).jpg",
         "1936": "../flags/iraq/Flag_of_Iraq_(1924–1959).jpg",
         "1939": "../flags/iraq/Flag_of_Iraq_(1924–1959).jpg"
         }

leader_images = {
    "1910": "../leaders/iraq/330px-AhmadShahQajar2_1910-1918.jpg",
    "1914": "../leaders/iraq/330px-AhmadShahQajar2_1910-1918.jpg",
    "1918": "../leaders/iraq/330px-AhmadShahQajar2_1910-1918.jpg",
    "1932": "../leaders/iraq/71nwewvdNlL.__AC_SY445_QL70_ML2_-1932.jpg",
    "1936": "../leaders/iraq/330px-Yasin_Hashimi,_1927-1936.jpg",
    "1939": "../leaders/iraq/330px-Yasin_Hashimi,_1927-1936.jpg"
}

class Iraq(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "asia"
        self.name = "Iraq"
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

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
            for i in range(0, len(nation_json['countries'])):
                if nation_json['countries'][i]['nation_name'] == "Mesopotamia (GB)":
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]