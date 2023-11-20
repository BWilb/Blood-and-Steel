import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords
from datetime import datetime, timedelta
from game.ai import playable_nation
leaders = {
    "1910" : "Robert Comtesse",
    "1914" : "Arthur Hoffmann",
    "1918" : "Felix Calonder",
    "1932" : "Giuseppe Motta",
    "1936" : "Albert Meyer",
    "1939" : "Philipp Etter"
}

population = {
    "1910": 3585751,
    "1914": 3695000,
    "1918": 3818000,
    "1932": 4111500,
    "1936": 4156167,
    "1939": 4184833
}
gdp = {
    "1910": 1765677700,
    "1914": 1975776780,
    "1918": 2021174168,
    "1932": 1595825500,
    "1936": 2443434342,
    "1939": 2061627844
}

class Switzerland(playable_nation.PlayableNation):
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
        self.population = population[year]
        self.births = 0
        self.deaths = 0
        # political
        self.leader = leaders[year]

        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.coordinates = []

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        for i in range(len(nation_json['countries'])):
            if (nation_json['countries'][i]['nation_name'] == "Switzerland"):
                self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))