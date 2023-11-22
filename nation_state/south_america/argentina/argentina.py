import json as js
from game.ai import playable_nation
from datetime import datetime, timedelta

from nation_data.coordination.retreive_and_convert import retreive_coords

leaders = {
    "1910" : "Roque Sáenz Peña",
    "1914" : "Victorino de la Plaza",
    "1918" : "Hipólito Yrigoyen",
    "1932" : "Agustín Pedro Justo",
    "1936" : "Agustín Pedro Justo",
    "1939" : "Roberto Marcelino Ortiz"
}

population = {
    "1910": 6814287,
    "1914": 7673303,
    "1918": 8442622,
    "1932": 12254730,
    "1936": 13306688,
    "1939": 13926663
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

class Argentina(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "argentina"
        # date variables
        self.date = datetime(globe.date.year, 1, 1)
        self.economic_change_date = self.date + timedelta(days=60)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        self.births = 0
        self.deaths = 0
        # political
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp
        self.coordinates = []

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
            for i in range(len(nation_json['countries'])):
                # print(nation_json['countries'][i]['nation_name'])
                if (nation_json['countries'][i]['nation_name'] == "Argentina"):
                    # print(nation_json['countries'][i]['coordinates'])
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))
