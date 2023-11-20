from datetime import datetime, timedelta
from game.ai import playable_nation
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords
leaders = {
    "1910" : "Arvid Lindman",
    "1914" : "Karl Staaff",
    "1918" : "Nils Edén",
    "1932" : "Carl Gustaf Ekman",
    "1936" : "Per Albin Hansson",
    "1939" : "Per Albin Hansson"
}
monarchs = {
    "1910" : "Gustaf V",
    "1914" : "Gustaf V",
    "1918" : "Gustaf V",
    "1932" : "Gustaf V",
    "1936" : "Gustaf V",
    "1939" : "Gustaf V"
}

population = {
    "1910": 5493302,
    "1914": 5619111,
    "1918": 5746841,
    "1932": 6172343,
    "1936": 6259363,
    "1939": 6335505
}
gdp = {
    "1910": 1765677700,
    "1914": 1035207385,
    "1918": 2754193594,
    "1932": 1911933808,
    "1936": 2344127797,
    "1939": 2892814865
}

leader_images = {
    "1910": "../leaders/sweden/330px-Arvid_Lindman_1910.jpg",
    "1914": "../leaders/sweden/Karl_Staaff_1914.jpg",
    "1918": "../leaders/sweden/Nils_Eden_1918.jpg",
    "1932": "../leaders/sweden/330px-Carl_Gustaf_Ekman_1932.jpg",
    "1936": "../leaders/sweden/330px-Per_Albin_Hansson_-_Sveriges_styresmän_1936-1939.jpg",
    "1939": "../leaders/sweden/330px-Per_Albin_Hansson_-_Sveriges_styresmän_1936-1939.jpg"
}
flags = {
    "1910": "../flags/sweden/Flag_of_Sweden.jpg",
    "1914": "../flags/sweden/Flag_of_Sweden.jpg",
    "1918": "../flags/sweden/Flag_of_Sweden.jpg",
    "1932": "../flags/sweden/Flag_of_Sweden.jpg",
    "1936": "../flags/sweden/Flag_of_Sweden.jpg",
    "1939": "../flags/sweden/Flag_of_Sweden.jpg"
}

class Sweden(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "Sweden"
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
        self.political_typology = 'Autocratic'
        self.leader = leaders[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]

        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp
        self.land = ['Sweden']
        self.coordinates = []

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        if self.date.year >= 1918:
            for land in range(0, len(self.land)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year == 1932:
            for land in range(0, len(self.land)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year == 1936:
            for land in range(0, len(self.land)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year >= 1939:
            for land in range(0, len(self.land)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))