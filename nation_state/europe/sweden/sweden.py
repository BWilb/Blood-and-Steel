import random
import time
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from game.ai import playable_nation
leaders = {
    "1910" : "Arvid Lindman",
    "1914" : "Karl Staaff",
    "1918" : "Nils Edén",
    "1932" : "Carl Gustaf Ekman",
    "1936" : "Per Albin Hansson",
    "1939" : "Per Albin Hansson"
}
monarchs = {
    "1910" : "Gustaf V",
    "1914" : "Gustaf V",
    "1918" : "Gustaf V",
    "1932" : "Gustaf V",
    "1936" : "Gustaf V",
    "1939" : "Gustaf V"
}

population = {
    "1910": 5493302,
    "1914": 5619111,
    "1918": 5746841,
    "1932": 6172343,
    "1936": 6259363,
    "1939": 6335505
}
gdp = {
    "1910": 1765677700,
    "1914": 1035207385,
    "1918": 2754193594,
    "1932": 1911933808,
    "1936": 2344127797,
    "1939": 2892814865
}

leader_images = {
    "1910": "../leaders/sweden/330px-Arvid_Lindman_1910.jpg",
    "1914": "../leaders/sweden/Karl_Staaff_1914.jpg",
    "1918": "../leaders/sweden/Nils_Eden_1918.jpg",
    "1932": "../leaders/sweden/330px-Carl_Gustaf_Ekman_1932.jpg",
    "1936": "../leaders/sweden/330px-Per_Albin_Hansson_-_Sveriges_styresmän_1936-1939.jpg",
    "1939": "../leaders/sweden/330px-Per_Albin_Hansson_-_Sveriges_styresmän_1936-1939.jpg"
}
flags = {
    "1910": "../flags/sweden/Flag_of_Sweden.jpg",
    "1914": "../flags/sweden/Flag_of_Sweden.jpg",
    "1918": "../flags/sweden/Flag_of_Sweden.jpg",
    "1932": "../flags/sweden/Flag_of_Sweden.jpg",
    "1936": "../flags/sweden/Flag_of_Sweden.jpg",
    "1939": "../flags/sweden/Flag_of_Sweden.jpg"
}

class Sweden(playable_nation.PlayableNation):
    def __init__(self, year):
        super().__init__(year)
        self.name = "Kingdom of Sweden"
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
        # other
        self.alliance = ""
        self.chosen = False