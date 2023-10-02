from datetime import datetime, timedelta
from game.ai import playable_nation

leaders = {
    "1910": None,
    "1914": None,
    "1918": None,
    "1932": "Nuri al-Said",
    "1936": "Yasin al-Hashimi",
    "1939": "Yasin al-Hashimi"
}


population = {
    "1910": 10970000,
    "1914": 10320000,
    "1918": 9530000,
    "1932": 13270000,
    "1936": 14230000,
    "1939": 14970000
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": None,
    "1914": None,
    "1918": None,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

flags = {"1910": "../flags/iraq/Flag_of_Iraq_(1924–1959).jpg",
         "1914": "../flags/iraq/Flag_of_Iraq_(1924–1959).jpg",
         "1918": "../flags/iraq/Flag_of_Iraq_(1924–1959).jpg",
         "1932": "../flags/iraq/Flag_of_Iraq_(1924–1959).jpg",
         "1936": "../flags/iraq/Flag_of_Iraq_(1924–1959).jpg",
         "1939": "../flags/iraq/Flag_of_Iraq_(1924–1959).jpg"
         }

leader_images = {
    "1910": "../leaders/iraq/330px-AhmadShahQajar2_1910-1918.jpg",
    "1914": "../leaders/iraq/330px-AhmadShahQajar2_1910-1918.jpg",
    "1918": "../leaders/iraq/330px-AhmadShahQajar2_1910-1918.jpg",
    "1932": "../leaders/iraq/71nwewvdNlL.__AC_SY445_QL70_ML2_-1932.jpg",
    "1936": "../leaders/iraq/330px-Yasin_Hashimi,_1927-1936.jpg",
    "1939": "../leaders/iraq/330px-Yasin_Hashimi,_1927-1936.jpg"
}

class Iraq(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "Iraq"
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
        # coordinates
        self.iraqi_coords = []
        # other
        self.chosen = False