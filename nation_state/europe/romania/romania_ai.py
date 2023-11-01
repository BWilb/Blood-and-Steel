import random
from datetime import timedelta
from enum import Enum
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

from game.ai.nation_ai import NationAI

# Romania
"""Population Dictionaries"""
population = {
    "1910": 11830000,
    "1914": 12040000,
    "1918": 12230000,
    "1932": 14470000,
    "1936": 15170000,
    "1939": 15680000
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

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class RomaniaAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Kingdom of Romania"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = leaders[str(globe.date.year)]
        self.political_power = 200
        self.political_exponent = 1.56
        """Stability"""
        self.stability = 95.56
        # economic
        self.corporate_taxes = 24.00
        self.income_taxes = 20.00
        self.current_gdp = gdp[str(globe.date.year)]
        """Components of GDP"""
        self.consumer_spending = 200
        self.investment = 300
        self.government_spending = 350
        self.exports = 1000
        self.imports = 1200
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # international
        self.alliance = ""
        self.us_relations = 34.56
        # other
        self.coordinates = []

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        for i in range(len(nation_json['countries'])):
            if (nation_json['countries'][i]['nation_name'] == "Romania"):
                self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]

        return self.coordinates

    # main function
    def main(self, globe, network):
        #super().establishing_beginning_objectives()
        while self.population > 2000000:
            """super().check_economic_growth(globe.date)
                        super().check_population_growth()
                        # random_functions.random_functions(self, globe)
                        super().stability_happiness_change(globe)
                        super().political_power_growth()
                        super().determine_diplomatic_approach(globe.nations, globe, network)
                        super().change_relations(globe.nations)
                        chance = random.randrange(1, 50)
                        if chance % 8 == 2 or chance % 5 == 4:
                            super().protests()"""
            super().pop_growth()
            super().check_economic_state(globe.date)
            self.date += timedelta(days=1)
            break
