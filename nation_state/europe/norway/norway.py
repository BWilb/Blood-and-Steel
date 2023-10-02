import random
import time
from datetime import datetime, timedelta

from globe_relations import globe
from datetime import datetime, timedelta
from game.ai import playable_nation

leaders = {
    "1910" : "Gunnar Knudsen",
    "1914" : "Gunnar Knudsen",
    "1918" : "Gunnar Knudsen",
    "1932" : "Peder Kolstad",
    "1936" : "Johan Nygaardsvold",
    "1939" : "Johan Nygaardsvold"
}
monarchs = {
    "1910" : "Haakon VII",
    "1914" : "Haakon VII",
    "1918" : "Haakon VII",
    "1932" : "Haakon VII",
    "1936" : "Haakon VII",
    "1939" : "Haakon VII"
}

population = {
    "1910": 2352192,
    "1914": 2455604,
    "1918": 2565700,
    "1932": 2840000,
    "1936": 2910000,
    "1939": 2960000
}
gdp = {
    "1910": 176567770,
    "1914": 103520738,
    "1918": 275419359,
    "1932": 191193380,
    "1936": 234412779,
    "1939": 289281486
}

flags = {"1910": "../flags/norway/norway.jpeg",
         "1914": "../flags/norway/norway.jpeg",
         "1918": "../flags/norway/norway.jpeg",
         "1932": "../flags/norway/norway.jpeg",
         "1936": "../flags/norway/norway.jpeg",
         "1939": "../flags/norway/norway.jpeg"}

leader_images = {
    "1910": "../leaders/norway/330px-Gunnar_Knudsen_02-1914-1918.jpg",
    "1914": "../leaders/norway/330px-Gunnar_Knudsen_02-1914-1918.jpg",
    "1918": "../leaders/norway/330px-Gunnar_Knudsen_02-1914-1918.jpg",
    "1932": "../leaders/norway/Peder_Kolstad-1932.jpg",
    "1936": "../leaders/norway/1936-1939.jpeg",
    "1939": "../leaders/norway/1936-1939.jpeg"
}

class Norway(playable_nation.PlayableNation):
    def __init__(self, year):
        super().__init__(year)
        self.name = "Norway"
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
