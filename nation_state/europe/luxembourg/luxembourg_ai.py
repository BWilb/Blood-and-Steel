import random
from datetime import timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

leaders = {
    "1910": "Paul Eyschen",
    "1914": "Paul Eyschen",
    "1918": "Léon Kauffman",
    "1932": "Pierre Dupong",
    "1936": "Pierre Dupong",
    "1939": "Pierre Dupong"
}
monarchs = {
    "1910": "Guillaume IV",
    "1914": "Marie-Adélaïde",
    "1918": "Marie-Adélaïde",
    "1932": "Charlotte",
    "1936": "Charlotte",
    "1939": "Charlotte"
}

population = {
    "1910": 2850000,
    "1914": 2630000,
    "1918": 2360000,
    "1932": 2430000,
    "1936": 2440000,
    "1939": 2450000
}
gdp = {
    "1910": 465966372,
    "1914": 484702474,
    "1918": 495328640,
    "1932": 503740350,
    "1936": 522800000,
    "1939": 703789473
}

flags = {
    "1910": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1914": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1918": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1932": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1936": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg",
    "1939": "../flags/luxembourg/1920px-Flag_of_Luxembourg_wide.jpg"
}

leader_images = {"1910": "../leaders/luxembourg/paul_eyschen_accroche_1910-1914.jpg",
                 "1914": "../leaders/luxembourg/paul_eyschen_accroche_1910-1914.jpg",
                 "1918": "../leaders/luxembourg/Léon_Kauffman_(1869-1952)_1918.jpg",
                 "1932": "../leaders/luxembourg/Joseph_Bech_(detail)_1933.jpg",
                 "1936": "../leaders/luxembourg/Pierre_Dupong,_Benelux_conference_The_Hague_March_1949,_Luxembourg_Delegation_1939.jpg",
                 "1939": "../leaders/luxembourg/Pierre_Dupong,_Benelux_conference_The_Hague_March_1949,_Luxembourg_Delegation_1939.jpg"
                 }


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


class LuxembourgAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Kingdom of Luxembourg"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.political_typology = "Republicanism"
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
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
        self.land = ["Luxembourg"]

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for land in range(0, len(self.land)):
            for i in range(0, len(nation_json['countries'])):
                if self.land[land] == nation_json['countries'][i]['nation_name']:
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]

    # main function
    def main(self, globe, network, user_nation):
        super().establishing_beginning_objectives()
        while self.population > 100000:
            super().check_economic_growth(globe.date)
            super().check_population_growth()
            super().political_power_growth()
            #super().stability_happiness_change(globe)
            super().determine_diplomatic_approach(globe.nations, globe, network, user_nation)
            super().change_relations(globe.nations)
            chance = random.randrange(1, 50)
            if chance % 8 == 2 or chance % 5 == 4:
                super().protests()
            super().pop_growth()
            super().check_economic_state(globe.date)
            self.date += timedelta(days=1)
            break
