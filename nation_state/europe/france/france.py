import random
import time
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from game.ai import playable_nation

"""Population Dictionaries"""
population = {
    "1910": 39446500,
    "1914": 39364666,
    "1918": 39213999,
    "1932": 41349803,
    "1936": 40478600,
    "1939": 39726646
}

"""Political Dictionaries"""
leaders = {
    "1910": "Armand Fallières",
    "1914": "Raymond Poincaré",
    "1918": "Raymond Poincaré",
    "1932": "Albert Lebrun",
    "1936": "Albert Lebrun",
    "1939": "Albert Lebrun"
}

gdp = {
    "1910": 7893726221,
    "1914": 8926821140,
    "1918": 13427143793,
    "1932": 10660656638,
    "1936": 14707806582,
    "1939": 11957073084
}

flags = {"1910": "../flags/france/Flag_of_France.jpg",
         "1914": "../flags/france/Flag_of_France.jpg",
         "1918": "../flags/france/Flag_of_France.jpg",
         "1932": "../flags/france/Flag_of_France.jpg",
         "1936": "../flags/france/Flag_of_France.jpg",
         "1939": "../flags/france/Flag_of_France.jpg"}

leader_images = {
    "1910": "../leaders/france/Armand_Fallières_Paris_till_1913.jpg",
    "1914": "../leaders/france/330px-Raymond_Poincaré_officiel_(cropped)_1913-1920.jpg",
    "1918": "../leaders/france/330px-Raymond_Poincaré_officiel_(cropped)_1913-1920.jpg",
    "1932": "../leaders/france/Albert_Lebrun_1932_(2)_(cropped_2)_1932-1940.jpg",
    "1936": "../leaders/france/Albert_Lebrun_1932_(2)_(cropped_2)_1932-1940.jpg",
    "1939": "../leaders/france/Albert_Lebrun_1932_(2)_(cropped_2)_1932-1940.jpg"
}


class France(playable_nation.PlayableNation):
    def __init__(self, year):
        super().__init__(year)
        self.name = "French Republic"
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
