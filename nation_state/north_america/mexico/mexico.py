import random
import sys
import time
from collections import OrderedDict
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from game.ai import playable_nation
def establish_foreign_nations(globe, *args):
    """labelling second parameter as *args, due to unknown number of nations that will be sent into this function"""
    for i in range(0, len(args)):
        globe.nations.append(args[i])


def slow_print(words):
    # used in international relations function, when dealing out region names
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.19)


"""Population Dictionaries"""
population = {
    "1910": 14702456,
    "1914": 14742623,
    "1918": 14782786,
    "1932": 17635255,
    "1936": 18971701,
    "1939": 19961661
}

"""Political Dictionaries"""
leaders = {
    "1910": "Porfirio Diaz",
    "1914": "Victoriano Huerta",
    "1918": "Venustiano Carranza",
    "1932": "Abelardo Rodriguez",
    "1936": "Lázaro Cárdenas",
    "1939": "Lázaro Cárdenas"
}

gdp = {
    "1910": 500000000,
    "1914": 659939450,
    "1918": 733488730,
    "1932": 723488730,
    "1936": 723488730,
    "1939": 743488730
}

flags = {
    "1910": "../flags/mexico/150px-Bandera_de_México_(1880-1914).jpg",
    "1914": "../flags/mexico/150px-Bandera_de_México_(1880-1914).jpg",
    "1918": "../flags/mexico/1920px-Bandera_de_la_Tercera_República_Federal_de_los_Estados_Unidos_Mexicanos(1916-1932).jpg",
    "1932": "../flags/mexico/1920px-Bandera_de_la_Tercera_República_Federal_de_los_Estados_Unidos_Mexicanos(1916-1932).jpg",
    "1936": "../flags/mexico/1920px-Bandera_de_la_Tercer_República_Federal_de_los_Estados_Unidos_Mexicanos_modelo_1934.jpg",
    "1939": "../flags/mexico/1920px-Bandera_de_la_Tercer_República_Federal_de_los_Estados_Unidos_Mexicanos_modelo_1934.jpg"
}
leader_images = {"1910": "../leaders/mexico/Porfirio_Diaz_en_1867.jpg",
                 "1914": "../leaders/mexico/huerta_1914.jpg",
                 "1918": "../leaders/mexico/s20_15_venustiano-768x1024_1918.jpg",
                 "1932": "../leaders/mexico/OIP_1932.jpeg",
                 "1936": "../leaders/mexico/lazaro_1936_1939.jpeg",
                 "1939": "../leaders/mexico/lazaro_1936_1939.jpeg"
                 }
class Mexico(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.is_intact = True
        self.name = "Mexico"
        # date variables
        self.date = datetime(int(globe.date.year), 1, 1)
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
        self.past_population = self.population
        self.births = 0
        self.deaths = 0
        self.birth_control = False
        self.birth_enhancer = False
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = leaders[str(globe.date.year)]
        """leader image only for sprite version"""
        self.leader_image = leader_images[str(globe.date.year)]
        self.political_power = 200
        self.political_exponent = 1.25
        """Stability"""
        self.stability = 95.56
        self.flag = flags[str(globe.date.year)]
        # economic
        self.e_s = "recovery"
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
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
