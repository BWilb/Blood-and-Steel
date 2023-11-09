import random
import time
from datetime import datetime, timedelta
import json as js
from game.ai.nation_ai import NationAI
from nation_data.coordination.retreive_and_convert import retreive_coords
from enum import Enum

leader_images = {
    "1910": "../leaders/bulgaria/800px-Zar_Ferdinand_Bulgarien.jpg",
    "1914": "../leaders/bulgaria/800px-Zar_Ferdinand_Bulgarien.jpg",
    "1918": "../leaders/bulgaria/800px-Zar_Ferdinand_Bulgarien.jpg",
    "1932": "../leaders/bulgaria/800px-Boris_III_of_Bulgaria.jpg",
    "1936": "../leaders/bulgaria/800px-Boris_III_of_Bulgaria.jpg",
    "1939": "../leaders/bulgaria/800px-Boris_III_of_Bulgaria.jpg"
}
flags = {
    "1910": "../flags/bulgaria/Flag_of_Bulgaria.svg.jpg",
    "1914": "../flags/bulgaria/Flag_of_Bulgaria.svg.jpg",
    "1918": "../flags/bulgaria/Flag_of_Bulgaria.svg.jpg",
    "1932": "../flags/bulgaria/Flag_of_Bulgaria.svg.jpg",
    "1936": "../flags/bulgaria/Flag_of_Bulgaria.svg.jpg",
    "1939": "../flags/bulgaria/Flag_of_Bulgaria.svg.jpg"
}

leaders = {
    "1910" : "Ferdinand I",
    "1914" : "Ferdinand I",
    "1918" : "Ferdinand I",
    "1932" : "Boris III",
    "1936" : "Boris III",
    "1939" : "Boris III"
}

population = {
    "1910": 4470000,
    "1914": 4680000,
    "1918": 4890000,
    "1932": 6070000,
    "1936": 6320000,
    "1939": 6510000
}
gdp = {
    "1910": 4659663,
    "1914": 4847024,
    "1918": 4953286,
    "1932": 5037403,
    "1936": 5228000,
    "1939": 7037894
}

class BulgariaAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.date_checker = globe.date + timedelta(days=3)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Bulgaria"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        if globe.date.year < 1932:
            self.political_typology = ""
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
        self.foreign_relations = {"foreign relations": []}

    def establish_foreign_objectives(self):
        if self.date.year <= 1918:
            objectives_enemy = ["Contain Serbia", "Contain Turkey"]
            objectives_allies = ["Improve relations with Germany", "Improve relations with Austria"]

        else:
            objectives_enemy = ["Contain Greece", "Contain Russia"]
            objectives_allies = ["Improve relations with Germany", "Improve relations with Italy", "Improve relations with Japan"]

        for enemy in objectives_enemy:
            self.objectives["objectives"][0]['foreign'].append(enemy)

        for ally in objectives_allies:
            self.objectives["objectives"][0]['foreign'].append(ally)

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
            for i in range(0, len(nation_json['countries'])):
                if nation_json['countries'][i]['nation_name'] == "Bulgaria":
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]

    def main(self, globe, network, user_nation):
        #super().establishing_beginning_objectives()
        while self.population > 100000:
            super().check_economic_growth(globe.date)
            super().check_population_growth()
            super().political_power_growth()
            super().stability_happiness_change(globe)
            if globe.date > self.date_checker:
                super().determine_diplomatic_approach(globe, network, user_nation)
                self.date_checker = globe.date + timedelta(days=3)
            super().change_relations(globe.nations)
            chance = random.randrange(1, 50)
            if chance % 8 == 2 or chance % 5 == 4:
                super().protests()
            super().pop_growth()
            super().check_economic_state(globe.date)
            super().adding_conscription_pool(globe)
            break