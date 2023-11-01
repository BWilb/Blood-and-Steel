import random
import time
from datetime import datetime, timedelta
from game.ai import playable_nation
from nation_data.coordination.retreive_and_convert import convert_coords, retreive_coords
import json as js

leaders = {
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
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (0, random.randrange(0, 255), random.randrange(0, 250))
        self.region = "europe"
        self.name = "Kingdom of Italy"
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
        """Stability"""
        self.stability = 95.56
        # economic
        self.e_s = "recovery"
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
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
        # other
        self.chosen = False
        self.coordinates = []
        self.land_1910 = ["Kingfom of Italy", "Eritrea"]
        self.land_1914 = ["Kingfom of Italy", "Eritrea", "Libya"]
        self.land_1932_1936 = ["Eritrea", "Italy", "Italian Somaliland"]
        self.land_1939 = ["Eritrea (Italy)", "Ethiopia (Italy)", "Italy", "Italian Somaliland", "Libya"]

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        if self.date.year <= 1914:
            for land in range(0, len(self.land_1914)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1914[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year == 1932 or self.date.year == 1936:
            for land in range(0, len(self.land_1932_1936)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1932_1936[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year >= 1939:
            for land in range(0, len(self.land_1939)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1939[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))