import json as js
from datetime import datetime, timedelta
from game.ai import playable_nation
from nation_data.coordination.retreive_and_convert import retreive_coords

leader_images = {
    "1910": "",
    "1914": "",
    "1918": "",
    "1932": "../leaders/hungary/OIP.jpg",
    "1936": "../leaders/hungary/OIP.jpg",
    "1939": "../leaders/hungary/OIP.jpg"
}
flags = {
    "1910": "../flags/hungary/Flag_of_Hungary_(1915-1918,_1919-1946).svg.jpg",
    "1914": "../flags/hungary/Flag_of_Hungary_(1915-1918,_1919-1946).svg.jpg",
    "1918": "../flags/hungary/Flag_of_Hungary_(1915-1918,_1919-1946).svg.jpg",
    "1932": "../flags/hungary/Flag_of_Hungary_(1915-1918,_1919-1946).svg.jpg",
    "1936": "../flags/hungary/Flag_of_Hungary_(1915-1918,_1919-1946).svg.jpg",
    "1939": "../flags/hungary/Flag_of_Hungary_(1915-1918,_1919-1946).svg.jpg"
}

"""Population Dictionaries"""
population = {
    "1910": 49438166,
    "1914": 51856258,
    "1918": 52342083,
    "1932": 8760497,
    "1936": 9008500,
    "1939": 9192000
}

"""Political Dictionaries"""
leaders = {
    "1910": "Franz Joseph",
    "1914": "Franz Joseph",
    "1918": "Mihály Károlyi",
    "1932": "Miklós Horthy",
    "1936": "Miklós Horthy",
    "1939": "Miklós Horthy"
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
    "1932": 98539364,
    "1936": 103462352,
    "1939": 113434839
}

class Hungary(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
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
        self.monarch = monarchs[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        """Stability"""
        self.stability = 95.56
        # economic
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp
        # other
        self.coordinates = []

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
            for i in range(0, len(nation_json['countries'])):
                if nation_json['countries'][i]['nation_name'] == "Hungary":
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]