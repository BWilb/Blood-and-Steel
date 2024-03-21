import random
import time
from datetime import datetime, timedelta
from game.ai import playable_nation
from nation_data.coordination.retreive_and_convert import convert_coords, retreive_coords
import json as js

"""Population Dictionaries"""
population = {
    "1910": 7395408,
    "1914": 7447647,
    "1918": 7355778,
    "1932": 8118461,
    "1936": 8210392,
    "1939": 8280500
}
"""Political Dictionaries"""
leaders = {
    "1910": "Frans Schollaert",
    "1914": "Charles de Broqueville",
    "1918": "Charles de Broqueville",
    "1932": "Jules Renkin",
    "1936": "Paul van Zeeland",
    "1939": "Hubert Pierlot"
}

monarchs = {
    "1910": "Albert I",
    "1914": "Albert I",
    "1918": "Albert I",
    "1932": "Albert I",
    "1936": "Leopold III",
    "1939": "Leopold III"
}

gdp = {
    "1910": 865645049,
    "1914": 1111426098,
    "1918": 1844390540,
    "1932": 2118539364,
    "1936": 3213537630,
    "1939": 3201339327
}

flags = {"1910": "../flags/belgium/belgian_flag.jpg",
         "1914": "../flags/belgium/belgian_flag.jpg",
         "1918": "../flags/belgium/belgian_flag.jpg",
         "1932": "../flags/belgium/belgian_flag.jpg",
         "1936": "../flags/belgium/belgian_flag.jpg",
         "1939": "../flags/belgium/belgian_flag.jpg"}
leader_images = {
    "1910": "../leaders/belgium/Schollaert_1910.jpg",
    "1914": "../leaders/belgium/800px-Comte_de_Broqueville_1914-1918.jpg",
    "1918": "../leaders/belgium/800px-Comte_de_Broqueville_1914-1918.jpg",
    "1932": "../leaders/belgium/800px-Comte_de_Broqueville_1914-1918.jpg",
    "1936": "../leaders/belgium/Paul_van_Zeeland,_1936.jpg",
    "1939": "../leaders/belgium/375px-Hubert_Pierlot_1939.jpg"
}

class Belgium(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "Belgium"
        self.nation_color = (0, random.randrange(0, 255), random.randrange(0, 250))
        # date variables
        self.date = datetime(globe.date.year, 1, 1)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        self.economic_change_date = self.date + timedelta(days=60)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
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
        self.political_typology = "Democratic"
        # economic
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp
        # relations
        self.improving_relations = []
        self.worsening_relations = []
        # drawing
        self.coordinates = []
        self.land_1910_1918 = ["Belgium", "Belgian Congo"]
        self.land_1932_1939 = ["Belgium", "Belgian Congo", "Rwanda (Belgium)", "Burundi"]

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        if self.date.year < 1932:
            for land in range(0, len(self.land_1910_1918)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1910_1918[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year >= 1932:
            for land in range(0, len(self.land_1932_1939)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1932_1939[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

