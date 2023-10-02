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
    def __init__(self, year):
        super().__init__(year)
        self.name = "Republic of Poland"
        # date variables
        self.date = datetime(int(year), 1, 1)
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
        self.birth_control = False
        self.birth_enhancer = False
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = leaders[year]
        self.leader_image = leader_images[year]
        self.flag = flags[year]
        """Stability"""
        self.stability = 95.56
        # economic
        self.e_s = "recovery"
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.income_tax_rate = 25.00
        self.corporate_tax_rate = 35.00
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # international
        self.alliance = ""
        # other
        self.chosen = False
