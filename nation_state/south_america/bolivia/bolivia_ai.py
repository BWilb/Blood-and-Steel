import json as js
import random
from datetime import datetime, timedelta

from nation_data.coordination.retreive_and_convert import retreive_coords
from game.ai.nation_ai import NationAI

population = {

    "1910": 44915900,
    "1914": 42956900,
    "1918": 39582000,
    "1932": 46335000,
    "1936": 47081300,
    "1939": 46029200
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

flags = {"1910": "../flags/bolivia/Flag_of_Bolivia.svg.jpg",
         "1914": "../flags/bolivia/Flag_of_Bolivia.svg.jpg",
         "1918": "../flags/bolivia/Flag_of_Bolivia.svg.jpg",
         "1932": "../flags/bolivia/Flag_of_Bolivia.svg.jpg",
         "1936": "../flags/bolivia/Flag_of_Bolivia.svg.jpg",
         "1939": "../flags/bolivia/Flag_of_Bolivia.svg.jpg"}

leader_images = {
    "1910": "../leaders/bolivia/Eliodoro_Villazón_-_2_1910.jpg",
    "1914": "../leaders/bolivia/Ismael_Montes_1914.jpg",
    "1918": "../leaders/bolivia/1918.png",
    "1932": "../leaders/bolivia/33_-_Daniel_Salamanca_(CROPPED2)_1932.jpg",
    "1936": "../leaders/bolivia/José_Luis_Tejada_Sorzano_-_1_1936.jpg",
    "1939": "../leaders/bolivia/Germán_Busch_-_2_1939.jpg"
}


class BoliviaAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "south america"
        self.name = "Bolivia"
        self.date = datetime(globe.date.year, 1, 1)
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = pm[str(globe.date.year)]
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

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
            for i in range(len(nation_json['countries'])):
                # print(nation_json['countries'][i]['nation_name'])
                if (nation_json['countries'][i]['nation_name'] == "Bolivia"):
                    # print(nation_json['countries'][i]['coordinates'])
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = [(retreive_coords(self.coordinates))]

    def main(self, globe):
        while self.population > 500000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break