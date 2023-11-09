import random
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

flags = {
    "1910": "../flags/britain/United-Kingdom-Flag.jpg",
    "1914": "../flags/britain/United-Kingdom-Flag.jpg",
    "1918": "../flags/britain/United-Kingdom-Flag.jpg",
    "1932": "../flags/britain/United-Kingdom-Flag.jpg",
    "1936": "../flags/britain/United-Kingdom-Flag.jpg",
    "1939": "../flags/britain/United-Kingdom-Flag.jpg"
}

leader_images = {"1910": "../leaders/britain/330px-Herbert_Henry_Asquith_till_1916.jpg",
                 "1914": "../leaders/britain/330px-Herbert_Henry_Asquith_till_1916.jpg",
                 "1918": "../leaders/britain/330px-David_Lloyd_George_1916-1922.jpg",
                 "1932": "../leaders/britain/J._Ramsay_MacDonald_LCCN2014715885_(cropped)_till_1935.jpg",
                 "1936": "../leaders/britain/Stanley_Baldwin_ggbain.35233_1935_1937.jpg",
                 "1939": "../leaders/britain/chamberlain_1937-1939.jpeg"
                 }

monarchs = {
    """Dictionary for english monarchs
    Leader selection will be in sync with time frame selection
    Unlike population, leader dictionary will be setup to be as historically accurate as possible"""

    "1910": "Edward VII",
    "1914": "George V",
    "1918": "George V",
    "1932": "George V",
    "1936": "Edward VIII",
    "1939": "George VI"
}

pm = {
    "1910": "H.H. Asquith",
    "1914": "H.H. Asquith",
    "1918": "David Lloyd George",
    "1932": "Ramsay MacDonald",
    "1936": "Stanley Baldwin",
    "1939": "Neville Chamberlain"
}

spare_pms = ["Duncan Pirie", "Henry Cowan", "Harold Baker", "James Calmont", "Ellis Ellis-Griffith",
             "Charles Craig", "William Jones", "Alfred Scott", "Sir Charles Hunter"]

spare_1900_1950_monarchs = ["Louis", "Prince Arthur", "Beatrice", "Prince Henry", "Alexander Ramsay",
                            "Alexander Cambridge",
                            "Albert Victor", "Victoria II", "George VI"]


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


# population variables and dictionaries
"""Dictionary for population
    Population selection will be in sync with time frame selection
    Population will then be set up to grow or shrink in random amounts"""
population = {

    "1910": 44720000,
    "1914": 45590000,
    "1918": 46350000,
    "1932": 46250000,
    "1936": 47190000,
    "1939": 47890000
}

# economic variables and dictionaries
gdp = {
    "1910": 15783763158,
    "1914": 17856842105,
    "1918": 23873207895,
    "1932": 44371994737,
    "1936": 53157368421,
    "1939": 54936947368
}


class Britain(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.date_checker = globe.date + timedelta(days=3)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Great Britain"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = pm[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.political_typology = "Democratic"
        self.political_power = 200
        self.political_exponent = 1.56
        """Stability"""
        self.current_gdp = gdp[str(globe.date.year)]
        self.coordinates = []
        self.land_1910_1914 = ["United Kingdom of Great Britain and Ireland", "British East Africa",
                               "British Somaliland",
                               "Malaya", "British Protectorate", "British Raj", "Australia", "Anglo-Egyption Sudan",
                               "Egypt",
                               "Mesopotamia (GB)", "South Africa", "Botswana", "Rhodesia", "New Zealand", "Nigeria"]

        self.land_1918_1936 = ["United Kingdom of Great Britain and Ireland", "British East Africa",
                               "British Somaliland",
                               "Malaya", "British Protectorate", "British Raj", "Australia", "Sudan", "Egypt",
                               "Union of South Africa", "Botswana", "German E. Africa (Tanganyika)",
                               "German South-West Africa", "Mandatory Palestine (GB)", "Zambia", "Zimbabwe",
                               "New Zealand", "Nigeria"]

        self.land_1939 = ["United Kingdom", "British East Africa", "British Somaliland",
                          "Malaya", "British Protectorate", "British Raj", "Australia", "Sudan", "Egypt",
                          "Union of South Africa", "Botswana", "Tanzania, United Republic of",
                          "German South-West Africa", "Mandatory Palestine (GB)", "Dominion of Newfoundland",
                          "New Zealand",
                          "Swaziland", "Oman (British Raj)", "Nigeria"]

        self.foreign_relations = {"foreign relations": []}

    def establish_foreign_objectives(self):
        if self.date.year <= 1918:
            objectives_enemy = ["Contain Germany", "Contain Turkey", "Contain Austria"]
            objectives_allies = ["Improve relations with France", "Improve relations with Russia", "Improve relations with United States"]

        else:
            objectives_enemy = ["Contain Germany", "Contain Italy", "Contain Russia"]
            objectives_allies = ["Improve relations with United States", "Improve relations with France", "Improve relations with Canada"]

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
        if self.date.year <= 1914:
            for land in range(0, len(self.land_1910_1914)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1910_1914[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year >= 1918 and self.date.year <= 1936:
            for land in range(0, len(self.land_1918_1936)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1918_1936[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year >= 1939:
            for land in range(0, len(self.land_1939)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1939[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

    # main function
    def main(self, globe, network, user_nation):
        super().establishing_beginning_objectives()
        while self.population > 2000000:
            super().check_economic_growth(globe.date)
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            super().political_power_growth()
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
