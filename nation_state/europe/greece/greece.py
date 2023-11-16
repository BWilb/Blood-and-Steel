import random
from datetime import datetime, timedelta
from game.ai import playable_nation
from nation_data.coordination.retreive_and_convert import retreive_coords
import json as js

def establish_foreign_nations(globe, *args):
    """labelling second parameter as *args, due to unknown number of nations that will be sent into this function"""
    for i in range(0, len(args)):
        globe.nations.append(args[i])

"""Population Dictionaries"""
population = {
    "1910": 4510644,
    "1914": 4716335,
    "1918": 5680000,
    "1932": 6590000,
    "1936": 6960000,
    "1939": 7240000
}

"""Political Dictionaries"""
leaders = {
    "1910": "Stephanos Dragoumis",
    "1914": "Eleftherios Venizelos",
    "1918": "Eleftherios Venizelos",
    "1932": "Eleftherios Venizelos",
    "1936": "Ioannis Metaxas",
    "1939": "Ioannis Metaxas"
}

monarchs = {
    "1910": "George I",
    "1914": "Constantine I",
    "1918": "Alexander",
    "1932": "Alexandros Zaimis",
    "1936": "George II",
    "1939": "George II"
}

gdp = {
    "1910": 340698411,
    "1914": 364431387,
    "1918": 417467307,
    "1932": 98539364,
    "1936": 103462352,
    "1939": 113434839
}
flags = {"1910": "../flags/greece/Flag_of_Greece.jpg",
         "1914": "../flags/greece/Flag_of_Greece.jpg",
         "1918": "../flags/greece/Flag_of_Greece.jpg",
         "1932": "../flags/greece/Flag_of_Greece.jpg",
         "1936": "../flags/greece/Flag_of_Greece.jpg",
         "1939": "../flags/greece/Flag_of_Greece.jpg"}

leader_images = {
    "1910": "../leaders/greece/george_i.jpeg",
    "1914": "../leaders/greece/constantine_i_1914-1918.jpeg",
    "1918": "../leaders/greece/King_Alexander_of_Greece_1918.jpg",
    "1932": "../leaders/greece/330px-Zaimis37216v_1932.jpg",
    "1936": "../leaders/greece/Georgeiiofgreece_1936-1939.jpg",
    "1939": "../leaders/greece/Georgeiiofgreece_1936-1939.jpg"
}

class Greece(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "Greece"
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
        self.land = ["Greece"]

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for land in range(0, len(self.land)):
            for i in range(0, len(nation_json['countries'])):
                if self.land[land] == nation_json['countries'][i]['nation_name']:
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))
