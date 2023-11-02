import random
import json as js
from nation_data.coordination.retreive_and_convert import convert_coords, retreive_coords
from game.ai import playable_nation
"""Population Dictionaries"""
population = {
    "1910": 7145835,
    "1914": 7642710,
    "1918": 7882960,
    "1932": 18143247,
    "1936": 18997248,
    "1939": 19868002
}

"""Political Dictionaries"""
leaders = {
    "1910": "Ion I. C. Brătianu",
    "1914": "Ion I. C. Brătianu",
    "1918": "Ion I. C. Brătianu",
    "1932": "Nicolae Iorga",
    "1936": "Gheorghe Tătărescu",
    "1939": "rmand Călinescu"
}

monarchs = {
    "1910": "Carol I",
    "1914": "Carol I",
    "1918": "Ferdinand I",
    "1932": "Carol II",
    "1936": "Carol II",
    "1939": "Carol II"
}

gdp = {
    "1910": 11882323232,
    "1914": 11982323232,
    "1918": 12182323232,
    "1932": 14212323232,
    "1936": 18882323232,
    "1939": 19882323232
}

flags = {"1910": "../flags/romania/romania.jpeg",
         "1914": "../flags/romania/romania.jpeg",
         "1918": "../flags/romania/romania.jpeg",
         "1932": "../flags/romania/romania.jpeg",
         "1936": "../flags/romania/romania.jpeg",
         "1939": "../flags/romania/romania.jpeg"}

leader_images = {
    "1910": "../leaders/romania/Carp_(The_Road_to_Romanian_Independence)_1910.jpeg",
    "1914": "../leaders/romania/IonelBratianu3b40761r_1914-1918.jpg",
    "1918": "../leaders/romania/IonelBratianu3b40761r_1914-1918.jpg",
    "1932": "../leaders/romania/Iorga_at_his_desk_Luceaferul_2,_1914-1932.jpg",
    "1936": "../leaders/romania/255px-Gheorghe_Tătărescu-1936.jpg",
    "1939": "../leaders/romania/Miron_Cristia_patriach_of_Romania-1939.jpeg"
}

class Romania(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Kingdom of Romania"
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
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        for i in range(len(nation_json['countries'])):
            if (nation_json['countries'][i]['nation_name'] == "Romania"):
                self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = [(retreive_coords(self.coordinates))]

        return self.coordinates