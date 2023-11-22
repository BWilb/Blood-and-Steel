from datetime import datetime, timedelta
from enum import Enum
from game.ai import playable_nation
from nation_data.coordination.retreive_and_convert import retreive_coords
import json as js
import random

#from random_functions import random_functions

"""Population Dictionaries"""
population = {
    "1910": 14502456,
    "1914": 14532623,
    "1918": 17242786,
    "1932": 17635255,
    "1936": 18471701,
    "1939": 19511661
}

"""Political Dictionaries"""
leaders = {
    "1910": "Porfirio Diaz",
    "1914": "Victoriano Huerta",
    "1918": "Venustiano Carranza",
    "1932": "Abelardo Rodriguez",
    "1936": "Lázaro Cárdenas",
    "1939": "Lázaro Cárdenas"
}

gdp = {
    "1910": 500000000,
    "1914": 659939450,
    "1918": 733488730,
    "1932": 723488730,
    "1936": 723488730,
    "1939": 743488730
}

flags = {
    "1910": "../flags/mexico/150px-Bandera_de_México_(1880-1914).jpg",
    "1914": "../flags/mexico/150px-Bandera_de_México_(1880-1914).jpg",
    "1918": "../flags/mexico/1920px-Bandera_de_la_Tercera_República_Federal_de_los_Estados_Unidos_Mexicanos(1916-1932).jpg",
    "1932": "../flags/mexico/1920px-Bandera_de_la_Tercera_República_Federal_de_los_Estados_Unidos_Mexicanos(1916-1932).jpg",
    "1936": "../flags/mexico/1920px-Bandera_de_la_Tercer_República_Federal_de_los_Estados_Unidos_Mexicanos_modelo_1934.jpg",
    "1939": "../flags/mexico/1920px-Bandera_de_la_Tercer_República_Federal_de_los_Estados_Unidos_Mexicanos_modelo_1934.jpg"
}
leader_images = {"1910": "../leaders/mexico/Porfirio_Diaz_en_1867.jpg",
                 "1914": "../leaders/mexico/huerta_1914.jpg",
                 "1918": "../leaders/mexico/s20_15_venustiano-768x1024_1918.jpg",
                 "1932": "../leaders/mexico/OIP_1932.jpeg",
                 "1936": "../leaders/mexico/lazaro_1936_1939.jpeg",
                 "1939": "../leaders/mexico/lazaro_1936_1939.jpeg"
                 }

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class Mexico(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "North America"
        self.name = "Mexico"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.political_typology = "Autocratic"
        self.leader = leaders[str(globe.date.year)]
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
        self.coordinates = []

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        for i in range(len(nation_json['countries'])):
            print(nation_json['countries'][i]['nation_name'])
            if nation_json['countries'][i]['nation_name'] == "Mexico":
                # print(nation_json['countries'][i]['coordinates'])
                self.coordinates = [((nation_json['countries'][i]['coordinates']))]
        self.coordinates = [(retreive_coords(self.coordinates))]