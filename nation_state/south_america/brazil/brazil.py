import json as js
from datetime import datetime, timedelta

from nation_data.coordination.retreive_and_convert import retreive_coords
from game.ai import playable_nation

leaders = {
    "1910" : "Hermes da Fonseca",
    "1914" : "Hermes da Fonseca",
    "1918" : "Venceslau Brás",
    "1932" : "Getúlio Vargas",
    "1936" : "Getúlio Vargas",
    "1939" : "Getúlio Vargas"
}

population = {
    "1910": 22597037,
    "1914": 24602624,
    "1918": 26713539,
    "1932": 35498876,
    "1936": 38735746,
    "1939": 41036654
}
gdp = {
    "1910": 4659663720,
    "1914": 4847024746,
    "1918": 4953286406,
    "1932": 5037403509,
    "1936": 5228000000,
    "1939": 7037894737
}

flags = {"1910": "../flags/brazil/1280px-Flag_of_Brazil_(1889–1960).jpg",
         "1914": "../flags/brazil/1280px-Flag_of_Brazil_(1889–1960).jpg",
         "1918": "../flags/brazil/1280px-Flag_of_Brazil_(1889–1960).jpg",
         "1932": "../flags/brazil/1280px-Flag_of_Brazil_(1889–1960).jpg",
         "1936": "../flags/brazil/1280px-Flag_of_Brazil_(1889–1960).jpg",
         "1939": "../flags/brazil/1280px-Flag_of_Brazil_(1889–1960).jpg"}

leader_images = {
    "1910": "../leaders/brazil/330px-Nilo_Peçanha_02-1910.jpg",
    "1914": "../leaders/brazil/330px-Venceslau_Brás-1918.jpg",
    "1918": "../leaders/brazil/330px-Venceslau_Brás-1918.jpg",
    "1932": "../leaders/brazil/330px-Getulio_Vargas_(1930)-1932-1939.jpg",
    "1936": "../leaders/brazil/330px-Getulio_Vargas_(1930)-1932-1939.jpg",
    "1939": "../leaders/brazil/330px-Getulio_Vargas_(1930)-1932-1939.jpg"
}

class Brazil(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "brazil"
        # date variables
        self.date = datetime(globe.date.year , 1, 1)
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
        """Stability"""
        self.stability = 95.56
        # economic
        self.e_s = "recovery"
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp
        self.coordinates = []
    # population functions
    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
            for i in range(len(nation_json['countries'])):
                # print(nation_json['countries'][i]['nation_name'])
                if (nation_json['countries'][i]['nation_name'] == "Brazil"):
                    # print(nation_json['countries'][i]['coordinates'])
                    self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))