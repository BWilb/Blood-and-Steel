import random
import time
from datetime import datetime, timedelta

from datetime import datetime, timedelta
from game.ai import playable_nation

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
    def __init__(self, year):
        super().__init__(year)
        self.region = "europe"
        self.name = "Denmark"
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
        self.monarch = monarchs[year]
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