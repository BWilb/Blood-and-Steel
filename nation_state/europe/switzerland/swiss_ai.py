import random
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords

from game.ai.nation_ai import NationAI

leaders = {
    "1910" : "Robert Comtesse",
    "1914" : "Arthur Hoffmann",
    "1918" : "Felix Calonder",
    "1932" : "Giuseppe Motta",
    "1936" : "Albert Meyer",
    "1939" : "Philipp Etter"
}

population = {
    "1910": 3710000,
    "1914": 3780000,
    "1918": 3848000,
    "1932": 4081500,
    "1936": 4156167,
    "1939": 4204833
}
gdp = {
    "1910": 1765677700,
    "1914": 1975776780,
    "1918": 2021174168,
    "1932": 1595825500,
    "1936": 2443434342,
    "1939": 2061627844
}

flags = {"1910": "../flags/switzerland/Flag_of_Switzerland_(Pantone).svg.png",
         "1914": "../flags/switzerland/Flag_of_Switzerland_(Pantone).svg.png",
         "1918": "../flags/switzerland/Flag_of_Switzerland_(Pantone).svg.png",
         "1932": "../flags/switzerland/Flag_of_Switzerland_(Pantone).svg.png",
         "1936": "../flags/switzerland/Flag_of_Switzerland_(Pantone).svg.png",
         "1939": "../flags/switzerland/Flag_of_Switzerland_(Pantone).svg.png"}

leader_images = {
    "1910": "../leaders/switzerland/02034_1910.jpg",
    "1914": "../leaders/switzerland/200px-Arthur_Hoffmann_IMG_1914.jpg",
    "1918": "../leaders/switzerland/Felix_Calonder_1918.jpg",
    "1932": "../leaders/switzerland/Giuseppe_Motta_circa_1915_1932.jpg",
    "1936": "../leaders/switzerland/gettyimages-541795457-612x612_1936.jpg",
    "1939": "../leaders/switzerland/Philip_Etter_Staatsarchiv_Bern_FN_Jost_P_365_1939.jpg"
}

class SwitzerlandAI(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Switzerland"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.political_typology = "Democratic"
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
        # other
        self.coordinates = []
        self.foreign_relations = {"foreign relations": []}

    def establish_foreign_objectives(self):
        objectives_allies = ["Improve relations with France", "Improve relations with Russia",
                             "Improve relations with United States",
                             "Improve relations with Germany", "Improve relations with Italy",
                             "Improve relations with Great Britain"]

        for ally in objectives_allies:
            self.objectives["objectives"][0]['foreign'].append(ally)
    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        for i in range(len(nation_json['countries'])):
            if (nation_json['countries'][i]['nation_name'] == "Switzerland"):
                self.coordinates.append((nation_json['countries'][i]['coordinates']))
        self.coordinates = (retreive_coords(self.coordinates))