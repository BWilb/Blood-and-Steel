import sys
import time
from datetime import datetime, timedelta

from datetime import datetime, timedelta
from game.ai import playable_nation
monarchs = {
    """Dictionary for english monarchs
    Leader selection will be in sync with time frame selection
    Unlike population, leader dictionary will be setup to be as historically accurate as possible"""

    "1910": "Edward VII",
    "1914": "George V",
    "1918": "George V",
    "1932": "George V",
    "1936": "Edward VIII",
    "1939": "George VI"
}

pm = {
    "1910": "H.H. Asquith",
    "1914": "H.H. Asquith",
    "1918": "David Lloyd George",
    "1932": "Ramsay MacDonald",
    "1936": "Stanley Baldwin",
    "1939": "Neville Chamberlain"
}

spare_pms = ["Duncan Pirie", "Henry Cowan", "Harold Baker", "James Calmont", "Ellis Ellis-Griffith",
             "Charles Craig", "William Jones", "Alfred Scott", "Sir Charles Hunter"]

spare_1900_1950_monarchs = ["Louis", "Prince Arthur", "Beatrice", "Prince Henry", "Alexander Ramsay",
                            "Alexander Cambridge",
                            "Albert Victor", "Victoria II", "George VI"]

# population variables and dictionaries
population = {
    """Dictionary for population
    Population selection will be in sync with time frame selection
    Population will then be set up to grow or shrink in random amounts"""

    "1910": 44915900,
    "1914": 42956900,
    "1918": 39582000,
    "1932": 46335000,
    "1936": 47081300,
    "1939": 46029200
}

# economic variables and dictionaries
gdp = {
    "1910": 15783763158,
    "1914": 17856842105,
    "1918": 23873207895,
    "1932": 44371994737,
    "1936": 53157368421,
    "1939": 54936947368
}

flags = {
    "1910": "../flags/britain/United-Kingdom-Flag.jpg",
    "1914": "../flags/britain/United-Kingdom-Flag.jpg",
    "1918": "../flags/britain/United-Kingdom-Flag.jpg",
    "1932": "../flags/britain/United-Kingdom-Flag.jpg",
    "1936": "../flags/britain/United-Kingdom-Flag.jpg",
    "1939": "../flags/britain/United-Kingdom-Flag.jpg"
}

leader_images = {"1910": "../leaders/britain/330px-Herbert_Henry_Asquith_till_1916.jpg",
                 "1914": "../leaders/britain/330px-Herbert_Henry_Asquith_till_1916.jpg",
                 "1918": "../leaders/britain/330px-David_Lloyd_George_1916-1922.jpg",
                 "1932": "../leaders/britain/J._Ramsay_MacDonald_LCCN2014715885_(cropped)_till_1935.jpg",
                 "1936": "../leaders/britain/Stanley_Baldwin_ggbain.35233_1935_1937.jpg",
                 "1939": "../leaders/britain/chamberlain_1937-1939.jpeg"
                 }

class Britain(playable_nation.PlayableNation):
    def __init__(self, year):
        super().__init__(year)
        self.is_intact = True
        self.name = "Great Britain"
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
        self.past_population = self.population
        self.births = 0
        self.deaths = 0
        self.birth_control = False
        self.birth_enhancer = False
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = pm[year]
        self.monarch = monarchs[year]
        self.leader_image = leader_images[year]
        self.flag = flags[year]
        self.political_power = 354
        self.political_exponent = 2.76
        """Stability"""
        self.stability = 95.56
        # economic
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.economic_stimulus = False
        self.e_s = "recovery"
        self.income_tax_rate = 25.00
        self.corporate_tax_rate = 35.00
        """Components of GDP"""
        self.consumer_spending = 500
        self.investment = 400
        self.government_spending = 1200
        self.exports = 10000
        self.imports = 9500
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # international
        self.alliance = ""
        # other
        self.chosen = False