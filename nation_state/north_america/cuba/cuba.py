from datetime import datetime, timedelta
from enum import Enum
from game.ai import playable_nation
from nation_data.coordination.retreive_and_convert import retreive_coords
import json as js
"""Population Dictionaries"""
population = {
    "1910": 2286981,
    "1914": 2578301,
    "1918": 2906220,
    "1932": 4087085,
    "1936": 4379675,
    "1939": 4610766
}

"""Political Dictionaries"""
leaders = {
    "1910": "José Miguel Gómez",
    "1914": "Mario García Menocal",
    "1918": "Mario García Menocal",
    "1932": "Gerardo Machado",
    "1936": "Federico Laredo Brú",
    "1939": "Federico Laredo Brú"
}

gdp = {
    "1910": 75000000,
    "1914": 76346343,
    "1918": 77648543,
    "1932": 76573434,
    "1936": 77346224,
    "1939": 78347343
}

flags = {
    "1910": "../flags/cuba/cuba.jpeg",
    "1914": "../flags/cuba/cuba.jpeg",
    "1918": "../flags/cuba/cuba.jpeg",
    "1932": "../flags/cuba/cuba.jpeg",
    "1936": "../flags/cuba/cuba.jpeg",
    "1939": "../flags/cuba/cuba.jpeg"
}
leader_images = {"1910": "../leaders/cuba/Gral_de_División_José_Miguel_Gomez_Gomez_1910.jpeg",
                 "1914": "../leaders/cuba/mario-garca-menocal-1866-1941-granger_1914-1918.jpg",
                 "1918": "../leaders/cuba/mario-garca-menocal-1866-1941-granger_1914-1918.jpg",
                 "1932": "../leaders/cuba/330px-Gmachado_1932.jpg",
                 "1936": "../leaders/cuba/1936.png",
                 "1939": "../leaders/cuba/1939.jpeg"
                 }

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class Cuba(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "Cuba"
        # date variables
        self.date = datetime(globe.date.year, 1, 1)
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        self.births = 0
        self.deaths = 0
        # political
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for i in range(len(nation_json['countries'])):
            print(nation_json['countries'][i]['nation_name'])
            if nation_json['countries'][i]['nation_name'] == "Cuba":
                # print(nation_json['countries'][i]['coordinates'])
                self.coordinates = [((nation_json['countries'][i]['coordinates']))]
        self.coordinates = [(retreive_coords(self.coordinates))]