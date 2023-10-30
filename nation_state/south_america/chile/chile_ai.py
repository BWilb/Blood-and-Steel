import json as js
import random
from datetime import datetime, timedelta

from nation_data.coordination.retreive_and_convert import retreive_coords
from game.ai.nation_ai import NationAI
population = {

    "1910": 3570000,
    "1914": 3760000,
    "1918": 3950000,
    "1932": 4790000,
    "1936": 5130000,
    "1939": 5400000
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

flags = {
    "1910": "../flags/chile/Flag_of_Chile.jpg",
    "1914": "../flags/chile/Flag_of_Chile.jpg",
    "1918": "../flags/chile/Flag_of_Chile.jpg",
    "1932": "../flags/chile/Flag_of_Chile.jpg",
    "1936": "../flags/chile/Flag_of_Chile.jpg",
    "1939": "../flags/chile/Flag_of_Chile.jpg"
}

leader_images = {"1910": "../leaders/britain/Pedro_Montt_(crop)-1910.jpg",
                 "1914": "../leaders/britain/330px-Barros_Luco-MHN_(cropped)-1914.jpg",
                 "1918": "../leaders/britain/330px-Jlsanfuentes-1918.png",
                 "1932": "../leaders/britain/ARTURO ALESSANDRI PALMA-1932.jpg",
                 "1936": "../leaders/britain/Bartolomé_Blanche-1932.jpeg",
                 "1939": "../leaders/britain/330px-Pedro_Aguirre_Cerda-1939.jpg"
}

class Chile(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "south america"
        self.name = "Chile"
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
                #print(nation_json['countries'][i]['nation_name'])
                if (nation_json['countries'][i]['nation_name'] == "Chile"):
                    # print(nation_json['countries'][i]['coordinates'])
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

    def main(self, globe, network):
        super().establishing_beginning_objectives()
        while self.population > 2000000:
            super().check_economic_growth(globe.date)
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            super().political_power_growth()
            super().determine_diplomatic_approach(globe.nations, globe, network)
            super().change_relations(globe.nations)
            chance = random.randrange(1, 50)
            if chance % 8 == 2 or chance % 5 == 4:
                super().protests()
            self.date += timedelta(days=1)
            break