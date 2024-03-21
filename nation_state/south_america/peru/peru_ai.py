import json as js
import random
from datetime import datetime, timedelta

from nation_data.coordination.retreive_and_convert import retreive_coords
from game.ai.nation_ai import NationAI

population = {

    "1910": 4140000,
    "1914": 4350000,
    "1918": 4570000,
    "1932": 5660000,
    "1936": 6040000,
    "1939": 6340000
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

pm = {
    "1910": "H.H. Asquith",
    "1914": "H.H. Asquith",
    "1918": "David Lloyd George",
    "1932": "Ramsay MacDonald",
    "1936": "Stanley Baldwin",
    "1939": "Neville Chamberlain"
}

flags = {"1910": "../flags/peru/Flag_of_Peru_(1884–1950).jpg",
         "1914": "../flags/peru/Flag_of_Peru_(1884–1950).jpg",
         "1918": "../flags/peru/Flag_of_Peru_(1884–1950).jpg",
         "1932": "../flags/peru/Flag_of_Peru_(1884–1950).jpg",
         "1936": "../flags/peru/Flag_of_Peru_(1884–1950).jpg",
         "1939": "../flags/peru/Flag_of_Peru_(1884–1950).jpg"}

leader_images = {
    "1910": "../leaders/peru/Augusto_B._Leguía_(portrait)-1910.jpg",
    "1914": "../leaders/peru/330px-Guillermo_Billinghurst_3-1914.jpg",
    "1918": "../leaders/peru/PH3XONXDAZD5JLVT4XVDDVQ2W4-1918.jpg",
    "1932": "../leaders/peru/Sánchez_Cerro-1932.jpg",
    "1936": "../leaders/peru/Óscar_Benavides-1936-1939.jpg",
    "1939": "../leaders/peru/Óscar_Benavides-1936-1939.jpg"
}


class Peru(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "south america"
        self.name = "Peru"
        self.date = datetime(globe.date.year, 1, 1)
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.political_typology = "Democratic"
        self.leader = pm[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
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
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
            for i in range(len(nation_json['countries'])):
                # print(nation_json['countries'][i]['nation_name'])
                if (nation_json['countries'][i]['nation_name'] == "Peru"):
                    # print(nation_json['countries'][i]['coordinates'])
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = [(retreive_coords(self.coordinates))]