import json as js
import random
from datetime import datetime, timedelta

from nation_data.coordination.retreive_and_convert import retreive_coords
from game.ai.nation_ai import NationAI
population = {

    "1910": 4940000,
    "1914": 5430000,
    "1918": 5980000,
    "1932": 8350000,
    "1936": 8730000,
    "1939": 9140000
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
    "1910": "../flags/columbia/Flag_of_Colombia.jpg",
    "1914": "../flags/columbia/Flag_of_Colombia.jpg",
    "1918": "../flags/columbia/Flag_of_Colombia.jpg",
    "1932": "../flags/columbia/Flag_of_Colombia.jpg",
    "1936": "../flags/columbia/Flag_of_Colombia.jpg",
    "1939": "../flags/columbia/Flag_of_Colombia.jpg"
}

leader_images = {"1910": "../leaders/columbia/Carlos_Eugenio_Restrepo,_1910-1914.jpg",
                 "1914": "../leaders/columbia/Carlos_Eugenio_Restrepo,_1910-1914.jpg",
                 "1918": "../leaders/columbia/Jose_Vicente_Concha_LCCN20146960911_1914-1918.jpg",
                 "1932": "../leaders/columbia/Enriqueolayaherrera1-1932.jpg",
                 "1936": "../leaders/columbia/375px-Alfonso_Lopez_Pumarejo-1936.jpg",
                 "1939": "../leaders/columbia/375px-Alfonso_Lopez_Pumarejo-1936.jpg"
}

class Columbia(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "south america"
        self.name = "Columbia"
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
                if (nation_json['countries'][i]['nation_name'] == "Colombia"):
                    # print(nation_json['countries'][i]['coordinates'])
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = [(retreive_coords(self.coordinates))]

    def main(self, globe):
        while self.population > 2000000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break