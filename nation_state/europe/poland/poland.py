import random
import time
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from game.ai import playable_nation
leaders = {
    "1910": None,
    "1914": None,
    "1918": "Józef Piłsudski",
    "1932": "Ignacy Mościcki",
    "1936": "Ignacy Mościcki",
    "1939": "Ignacy Mościcki"
}

population = {
    "1910": None,
    "1914": None,
    "1918": 10128121,
    "1932": 13962629,
    "1936": 14620667,
    "1939": 15128000
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": None,
    "1914": None,
    "1918": 14723268421,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

flags = {"1910": None,
         "1914": None,
         "1918": "../flags/poland/Flag_of_Poland_(1919–1927).jpg",
         "1932": "../flags/poland/Flag_of_Poland_(1919–1927).jpg",
         "1936": "../flags/poland/Flag_of_Poland_(1919–1927).jpg",
         "1939": "../flags/poland/Flag_of_Poland_(1919–1927).jpg"}

leader_images = {
    "1910": None,
    "1914": None,
    "1918": "../leaders/poland/Józef_Piłsudski_(-1930)-1918.jpg",
    "1932": "../leaders/poland/Moscicki-1932-1939.jpg",
    "1936": "../leaders/poland/Moscicki-1932-1939.jpg",
    "1939": "../leaders/poland/Moscicki-1932-1939.jpg"
}


class Poland(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "Republic of Poland"
        # date variables
        self.date = datetime(globe.year, 1, 1)
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
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
