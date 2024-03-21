import random
from datetime import datetime, timedelta
from game.ai.nation_ai import NationAI
from nation_data.coordination.retreive_and_convert import retreive_coords
import json as js

leaders = {
    "1910": "Roque Sáenz Peña",
    "1914": "Victorino de la Plaza",
    "1918": "Hipólito Yrigoyen",
    "1932": "Agustín Pedro Justo",
    "1936": "Agustín Pedro Justo",
    "1939": "Roberto Marcelino Ortiz"
}

population = {
    "1910": 6750000,
    "1914": 7530000,
    "1918": 8350000,
    "1932": 12234730,
    "1936": 13116688,
    "1939": 13836663
}
gdp = {
    "1910": 2467696842,
    "1914": 2262736842,
    "1918": 2712949158,
    "1932": 5115745614,
    "1936": 6132500000,
    "1939": 7071947368
}

flags = {"1910": "../flags/argentina/Flag_of_Argentina.jpg",
         "1914": "../flags/argentina/Flag_of_Argentina.jpg",
         "1918": "../flags/argentina/Flag_of_Argentina.jpg",
         "1932": "../flags/argentina/Flag_of_Argentina.jpg",
         "1936": "../flags/argentina/Flag_of_Argentina.jpg",
         "1939": "../flags/argentina/Flag_of_Argentina.jpg"}

leader_images = {
    "1910": "../leaders/argentina/OIP-1910.jpeg",
    "1914": "../leaders/argentina/Roque_Saenz_Pena-1914.jpg",
    "1918": "../leaders/argentina/R-1914-1918.jpeg",
    "1932": "../leaders/argentina/José_Félix_Uriburu-1932.jpg",
    "1936": "../leaders/argentina/Presidente_Agustín_Pedro_Justo-1936.jpg",
    "1939": "../leaders/argentina/315px-Robertomortiz-1939.jpg"
}


class Argentina(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.name = "Argentina"
        # date variables
        self.economic_change_date = self.date + timedelta(days=120)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        self.births = 0
        self.deaths = 0
        # political
        self.political_typology = "Autocratic"
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        # economic
        """self.national_debt = 0"""
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp
        self.coordinates = []
        self.foreign_relations = {"foreign relations": []}

    def establish_foreign_objectives(self):
        objectives_enemy = ['']

        objectives_allies = ["Improve relations with Germany",
                             "Improve relations with Mexico",
                             "Improve relations with Brazil", "Improve relations with Chile",
                             'Improve relations with Bolivia', "Improve relations with Great Britain",
                             "Improve relations with United States"]

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
                if (nation_json['countries'][i]['nation_name'] == "Argentina"):
                    # print(nation_json['countries'][i]['coordinates'])
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

    # main function