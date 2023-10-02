import random
import time
from collections import OrderedDict
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from game.ai import playable_nation

"""Population Dictionaries"""
population = {
    "1910": 7041174,
    "1914": 7674382,
    "1918": 8302357,
    "1932": 10477365,
    "1936": 10957346,
    "1939": 11413434
}

"""Political Dictionaries"""
pms = {
    "1910": "Wilfrid Laurier",
    "1914": "Robert Borden",
    "1918": "Robert Borden",
    "1932": "R. B. Bennett",
    "1936": "William Mackenzie King",
    "1939": "William Mackenzie King"
}

gdp = {
    "1910": 50000000,
    "1914": 65993945,
    "1918": 73348873,
    "1932": 72348873,
    "1936": 72348873,
    "1939": 74348873
}

flags = {"1910": "../flags/canada/canada_flag_1920.jpg",
         "1914": "../flags/canada/canada_flag_1920.jpg",
         "1918": "../flags/canada/canada_flag_1920.jpg",
         "1932": "../flags/canada/Can-Red-Ensign-after-1921-green-leaves.jpg",
         "1936": "../flags/canada/Can-Red-Ensign-after-1921-green-leaves.jpg",
         "1939": "../flags/canada/Can-Red-Ensign-after-1921-green-leaves.jpg"}

leader_images = {
    "1910": "../leaders/canada/wilfred_laurier_1910.jpeg",
    "1914": "../leaders/canada/robert_borden_1914-1920.jpeg",
    "1918": "../leaders/canada/robert_borden_1914-1920.jpeg",
    "1932": "../leaders/canada/Wm_Lyon_Mackenzie_King_1932-1940.jpg",
    "1936": "../leaders/canada/Wm_Lyon_Mackenzie_King_1932-1940.jpg",
    "1939": "../leaders/canada/Wm_Lyon_Mackenzie_King_1932-1940.jpg"
}

class Canada(playable_nation.PlayableNation):
    def __init__(self, year):
        super().__init__(year)
        self.is_intact = True
        self.name = "Canada"
        # date variables
        self.date = datetime(int(year), 1, 1)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        self.economic_stimulus = self.date
        self.economic_change_date = self.date + timedelta(days=60)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[year]
        self.birth_enhancer = False
        self.birth_control = False
        self.births = 0
        self.deaths = 0
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = pms[year]
        self.leader_image = leader_images[year]
        """Stability"""
        self.stability = 95.56
        self.flag = flags[year]
        # economic
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.e_s = "recovery"
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
        """general"""