import random
import time
from collections import OrderedDict
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from game.ai import playable_nation

"""Population Dictionaries"""
population = {
    "1910": 7041174,
    "1914": 7674382,
    "1918": 8302357,
    "1932": 10477365,
    "1936": 10957346,
    "1939": 11413434
}

"""Political Dictionaries"""
pms = {
    "1910": "Wilfrid Laurier",
    "1914": "Robert Borden",
    "1918": "Robert Borden",
    "1932": "R. B. Bennett",
    "1936": "William Mackenzie King",
    "1939": "William Mackenzie King"
}

gdp = {
    "1910": 50000000,
    "1914": 65993945,
    "1918": 73348873,
    "1932": 72348873,
    "1936": 72348873,
    "1939": 74348873
}

flags = {"1910": "../flags/canada/canada_flag_1920.jpg",
         "1914": "../flags/canada/canada_flag_1920.jpg",
         "1918": "../flags/canada/canada_flag_1920.jpg",
         "1932": "../flags/canada/Can-Red-Ensign-after-1921-green-leaves.jpg",
         "1936": "../flags/canada/Can-Red-Ensign-after-1921-green-leaves.jpg",
         "1939": "../flags/canada/Can-Red-Ensign-after-1921-green-leaves.jpg"}

leader_images = {
    "1910": "../leaders/canada/wilfred_laurier_1910.jpeg",
    "1914": "../leaders/canada/robert_borden_1914-1920.jpeg",
    "1918": "../leaders/canada/robert_borden_1914-1920.jpeg",
    "1932": "../leaders/canada/Wm_Lyon_Mackenzie_King_1932-1940.jpg",
    "1936": "../leaders/canada/Wm_Lyon_Mackenzie_King_1932-1940.jpg",
    "1939": "../leaders/canada/Wm_Lyon_Mackenzie_King_1932-1940.jpg"
}

class Canada(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "Canada"
        # date variables
        self.date = datetime(globe.date.year, 1, 1)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        self.births = 0
        self.deaths = 0
        # political
        self.leader = pms[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        """Stability"""
        self.stability = 95.56
        self.flag = flags[str(globe.date.year)]
        # economic
        self.national_debt = 0
        self.current_gdp = gdp[str(globe.date.year)]
        self.past_gdp = self.current_gdp