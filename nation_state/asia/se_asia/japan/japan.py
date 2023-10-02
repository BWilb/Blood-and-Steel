from datetime import datetime, timedelta
from game.ai import playable_nation

leaders = {
    "1910": "Katsura Tarō",
    "1914": "Ōkuma Shigenobu",
    "1918": "Hara Takashi",
    "1932": "Saitō Makoto",
    "1936": "Kōki Hirota",
    "1939": "Kiichirō Hiranuma"
}
monarchs = {
    "1910": "Emperor Meiji",
    "1914": "Emperor Taishō",
    "1918": "Emperor Taishō",
    "1932": "Emperor Shōwa",
    "1936": "Emperor Shōwa",
    "1939": "Emperor Shōwa"
}

population = {
    "1910": 49600000,
    "1914": 52500000,
    "1918": 55000000,
    "1932": 66300000,
    "1936": 70400000,
    "1939": 72500000
}
gdp = {
    "1910": 6366802632,
    "1914": 7851127368,
    "1918": 9901977895,
    "1932": 15995421053,
    "1936": 18197631579,
    "1939": 23894736842
}

flags = {"1910": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1914": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1918": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1932": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1936": "../flags/japan/Flag_of_Japan_(1870–1999).jpg",
         "1939": "../flags/japan/Flag_of_Japan_(1870–1999).jpg"}

leader_images = {
    "1910": "../leaders/japan/330px-11_KatsuraT-1910.jpg",
    "1914": "../leaders/japan/330px-Gonbee_Yamamoto_later_years-1914.jpg",
    "1918": "../leaders/japan/330px-Masatake_Terauchi_2-1918.jpg",
    "1932": "../leaders/japan/Inukai_Tsuyoshi-1932.jpg",
    "1936": "../leaders/japan/Prime_Minister_Keisuke_Okada-1936.jpg",
    "1939": "../leaders/japan/Fumimaro_Konoe(cropped)-1939.jpg"
}

class Japan(playable_nation.PlayableNation):
    def __init__(self, year):
        super().__init__(year)
        self.name = "Japan"
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
        self.alliance = ""
        # other
        self.chosen = False