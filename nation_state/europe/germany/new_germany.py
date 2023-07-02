import globe
import arcade
import os
import random
import time
from datetime import datetime, timedelta
from administrative_regions import prussia, bavaria, wurttemburg, saxony, alsace_lorraine, baden

"""Population Dictionaries"""
population = {
    "1910": 63200000,
    "1914": 63200000,
    "1918": 62400000,
    "1932": 67200000,
    "1936": 69100000,
    "1939": 70500000
}

"""Political Dictionaries"""
chancellors = {
    "1910": "Theobald von Bethmann Hollweg",
    "1914": "Theobald von Bethmann Hollweg",
    "1918": "Friedrich Ebert",
    "1932": "Kurt von Schleicher",
    "1936": "Adolf Hitler",
    "1939": "Adolf Hitler"
}

kaisers = {
    "1910": "Wilhelm II",
    "1914": "Wilhelm II",
    "1918": "None",
    "1932": "None",
    "1936": "None",
    "1939": "None"
}
# establishing populace and economy of germany based off of inner administrative districts
def establish_initial_stats(germany):
    for state in germany.regions:
        germany.current_pop += state.current_pop
        germany.current_gdp += state.current_gdp
        germany.stability += state.stability
        germany.happiness += state.happiness

# establishing districts of germany
def establish_districts(germany):
    folder = "administrative_districts"
    for file in folder:
        if file.removesuffix(".py") == "alsace_lorraine":
            germany.regions.append(alsace_lorraine.Alsace_Lorraine(germany.date.year, germany))

        elif file.removesuffix(".py") == "baden":
            germany.regions.append(baden.Baden(germany.date.year, germany))

        elif file.removesuffix(".py") == "bavaria":
            germany.regions.append(bavaria.Bavaria(germany.date.year, germany))

        elif file.removesuffix(".py") == "prussia":
            germany.regions.append(prussia.Prussia(germany.date.year, germany))

        elif file.removesuffix(".py") == "saxony":
            germany.regions.append(saxony.Saxony(germany.date.year, germany))

        elif file.removesuffix(".py") == "prussia":
            germany.regions.append(wurttemburg.Wurttemburg(germany.date.year, germany))

def manual_game(germany, globe1):
    establish_districts(germany)

class Germany:
    def __init__(self, year):
        # date variables
        self.date = datetime(int(year), 1, 1)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        # administrative and political variables
        """administrative"""
        self.regions = []
        """political variables"""
        self.stability = 0
        self.kaiser = kaisers[year]
        self.leader = chancellors[year]
        self.political_power = 150
        self.political_exponent = 2.45
        # economic variables
        self.current_gdp = 0
        self.past_gdp = 0
        self.national_debt = 0
        self.economic_stimulus = False
        # social variables
        self.happiness = 0
        self.current_pop = 0
        self.past_pop = 0
        self.births = 0
        self.deaths = 0
        self.pop_growth = 0