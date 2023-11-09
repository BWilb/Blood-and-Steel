import random
from datetime import timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
from nation_data.coordination.retreive_and_convert import retreive_coords
import json as js

flags = {
    "1910": "../flags/austria/Flag_of_the_Habsburg_Monarchy.jpg",
    "1914": "../flags/austria/Flag_of_the_Habsburg_Monarchy.jpg",
    "1918": "../flags/austria/Flag_of_the_Habsburg_Monarchy.jpg",
    "1932": "../flags/austria/Flag_of_Austria_1932.jpg",
    "1936": "../flags/austria/State_flag_of_Austria_(1934–1938).jpg",
    "1939": "../flags/austria/Standarte_Adolf_Hitlers.jpg"
}
leader_images = {"1910": "../leaders/austria/joseph_ii.jpeg",
                 "1914": "../leaders/austria/joseph_ii.jpeg",
                 "1918": "../leaders/austria/charles_i.jpg",
                 "1932": "../leaders/austria/miklas.jpeg",
                 "1936": "../leaders/austria/miklas.jpeg",
                 "1939": "../leaders/austria/adolf-hitler-10253.jpg"
                 }


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


"""Population Dictionaries"""
population = {
    "1910": 31850000,
    "1914": 31970000,
    "1918": 31560000,
    "1932": 6700000,
    "1936": 6700000,
    "1939": 6720000
}

"""Political Dictionaries"""
leaders = {
    "1910": "Franz Joseph",
    "1914": "Franz Joseph",
    "1918": "Otto Von Hapsburg",
    "1932": "Engelbert Dollfuss",
    "1936": "Kurt Schuschnigg",
    "1939": None
}

monarchs = {
    "1910": "Franz Joseph",
    "1914": "Franz Joseph",
    "1918": "Otto Von Habsburg",
    "1932": "Otto von Habsburg II",
    "1936": "Otto von Habsburg II",
    "1939": None
}

gdp = {
    "1910": 3406984117,
    "1914": 3644313879,
    "1918": 4174673077,
    "1932": 2118539364,
    "1936": 73462352,
    "1939": None
}


class Austria(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "Europe"
        self.name = "Austria"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = leaders[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        if globe.date.year <= 1918:
            self.political_typology = "Autocratic"
        else:
            self.political_typology = "Democratic"
        self.political_power = 200
        self.political_exponent = 1.56
        self.current_gdp = gdp[str(globe.date.year)]
        """Components of GDP"""
        self.consumer_spending = 200
        self.investment = 300
        self.government_spending = 350
        self.exports = 1000
        self.imports = 1200
        # other
        self.coordinates = []
        self.land_1910_1918 = ["Austro-Hungarian Empire"]
        self.land_1932 = ["Austria"]
        self.foreign_relations = {"foreign relations": []}

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
            self.coordinates = [(retreive_coords(self.coordinates))]

        if self.date.year > 1918:
            for land in range(0, len(self.land_1932)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1932[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = [(retreive_coords(self.coordinates))]

    # main function
    def main(self, globe, network, user_nation):
        super().establishing_beginning_objectives()
        while self.population > 50000:
            super().check_economic_growth(globe.date)
            super().check_population_growth()
            super().political_power_growth()
            super().stability_happiness_change(globe)
            super().determine_diplomatic_approach(globe, network, user_nation)
            super().change_relations(globe.nations)
            chance = random.randrange(1, 50)
            if chance % 8 == 2 or chance % 5 == 4:
                super().protests()
            super().pop_growth()
            super().check_economic_state(globe.date)
            self.date += timedelta(days=1)
            break
