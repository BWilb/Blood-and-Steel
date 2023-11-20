import json as js
from datetime import datetime, timedelta
from game.ai import playable_nation
from nation_data.coordination.retreive_and_convert import retreive_coords

"""Population Dictionaries"""
population = {
    "1910": 5893247,
    "1914": 6274226,
    "1918": 6687933,
    "1932": 8052797,
    "1936": 8441838,
    "1939": 8788112
}

"""Political Dictionaries"""
leaders = {
    "1910": "Theo Heemskerk",
    "1914": "Pieter Cort van der Linden",
    "1918": "Pieter Cort van der Linden",
    "1932": "Charles Ruijs de Beerenbrouck",
    "1936": "Hendrikus Colijn",
    "1939": "Hendrikus Colijn"
}

monarchs = {
    "1910": "Wilhelmina",
    "1914": "Wilhelmina",
    "1918": "Wilhelmina",
    "1932": "Wilhelmina",
    "1936": "Wilhelmina",
    "1939": "Wilhelmina"
}

gdp = {
    "1910": 865645049,
    "1914": 1111426098,
    "1918": 1844390540,
    "1932": 2118539364,
    "1936": 3213537630,
    "1939": 3201339327
}

flags = {
    "1910": "../flags/netherlands/vector-illustration-of-netherlands-flag.jpg",
    "1914": "../flags/netherlands/vector-illustration-of-netherlands-flag.jpg",
    "1918": "../flags/netherlands/vector-illustration-of-netherlands-flag.jpg",
    "1932": "../flags/netherlands/vector-illustration-of-netherlands-flag.jpg",
    "1936": "../flags/netherlands/vector-illustration-of-netherlands-flag.jpg",
    "1939": "../flags/netherlands/vector-illustration-of-netherlands-flag.jpg"
}

leader_images = {"1910": "../leaders/netherlands/skirmer_1910.png",
                 "1914": "../leaders/netherlands/250px-Pieter_Cort_van_der_Linden_1914-1918.jpg",
                 "1918": "../leaders/netherlands/250px-Pieter_Cort_van_der_Linden_1914-1918.jpg",
                 "1932": "../leaders/netherlands/Beerenbrouck_1932.jpg",
                 "1936": "../leaders/netherlands/Hendrik_Colijn_(1925)_1936-1939.jpg",
                 "1939": "../leaders/netherlands/Hendrik_Colijn_(1925)_1936-1939.jpg"
                 }

class Netherlands(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.region = "europe"
        self.name = "Netherlands"
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
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp
        self.coordinates = []
        self.land = ["Dutch East Indies", "Netherlands", "Netherlands Antilles"]

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for land in range(0, len(self.land)):
            for i in range(0, len(nation_json['countries'])):
                if self.land[land] == nation_json['countries'][i]['nation_name']:
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))