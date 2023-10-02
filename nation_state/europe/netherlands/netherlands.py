import random
import time
from datetime import datetime, timedelta

from globe_relations import globe
from datetime import datetime, timedelta
from game.ai import playable_nation

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
    def __init__(self, year):
        super().__init__(year)
        self.region = "europe"
        self.name = "Netherlands"
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
        self.income_tax_rate = 25.00
        self.corporate_tax_rate = 35.00
        self.e_s = "recovery"
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
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