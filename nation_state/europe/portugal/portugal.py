import json as js
import random
from game.ai import playable_nation
from nation_data.coordination.retreive_and_convert import retreive_coords
"""Population Dictionaries"""
population = {
    "1910": 5850000,
    "1914": 5930000,
    "1918": 5990000,
    "1932": 6940000,
    "1936": 7300000,
    "1939": 7570000
}

"""Political Dictionaries"""
pms = {
    "1910": "Wilfrid Laurier",
    "1914": "Robert Borden",
    "1918": "Robert Borden",
    "1932": "R. B. Bennett",
    "1936": "William Mackenzie King",
    "1939": "William Mackenzie King"
}

gdp = {
    "1910": 50000000,
    "1914": 65993945,
    "1918": 73348873,
    "1932": 72348873,
    "1936": 72348873,
    "1939": 74348873
}

flags = {"1910": "../flags/portugal/Flag_of_Portugal.svg.jpg",
         "1914": "../flags/portugal/Flag_of_Portugal.svg.jpg",
         "1918": "../flags/portugal/Flag_of_Portugal.svg.jpg",
         "1932": "../flags/portugal/Flag_of_Portugal.svg.jpg",
         "1936": "../flags/portugal/Flag_of_Portugal.svg.jpg",
         "1939": "../flags/portugal/Flag_of_Portugal.svg.jpg"}

leader_images = {
    "1910": "../leaders/portugal/1910.png",
    "1914": "../leaders/portugal/1914.png",
    "1918": "../leaders/portugal/1918.png",
    "1932": "../leaders/portugal/1932-1939.jpg",
    "1936": "../leaders/portugal/1932-1939.jpg",
    "1939": "../leaders/portugal/1932-1939.jpg"
}

class Portugal(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Portugal"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        if self.date.year == 1910 or self.date.year >= 1932:
            self.political_typology = "Autocratic"

        elif 1914 > self.date.year < 1932:
            self.political_typology = "Democratic"

        self.leader = pms[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.political_power = 200
        self.political_exponent = 1.56
        self.current_gdp = gdp[str(globe.date.year)]
        # other
        self.coordinates = []
        self.foreign_relations = {"foreign relations": []}

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for i in range(len(nation_json['countries'])):
            # print(nation_json['countries'][i]['nation_name'])
            if (nation_json['countries'][i]['nation_name'] == "Portugal" or
            nation_json['countries'][i]['nation_name'] == "Angola (Portugal)" or
            nation_json['countries'][i]['nation_name'] == "Mozambique (Portugal)"):
                # print(nation_json['countries'][i]['coordinates'])
                self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))