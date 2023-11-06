import random
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

flags = {"1910": "../flags/france/Flag_of_France.jpg",
         "1914": "../flags/france/Flag_of_France.jpg",
         "1918": "../flags/france/Flag_of_France.jpg",
         "1932": "../flags/france/Flag_of_France.jpg",
         "1936": "../flags/france/Flag_of_France.jpg",
         "1939": "../flags/france/Flag_of_France.jpg"}

leader_images = {
    "1910": "../leaders/france/Armand_Fallières_Paris_till_1913.jpg",
    "1914": "../leaders/france/330px-Raymond_Poincaré_officiel_(cropped)_1913-1920.jpg",
    "1918": "../leaders/france/330px-Raymond_Poincaré_officiel_(cropped)_1913-1920.jpg",
    "1932": "../leaders/france/Albert_Lebrun_1932_(2)_(cropped_2)_1932-1940.jpg",
    "1936": "../leaders/france/Albert_Lebrun_1932_(2)_(cropped_2)_1932-1940.jpg",
    "1939": "../leaders/france/Albert_Lebrun_1932_(2)_(cropped_2)_1932-1940.jpg"
}

"""Population Dictionaries"""
population = {
    "1910": 40340000,
    "1914": 39580000,
    "1918": 38680000,
    "1932": 40690000,
    "1936": 40450000,
    "1939": 40310000
}

"""Political Dictionaries"""
leaders = {
    "1910": "Armand Fallières",
    "1914": "Raymond Poincaré",
    "1918": "Raymond Poincaré",
    "1932": "Albert Lebrun",
    "1936": "Albert Lebrun",
    "1939": "Albert Lebrun"
}

gdp = {
    "1910": 7893726221,
    "1914": 8926821140,
    "1918": 13427143793,
    "1932": 10660656638,
    "1936": 14707806582,
    "1939": 11957073084
}

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class FranceAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.date_checker = globe.date + timedelta(days=3)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Republic of France"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.political_power = 200
        self.political_exponent = 1.56
        self.political_typology = "Democratic"
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
        self.land_1910_1918 = ["Tunisia", "France", "French Guiana", "French Indo-China", "French Equatorial Africa",
                               "French West Africa", "Algeria", "Congo (France)", "Algeria (France)", "Morocco (France)"]

        self.land_1932_1939 = ["Tunisia", "France", "French Guiana", "French Indo-China", "French Equatorial Africa",
                               "French West Africa", "Algeria (France)", "French Cameroons", "Congo (France)",
                               "Syria (France)", "Armenia", "Morocco (France)", "Morocco", "Algeria"]

    def establish_foreign_objectives(self):
        if self.date.year <= 1918:
            objectives_enemy = ["Contain Germany", "Contain Turkey", "Contain Austria"]
            objectives_allies = ["Improve relations with France", "Improve relations with Russia", "Improve relations with United States"]

        else:
            objectives_enemy = ["Contain Germany", "Contain Italy", "Contain Russia", "Contain Japan"]
            objectives_allies = ["Improve relations with United States", "Improve relations with Britain", "Improve relations with Belgium"]

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

        if self.date.year <= 1918:
            for land in range(0, len(self.land_1910_1918)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1910_1918[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year >= 1932:
            for land in range(0, len(self.land_1932_1939)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1932_1939[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

    # main function
    def main(self, globe, network, user_nation):
        #super().establishing_beginning_objectives()
        while self.population > 2000000:
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
            break