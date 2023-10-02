import random
import time
from datetime import datetime, timedelta
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
    def __init__(self, year):
        super().__init__(year)
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
        """Stability"""
        self.stability = 95.56
        # economic
        self.income_tax_rate = 25.00
        self.corporate_tax_rate = 35.00
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
        # other
        self.chosen = False