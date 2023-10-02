import random
import time
from datetime import datetime, timedelta
from game.ai import playable_nation

leaders = {
    "1910": "Habibullah",
    "1914": "Habibullah",
    "1918": "Habibullah",
    "1932": "Nadir Khan",
    "1936": "Zahir Shah",
    "1939": "Zahir Shah"
}


population = {
    "1910": 5500000,
    "1914": 7120000,
    "1918": 9530000,
    "1932": 6410000,
    "1936": 6410000,
    "1939": 6430000
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": 12003528421,
    "1914": 15085307368,
    "1918": 14723268421,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

flags = {"1910": "../flags/afghanistan/Flag_of_Afghanistan_(1919–1921).jpg",
         "1914": "../flags/afghanistan/Flag_of_Afghanistan_(1919–1921).jpg",
         "1918": "../flags/afghanistan/Flag_of_Afghanistan_(1919–1921).jpg",
         "1932": "../flags/afghanistan/Flag_of_Afghanistan_(1931–1973).jpg",
         "1936": "../flags/afghanistan/Flag_of_Afghanistan_(1931–1973).jpg",
         "1939": "../flags/afghanistan/Flag_of_Afghanistan_(1931–1973).jpg"
         }

leader_images = {
    "1910": "../leaders/afghanistan/Habibullah-1910-1918.jpg",
    "1914": "../leaders/afghanistan/Habibullah-1910-1918.jpg",
    "1918": "../leaders/afghanistan/Habibullah-1910-1918.jpg",
    "1932": "../leaders/afghanistan/330px-Nadir_Khan_of_Afghanistan-1932.jpg",
    "1936": "../leaders/afghanistan/King_Zahir_Shah_of_Afghanistan_in_1963-1936-1939.jpg",
    "1939": "../leaders/afghanistan/King_Zahir_Shah_of_Afghanistan_in_1963-1936-1939.jpg"
}

class Afghanistan(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "Afghanistan"
        # date variables
        self.date = datetime(globe.date.year, 1, 1)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        self.economic_change_date = self.date + timedelta(days=60)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        self.births = 0
        self.deaths = 0
        self.birth_control = False
        self.birth_enhancer = False
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        """Stability"""
        self.stability = 95.56
        self.flag = flags[str(globe.date.year)]
        # economic
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
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
        self.alliance = ""
        # other
        self.chosen = False
