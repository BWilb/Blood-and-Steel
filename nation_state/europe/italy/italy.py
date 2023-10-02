from datetime import datetime, timedelta
from game.ai import playable_nation

prime_ministers = {
    "1910": "Luigi Luzzatti",
    "1914": "Antonio Salandra",
    "1918": "Vittorio Emanuele Orlando",
    "1932": "Benito Mussolini",
    "1936": "Benito Mussolini",
    "1939": "Benito Mussolini"
}

monarchs = {
    "1910": "Victor Emmanuel III",
    "1914": "Victor Emmanuel III",
    "1918": "Victor Emmanuel III",
    "1932": "Victor Emmanuel III",
    "1936": "Victor Emmanuel III",
    "1939": "Victor Emmanuel III"
}
"""Economic variables and dictionaries"""
gdp = {
    "1910": 7243560000,
    "1914": 7294052632,
    "1918": 7318292632,
    "1932": 12072684211,
    "1936": 15920315789,
    "1939": 19837894737
}

"""Population variables and dictionaries"""
population = {
    "1910": 36100000,
    "1914": 36500000,
    "1918": 36800000,
    "1932": 41000000,
    "1936": 42400000,
    "1939": 43500000
}
leader_images = {
    "1910": "../leaders/italy/Sidney_sonnino_1910.jpg",
    "1914": "../leaders/italy/giolitti_1914.jpg",
    "1918": "../leaders/italy/Flag_of_Greece.jpg",
    "1932": "../leaders/italy/220px-Benito_Mussolini_uncolored.jpg",
    "1936": "../leaders/italy/220px-Benito_Mussolini_uncolored.jpg",
    "1939": "../leaders/italy/220px-Benito_Mussolini_uncolored.jpg"
}
flags = {
    "1910": "../flags/italy/Flag_of_Italy_(1861-1946)_crowned.jpg",
    "1914": "../flags/italy/Flag_of_Italy_(1861-1946)_crowned.jpg",
    "1918": "../flags/italy/Flag_of_Italy_(1861-1946)_crowned.jpg",
    "1932": "../flags/italy/Flag_of_Italy_(1861-1946)_crowned.jpg",
    "1936": "../flags/italy/Flag_of_Italy_(1861-1946)_crowned.jpg",
    "1939": "../flags/italy/Flag_of_Italy_(1861-1946)_crowned.jpg"
}


class Italy(playable_nation.PlayableNation):
    def __init__(self, year):
        super().__init__(year)
        self.region = "europe"
        self.name = "Kingdom of Italy"
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
        self.leader = prime_ministers[year]
        self.monarch = monarchs[year]
        self.leader_image = leader_images[year]
        self.flag = flags[year]
        """Stability"""
        self.stability = 95.56
        # economic
        self.e_s = "recovery"
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.corporate_tax_rate = 25.00
        self.income_tax_rate = 24.00
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
        """North america"""
        # us
        self.us_relations = 56.97
        self.us_guarantee = False
        self.us_embargo = False
        # mexico
        self.mexico_relations = 89.97
        self.mexico_guarantee = False
        self.mexico_embargo = False
        # other
        self.chosen = False