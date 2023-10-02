import random
import time
from datetime import datetime, timedelta
import json as js
from nation_data.coordination.retreive_and_convert import convert_coords, retreive_coords
from datetime import datetime, timedelta
from game.ai import playable_nation
"""Population Dictionaries"""
population = {
    "1910": 7145835,
    "1914": 7642710,
    "1918": 7882960,
    "1932": 18143247,
    "1936": 18997248,
    "1939": 19868002
}

"""Political Dictionaries"""
leaders = {
    "1910": "Ion I. C. Brătianu",
    "1914": "Ion I. C. Brătianu",
    "1918": "Ion I. C. Brătianu",
    "1932": "Nicolae Iorga",
    "1936": "Gheorghe Tătărescu",
    "1939": "rmand Călinescu"
}

monarchs = {
    "1910": "Carol I",
    "1914": "Carol I",
    "1918": "Ferdinand I",
    "1932": "Carol II",
    "1936": "Carol II",
    "1939": "Carol II"
}

gdp = {
    "1910": 11882323232,
    "1914": 11982323232,
    "1918": 12182323232,
    "1932": 14212323232,
    "1936": 18882323232,
    "1939": 19882323232
}

flags = {"1910": "../flags/romania/romania.jpeg",
         "1914": "../flags/romania/romania.jpeg",
         "1918": "../flags/romania/romania.jpeg",
         "1932": "../flags/romania/romania.jpeg",
         "1936": "../flags/romania/romania.jpeg",
         "1939": "../flags/romania/romania.jpeg"}

leader_images = {
    "1910": "../leaders/romania/Carp_(The_Road_to_Romanian_Independence)_1910.jpeg",
    "1914": "../leaders/romania/IonelBratianu3b40761r_1914-1918.jpg",
    "1918": "../leaders/romania/IonelBratianu3b40761r_1914-1918.jpg",
    "1932": "../leaders/romania/Iorga_at_his_desk_Luceaferul_2,_1914-1932.jpg",
    "1936": "../leaders/romania/255px-Gheorghe_Tătărescu-1936.jpg",
    "1939": "../leaders/romania/Miron_Cristia_patriach_of_Romania-1939.jpeg"
}

class Romania(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "Kingdom of Romania"
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
        self.flag = flags[str(globe.date.year)]
        self.e_s = "recovery"
        """Stability"""
        self.stability = 95.56
        # economic
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        self.income_tax_rate = 25.00
        self.corporate_tax_rate = 35.00
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # international
        self.alliance = ""
        # international
        self.alliance = ""
        # coordinates
        self.romanian_coords = []
        # other
        self.sprite = False
    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        # utilizing absolute path of file, to ensure that the file is found
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for i in range(len(nation_json['countries'])):
            if nation_json['countries'][i]['nation_name'] == "Romania":
                # searching for Romania
                return retreive_coords(nation_json['countries'][i]['coordinates'])