import random
from datetime import datetime, timedelta
from game.ai import playable_nation
from nation_data.coordination.retreive_and_convert import retreive_coords
import json as js

"""Population Dictionaries"""
population = {
    "1910": 2713555,
    "1914": 2905149,
    "1918": 3122049,
    "1932": 3600000,
    "1936": 3720000,
    "1939": 3810000
}

"""Political Dictionaries"""
leaders = {
    "1910": "Carl Theodor Zahle",
    "1914": "Carl Theodor Zahle",
    "1918": "Carl Theodor Zahle",
    "1932": "Thorvald Stauning",
    "1936": "Thorvald Stauning",
    "1939": "Thorvald Stauning"
}

monarchs = {
    "1910": "Frederick VIII",
    "1914": "Christian IX",
    "1918": "Christian IX",
    "1932": "Christian IX",
    "1936": "Christian IX",
    "1939": "Christian IX"
}

gdp = {
    "1910": 75000000,
    "1914": 76346343,
    "1918": 77648543,
    "1932": 76573434,
    "1936": 77346224,
    "1939": 78347343
}

flags = {"1910": "../flags/denmark/Flag_of_Denmark.jpg",
         "1914": "../flags/denmark/Flag_of_Denmark.jpg",
         "1918": "../flags/denmark/Flag_of_Denmark.jpg",
         "1932": "../flags/denmark/Flag_of_Denmark.jpg",
         "1936": "../flags/denmark/Flag_of_Denmark.jpg",
         "1939": "../flags/denmark/Flag_of_Denmark.jpg"}

leader_images = {
    "1910": "../leaders/denmark/Ke019217_1910.jpg",
    "1914": "../leaders/denmark/Ke019217_1910.jpg",
    "1918": "../leaders/denmark/Ke019217_1910.jpg",
    "1932": "../leaders/denmark/stauning_1932--1939.jpeg",
    "1936": "../leaders/denmark/stauning_1932--1939.jpeg",
    "1939": "../leaders/denmark/stauning_1932--1939.jpeg"
}

class Denmark(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "Denmark"
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
        self.e_s = "recovery"
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        self.improving_relations = []
        self.worsening_relations = []
        # drawing
        self.coordinates = []
        # other
        self.land = ["Denmark", "Iceland"]

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        for land in range(0, len(self.land)):
            for i in range(0, len(nation_json['countries'])):
                if self.land[land] == nation_json['countries'][i]['nation_name']:
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))
