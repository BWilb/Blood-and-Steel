import json as js
from datetime import datetime, timedelta
from nation_data.coordination.retreive_and_convert import retreive_coords
from game.ai import playable_nation

leader_images = {
    "1910": "",
    "1914": "",
    "1918": "",
    "1932": "../leaders/estonia/330px-Konstantin_Pats_1934.jpg",
    "1936": "../leaders/estonia/330px-Konstantin_Pats_1934.jpg",
    "1939": "../leaders/estonia/330px-Konstantin_Pats_1934.jpg"
}
flags = {
    "1910": "../flags/estonia/Flag_of_Estonia.svg.jpg",
    "1914": "../flags/estonia/Flag_of_Estonia.svg.jpg",
    "1918": "../flags/estonia/Flag_of_Estonia.svg.jpg",
    "1932": "../flags/estonia/Flag_of_Estonia.svg.jpg",
    "1936": "../flags/estonia/Flag_of_Estonia.svg.jpg",
    "1939": "../flags/estonia/Flag_of_Estonia.svg.jpg"
}

leaders = {
    "1910" : None,
    "1914" : None,
    "1918" : "Konstantin Päts",
    "1932" : "Konstantin Päts",
    "1936" : "Konstantin Päts",
    "1939" : "Kaarel Eenpalu"
}

population = {
    "1910": 984000,
    "1914": 1030000,
    "1918": 1090000,
    "1932": 1120000,
    "1936": 1120000,
    "1939": 1120000
}
gdp = {
    "1910": 4659663,
    "1914": 4847024,
    "1918": 4953286,
    "1932": 5037403,
    "1936": 5228000,
    "1939": 7037894
}

class Estonia(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.region = "europe"
        self.name = "Estonia"
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
                if nation_json['countries'][i]['nation_name'] == "Estonia":
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]