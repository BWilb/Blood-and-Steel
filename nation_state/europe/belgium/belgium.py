import random
import time
from datetime import datetime, timedelta

from game.ai import playable_nation
from nation_data.coordination.retreive_and_convert import convert_coords, retreive_coords
import json as js

"""Population Dictionaries"""
population = {
    "1910": 7395408,
    "1914": 7447647,
    "1918": 7355778,
    "1932": 8118461,
    "1936": 8210392,
    "1939": 8280500
}

"""Political Dictionaries"""
leaders = {
    "1910": "Frans Schollaert",
    "1914": "Charles de Broqueville",
    "1918": "Charles de Broqueville",
    "1932": "Jules Renkin",
    "1936": "Paul van Zeeland",
    "1939": "Hubert Pierlot"
}

monarchs = {
    "1910": "Albert I",
    "1914": "Albert I",
    "1918": "Albert I",
    "1932": "Albert I",
    "1936": "Leopold III",
    "1939": "Leopold III"
}

gdp = {
    "1910": 865645049,
    "1914": 1111426098,
    "1918": 1844390540,
    "1932": 2118539364,
    "1936": 3213537630,
    "1939": 3201339327
}

flags = {"1910": "../flags/belgium/belgian_flag.jpg",
         "1914": "../flags/belgium/belgian_flag.jpg",
         "1918": "../flags/belgium/belgian_flag.jpg",
         "1932": "../flags/belgium/belgian_flag.jpg",
         "1936": "../flags/belgium/belgian_flag.jpg",
         "1939": "../flags/belgium/belgian_flag.jpg"}

leader_images = {
    "1910": "../leaders/belgium/Schollaert_1910.jpg",
    "1914": "../leaders/belgium/800px-Comte_de_Broqueville_1914-1918.jpg",
    "1918": "../leaders/belgium/800px-Comte_de_Broqueville_1914-1918.jpg",
    "1932": "../leaders/belgium/800px-Comte_de_Broqueville_1914-1918.jpg",
    "1936": "../leaders/belgium/Paul_van_Zeeland,_1936.jpg",
    "1939": "../leaders/belgium/375px-Hubert_Pierlot_1939.jpg"
}


class Belgium(playable_nation.PlayableNation):
    def __init__(self, globe):
        super().__init__(globe)
        self.name = "Kingdom of Belgium"
        self.nation_color = (0, random.randrange(0, 255), random.randrange(0, 250))
        # date variables
        self.date = datetime(globe.date.year, 1, 1)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        self.economic_change_date = self.date + timedelta(days=60)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        self.births = 0
        self.deaths = 0
        self.birth_control = False
        self.birth_enhancer = False
        """happiness"""
        self.happiness = 98.56
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
        self.income_tax_rate = 25.00
        self.corporate_tax_rate = 35.00
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # international
        self.alliance = ""
        self.improving_relations = []
        self.worsening_relations = []
        self.embargoed_nations = []
        self.foreign_relations = {
            "Austria": 77.67,
            "Great Britain": 89.56,
            "Kingdom of Denmark": 80.56,
            "Republic of France": 88.45,
            "Germany": 75.56,
            "Kingdom of Greece": 80.56,
            "Kingdom of Italy": 88.00,
            "Kingdom of Luxembourg": 94.56,
            "Kingdom of Netherlands": 92.34,
            "Kingdom of Norway": 88.88,
            "Poland": 90.56,
            "Kingdom of Romania": 91.24,
            "Russia": 78.45,
            "Kingdom of Sweden": 85.56,
            "Republic of Switzerland": 100,
            "Dominion of Canada": 98.56,
            "Republic of Cuba": 100,
            "Republic of Mexico": 89.98,
            "Afghanistan": 89.45,
            "Iran": 88.23,
            "Iraq": 89.12,
            "Turkey": 78.45,
            "China": 82.34,
            "Japanese Empire": 75.67,
            "Brazil": 56.65,
            "Venezuela": 86.45,
            "Argentina": 67.45
        }
        # drawing
        self.coordinates = []
        # other
        self.sprite = False
        self.land_1910_1918 = ["Belgium", "Belgian Congo"]
        self.land_1932_1939 = ["Belgium", "Belgian Congo", "Rwanda (Belgium)", "Burundi"]
        self.chosen = True

    def establish_map_coordinates(self):
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        if self.date.year < 1932:
            for land in range(0, len(self.land_1910_1918)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1910_1918[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year >= 1932:
            for land in range(0, len(self.land_1932_1939)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1932_1939[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

    def improve_relations(self):
        for nation, relations in self.foreign_relations.items():
            # looping through items in foreign relations
            for i in range(0, len(self.improving_relations)):
                # looping through list of nations that user is improving relations with(based off of network variable in sprite game)
                if nation == self.improving_relations[i]:
                    if self.foreign_relations[nation] + 0.5 <= 100:
                        self.foreign_relations[nation] += 0.5

        #print(self.improving_relations)