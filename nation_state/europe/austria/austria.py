from datetime import datetime, timedelta
from game.ai import playable_nation
from nation_data.coordination.retreive_and_convert import retreive_coords
import json as js

"""Population Dictionaries"""
population = {
    "1910": 49438166,
    "1914": 51856258,
    "1918": 52342083,
    "1932": 6692240,
    "1936": 6664400,
    "1939": 0
}

"""Political Dictionaries"""
leaders = {
    "1910": "Franz Joseph",
    "1914": "Franz Joseph",
    "1918": "Otto Von Hapsburg",
    "1932": "Engelbert Dollfuss",
    "1936": "Kurt Schuschnigg",
    "1939": "Hubert Pierlot"
}

monarchs = {
    "1910": "Franz Joseph",
    "1914": "Franz Joseph",
    "1918": "Otto Von Habsburg",
    "1932": "Otto von Habsburg II",
    "1936": "Otto von Habsburg II",
    "1939": None
}

gdp = {
    "1910": 3406984117,
    "1914": 3644313879,
    "1918": 4174673077,
    "1932": 2118539364,
    "1936": 73462352,
    "1939": 0
}
flags = {
    "1910": "../flags/austria/Flag_of_the_Habsburg_Monarchy.jpg",
    "1914": "../flags/austria/Flag_of_the_Habsburg_Monarchy.jpg",
    "1918": "../flags/austria/Flag_of_the_Habsburg_Monarchy.jpg",
    "1932": "../flags/austria/Flag_of_Austria_1932.jpg",
    "1936": "../flags/austria/State_flag_of_Austria_(1934–1938).jpg",
    "1939": "../flags/austria/Standarte_Adolf_Hitlers.jpg"
}
leader_images = {"1910": "../leaders/austria/joseph_ii.jpeg",
                 "1914": "../leaders/austria/joseph_ii.jpeg",
                 "1918": "../leaders/austria/charles_i.jpg",
                 "1932": "../leaders/austria/miklas.jpeg",
                 "1936": "../leaders/austria/miklas.jpeg",
                 "1939": "../leaders/austria/adolf-hitler-10253.jpg"
                 }

class Austria(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "austria"
        # date variables
        self.date = datetime(globe.date.year, 1, 1)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        self.births = 0
        self.deaths = 0
        # political
        self.leader = leaders[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        # economic
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp
        self.land_1910_1918 = ["Austro-Hungarian Empire"]
        self.land_1932 = ["Austria"]
        self.coordinates = []

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        if self.date.year <= 1918:
            for land in range(0, len(self.land_1910_1918)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1910_1918[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = [(retreive_coords(self.coordinates))]

        if self.date.year > 1918:
            for land in range(0, len(self.land_1932)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1932[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = [(retreive_coords(self.coordinates))]