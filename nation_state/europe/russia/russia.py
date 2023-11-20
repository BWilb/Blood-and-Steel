from game.ai import playable_nation
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords
import random

leaders = {
    "1910": "Nicolaus II",
    "1914": "Nicolaus II",
    "1918": "Vladimir Lenin",
    "1932": "Joseph Stalin",
    "1936": "Joseph Stalin",
    "1939": "Joseph Stalin"
}


population = {
    "1910": 126200000,
    "1914": 130000000,
    "1918": 136800000,
    "1932": 126000000,
    "1936": 104900000,
    "1939": 109397463
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": 12003528421,
    "1914": 15085307368,
    "1918": 14723268421,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

flags = {"1910": "../flags/russia/Flag_of_Russia.jpg",
         "1914": "../flags/russia/Flag_of_Russia.jpg",
         "1918": "../flags/russia/Flag_of_Russia.jpg",
         "1932": "../flags/russia/Flag_of_the_Soviet_Union_(1924–1936).jpg",
         "1936": "../flags/russia/Flag_of_the_Soviet_Union_(1924–1936).jpg",
         "1939": "../flags/russia/Flag_of_the_USSR_(1936-1955).jpg"}

leader_images = {
    "1910": "../leaders/russia/800px-Mikola_II_(cropped)-2.jpg",
    "1914": "../leaders/russia/800px-Mikola_II_(cropped)-2.jpg",
    "1918": "../leaders/russia/800px-Mikola_II_(cropped)-2.jpg",
    "1932": "../leaders/russia/Joseph_Stalin,_1950_(cropped).jpg",
    "1936": "../leaders/russia/Joseph_Stalin,_1950_(cropped).jpg",
    "1939": "../leaders/russia/Joseph_Stalin,_1950_(cropped).jpg"
}

class Russia(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.spare_color = self.nation_color
        self.region = "europe"
        self.name = "Russia"
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        if self.date.year <= 1918:
            self.political_typology = "Autocratic"
        else:
            self.political_typology = "Communist"

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

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)

        if self.date.year <= 1918:
            # Azerbaijan
            # Armenia
            for i in range(len(nation_json['countries'])):
                if (nation_json['countries'][i]['nation_name'] == "Russian Empire" or nation_json['countries'][i]['nation_name']
                        == "Finland" or nation_json['countries'][i]['nation_name'] == "Azerbaijan" or
                        nation_json['countries'][i]['nation_name'] == "Armenia" or nation_json['countries'][i][
                            'nation_name'] == "Georgia"):
                    # print(nation_json['countries'][i]['coordinates'])
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
                    print(self.coordinates)
            self.coordinates = (retreive_coords(self.coordinates))
        if self.date.year > 1918 and self.date.year < 1932:
            for i in range(len(nation_json['countries'])):
                if nation_json['countries'][i]['nation_name'] == "USSR" or nation_json['countries'][i]['nation_name'] \
                        == "White Russia":
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year >= 1932:
            print('hi')
            for i in range(len(nation_json['countries'])):
                if (nation_json['countries'][i]['nation_name'] == "USSR"
                        or nation_json['countries'][i]['nation_name'] == "White Russia" or
                        nation_json['countries'][i]['nation_name'] == "Ukraine"):
                    # print(nation_json['countries'][i]['coordinates'])
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))