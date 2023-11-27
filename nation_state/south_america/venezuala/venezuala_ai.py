import random

from nation_data.coordination.retreive_and_convert import retreive_coords
from game.ai.nation_ai import NationAI
import json as js
from datetime import datetime, timedelta
leaders = {
    "1910" : "Hermes da Fonseca",
    "1914" : "Hermes da Fonseca",
    "1918" : "Venceslau Brás",
    "1932" : "Getúlio Vargas",
    "1936" : "Getúlio Vargas",
    "1939" : "Getúlio Vargas"
}

population = {
    "1910": 3010000,
    "1914": 3110000,
    "1918": 3210000,
    "1932": 3680000,
    "1936": 3389000,
    "1939": 4070000
}
gdp = {
    "1910": 4659663720,
    "1914": 4847024746,
    "1918": 4953286406,
    "1932": 5037403509,
    "1936": 5228000000,
    "1939": 7037894737
}

flags = {"1910": "../flags/venezuela/Flag_of_Venezuela_(1905–1930).svg.png",
         "1914": "../flags/venezuela/Flag_of_Venezuela_(1905–1930).svg.png",
         "1918": "../flags/venezuela/Flag_of_Venezuela_(1905–1930).svg.png",
         "1932": "../flags/venezuela/State_flag_of_Venezuela_(1930–1954).svg.png",
         "1936": "../flags/venezuela/State_flag_of_Venezuela_(1930–1954).svg.png",
         "1939": "../flags/venezuela/State_flag_of_Venezuela_(1930–1954).svg.png"}

leader_images = {
    "1910": "../leaders/venezuela/Presidente_Victorino_Marquez_Bustillos-1910-1918.jpg",
    "1914": "../leaders/venezuela/Presidente_Victorino_Marquez_Bustillos-1910-1918.jpg",
    "1918": "../leaders/venezuela/Presidente_Victorino_Marquez_Bustillos-1910-1918.jpg",
    "1932": "../leaders/venezuela/Juan_Vicente_Gómez_2-1932.jpg",
    "1936": "../leaders/venezuela/Eleazar_López_Contreras-35-41.jpg",
    "1939": "../leaders/venezuela/Eleazar_López_Contreras-35-41.jpg"
}

class Venezuala(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.name = "Venezuela"
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
        # political
        self.political_typology = "Fascist"
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp
        self.income_tax_rate = 25.00
        self.corporate_tax_rate = 35.00
        """Components of GDP"""
        """self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0"""
        # other
        self.coordinates = []
        self.foreign_relations = {"foreign relations": []}

    def establish_foreign_objectives(self):
        objectives_enemy = ['']

        objectives_allies = ["Improve relations with Germany",
                             "Improve relations with Mexico",
                             "Improve relations with Brazil", "Improve relations with Bolivia",
                             "Improve relations with Argentina"]
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
            for i in range(len(nation_json['countries'])):
                # print(nation_json['countries'][i]['nation_name'])
                if (nation_json['countries'][i]['nation_name'] == "Venezuela"):
                    # print(nation_json['countries'][i]['coordinates'])
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = [(retreive_coords(self.coordinates))]