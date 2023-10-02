import random
import time
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from game.ai import playable_nation

"""Population Dictionaries"""
population = {
    "1910": 2286981,
    "1914": 2618301,
    "1918": 2916220,
    "1932": 4147085,
    "1936": 4409675,
    "1939": 4620766
}

"""Political Dictionaries"""
leaders = {
    "1910": "José Miguel Gómez",
    "1914": "Mario García Menocal",
    "1918": "Mario García Menocal",
    "1932": "Gerardo Machado",
    "1936": "Federico Laredo Brú",
    "1939": "Federico Laredo Brú"
}

gdp = {
    "1910": 75000000,
    "1914": 76346343,
    "1918": 77648543,
    "1932": 76573434,
    "1936": 77346224,
    "1939": 78347343
}

flags = {
    "1910": "../flags/cuba/cuba.jpeg",
    "1914": "../flags/cuba/cuba.jpeg",
    "1918": "../flags/cuba/cuba.jpeg",
    "1932": "../flags/cuba/cuba.jpeg",
    "1936": "../flags/cuba/cuba.jpeg",
    "1939": "../flags/cuba/cuba.jpeg"
}
leader_images = {"1910": "../leaders/cuba/Gral_de_División_José_Miguel_Gomez_Gomez_1910.jpeg",
                 "1914": "../leaders/cuba/mario-garca-menocal-1866-1941-granger_1914-1918.jpg",
                 "1918": "../leaders/cuba/mario-garca-menocal-1866-1941-granger_1914-1918.jpg",
                 "1932": "../leaders/cuba/330px-Gmachado_1932.jpg",
                 "1936": "../leaders/cuba/1936.png",
                 "1939": "../leaders/cuba/1939.jpeg"
                 }

class Cuba(playable_nation.PlayableNation):
    def __init__(self, year):
        super().__init__(year)
        self.name = "Cuban Republic"
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
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.e_s = "recovery"
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