import random
from datetime import timedelta
import json as js
from game.ai.nation_ai import NationAI
from nation_data.coordination.retreive_and_convert import retreive_coords

leader_images = {
    "1910": "",
    "1914": "",
    "1918": "",
    "1932": "../leaders/lithuania/Antanas_Smetona_2.jpg",
    "1936": "../leaders/lithuania/Antanas_Smetona_2.jpg",
    "1939": "../leaders/lithuania/Antanas_Smetona_2.jpg"
}
flags = {
    "1910": "",
    "1914": "",
    "1918": "",
    "1932": "../flags/lithuania/Flag_of_Lithuania.svg.jpg",
    "1936": "../flags/lithuania/Flag_of_Lithuania.svg.jpg",
    "1939": "../flags/lithuania/Flag_of_Lithuania.svg.jpg"
}

leaders = {
    "1910" : None,
    "1914" : None,
    "1918" : None,
    "1932" : "Konstantin Päts",
    "1936" : "Konstantin Päts",
    "1939" : "Kaarel Eenpalu"
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
    "1910": 4659663,
    "1914": 4847024,
    "1918": 4953286,
    "1932": 5037403,
    "1936": 5228000,
    "1939": 7037894
}

class LithuaniaAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.date_checker = globe.date + timedelta(days=3)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Lithuania"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.political_typology = "Autocratic"
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
        self.foreign_relations = {"foreign relations": []}

    def establish_foreign_objectives(self):
        objectives_enemy = ["Contain Germany", "Contain Italy", "Contain Russia", "Contain Bulgaria"]
        objectives_allies = ["Improve relations with United States", "Improve relations with France",
                             "Improve relations with Canada", "Improve relations with Belgium",
                             "Improve relations with Netherlands", "Improve relations with Estonia",
                             "Improve relations with Latvia"]

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
                if nation_json['countries'][i]['nation_name'] == "Lithuania":
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]