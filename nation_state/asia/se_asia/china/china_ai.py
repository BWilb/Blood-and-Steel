import random
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


leaders = {
    "1910": "Emperor Xuantong",
    "1914": "Yuan Shikai",
    "1918": "Xu Shichangi",
    "1932": "Lin Sen",
    "1936": "Lin Sen",
    "1939": "Lin Sen"
}
monarchs = {
    "1910": "Emperor Xuantong",
    "1914": "Emperor Xuantong",
    "1918": "Emperor Xuantong",
    "1932": "Emperor Xuantong",
    "1936": "Emperor Xuantong",
    "1939": "Emperor Xuantong"
}

population = {
    "1910": 419060000,
    "1914": 436080000,
    "1918": 455340000,
    "1932": 487880000,
    "1936": 499550000,
    "1939": 508420000
}
gdp = {
    "1910": 17340421053,
    "1914": 19231073684,
    "1918": 23090862632,
    "1932": 48070526316,
    "1936": 60420631579,
    "1939": 54934157895
}

flags = {"1910": "../flags/china/1024px-flag_of_the_qing_dynasty_1889-1912-jpg.webp",
         "1914": "../flags/china/Flag_of_China_(1912–1928).flag.png",
         "1918": "../flags/china/Flag_of_China_(1912–1928).flag.png",
         "1932": "../flags/china/Flag_of_the_Republic_of_China.jpg",
         "1936": "../flags/china/Flag_of_the_Republic_of_China.jpg",
         "1939": "../flags/china/Flag_of_the_Republic_of_China.jpg"}

leader_images = {
    "1910": "../leaders/china/Pu_Yi,_Qing_dynasty,_China,_Last_emperor-1910.jpg",
    "1914": "../leaders/china/YuanShikaiPresidente1914.jpg",
    "1918": "../leaders/china/Feng-Kwo-Chang,_President_of_China_(9to12)-1918.jpg",
    "1932": "../leaders/china/Lin_Sen-1932-1939.jpg",
    "1936": "../leaders/china/Lin_Sen-1932-1939.jpg",
    "1939": "../leaders/china/Lin_Sen-1932-1939.jpg"
}

class ChinaAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.name = "China"
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
        # other
        self.coordinates = []
        self.foreign_relations = {"foreign relations": []}
        self.land_1910 = ["Mongolia", "Manchu Empire", "Tibet", "Xinjiang"]
        self.land_1914_1918 = ["Manchu Empire", "Tibet", "Xinjiang"]
        self.land_1932_1936 = ["Chinese Warlords"]
        self.land_1939 = ["Chinese Warlords"]

    def establish_foreign_objectives(self):
        pass

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

            if self.date.year <= 1918:
                for i in range(len(nation_json['countries'])):
                    # print(nation_json['countries'][i]['nation_name'])
                    if (nation_json['countries'][i]['nation_name'] == "Manchu Empire" or
                            nation_json['countries'][i]['nation_name'] == "Tibet" or
                            nation_json['countries'][i]['nation_name'] == "Xinjiang" or
                            nation_json['countries'][i]['nation_name'] == "Mongolia"):
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
                    if "Manchu Empire" == nation_json['countries'][i]['nation_name']:
                        print("Hi", nation_json['countries'][i]['coordinates'])
                self.coordinates = (retreive_coords(self.coordinates))


            elif 1931 < self.date.year < 1937:
                for i in range(len(nation_json['countries'])):
                    # print(nation_json['countries'][i]['nation_name'])
                    if (nation_json['countries'][i]['nation_name'] == "Chinese Warlords"):
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
                self.coordinates = (retreive_coords(self.coordinates))

            elif self.date.year >= 1939:
                for i in range(len(nation_json['countries'])):
                    # print(nation_json['countries'][i]['nation_name'])
                    if (nation_json['countries'][i]['nation_name'] == "Chinese warlords"):
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
                self.coordinates = (retreive_coords(self.coordinates))