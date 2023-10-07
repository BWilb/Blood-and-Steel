import random
from datetime import datetime, timedelta
from enum import Enum
from game.ai.nation_ai import NationAI
import json as js
from nation_data.coordination.retreive_and_convert import retreive_coords
from colors.color import Color

flags = {
    "1910": "../flags/britain/United-Kingdom-Flag.jpg",
    "1914": "../flags/britain/United-Kingdom-Flag.jpg",
    "1918": "../flags/britain/United-Kingdom-Flag.jpg",
    "1932": "../flags/britain/United-Kingdom-Flag.jpg",
    "1936": "../flags/britain/United-Kingdom-Flag.jpg",
    "1939": "../flags/britain/United-Kingdom-Flag.jpg"
}

leader_images = {"1910": "../leaders/britain/330px-Herbert_Henry_Asquith_till_1916.jpg",
                 "1914": "../leaders/britain/330px-Herbert_Henry_Asquith_till_1916.jpg",
                 "1918": "../leaders/britain/330px-David_Lloyd_George_1916-1922.jpg",
                 "1932": "../leaders/britain/J._Ramsay_MacDonald_LCCN2014715885_(cropped)_till_1935.jpg",
                 "1936": "../leaders/britain/Stanley_Baldwin_ggbain.35233_1935_1937.jpg",
                 "1939": "../leaders/britain/chamberlain_1937-1939.jpeg"
                 }

monarchs = {
    """Dictionary for english monarchs
    Leader selection will be in sync with time frame selection
    Unlike population, leader dictionary will be setup to be as historically accurate as possible"""

    "1910": "Edward VII",
    "1914": "George V",
    "1918": "George V",
    "1932": "George V",
    "1936": "Edward VIII",
    "1939": "George VI"
}

pm = {
    "1910": "H.H. Asquith",
    "1914": "H.H. Asquith",
    "1918": "David Lloyd George",
    "1932": "Ramsay MacDonald",
    "1936": "Stanley Baldwin",
    "1939": "Neville Chamberlain"
}

spare_pms = ["Duncan Pirie", "Henry Cowan", "Harold Baker", "James Calmont", "Ellis Ellis-Griffith",
             "Charles Craig", "William Jones", "Alfred Scott", "Sir Charles Hunter"]

spare_1900_1950_monarchs = ["Louis", "Prince Arthur", "Beatrice", "Prince Henry", "Alexander Ramsay",
                            "Alexander Cambridge",
                            "Albert Victor", "Victoria II", "George VI"]


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


# population variables and dictionaries
"""Dictionary for population
    Population selection will be in sync with time frame selection
    Population will then be set up to grow or shrink in random amounts"""
population = {

    "1910": 44915900,
    "1914": 42956900,
    "1918": 39582000,
    "1932": 46335000,
    "1936": 47081300,
    "1939": 46029200
}

# economic variables and dictionaries
gdp = {
    "1910": 15783763158,
    "1914": 17856842105,
    "1918": 23873207895,
    "1932": 44371994737,
    "1936": 53157368421,
    "1939": 54936947368
}


class Britain(NationAI):
    def __init__(self, globe):
        super().__init__(globe)
        self.nation_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.region = "europe"
        self.name = "Great Britain"
        self.date = datetime(globe.date.year, 1, 1)
        # social variables
        """population"""
        self.population = population[str(globe.date.year)]
        # political
        self.leader = pm[str(globe.date.year)]
        self.leader_image = leader_images[str(globe.date.year)]
        self.flag = flags[str(globe.date.year)]
        self.political_typology = "Republicanism"
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
        self.land_1910_1914 = ["United Kingdom of Great Britain and Ireland", "British East Africa",
                               "British Somaliland",
                               "Malaya", "British Protectorate", "British Raj", "Australia", "Anglo-Egyption Sudan",
                               "Egypt",
                               "Mesopotamia (GB)", "South Africa", "Botswana", "Rhodesia", "New Zealand", "Nigeria"]

        self.land_1918_1936 = ["United Kingdom of Great Britain and Ireland", "British East Africa",
                               "British Somaliland",
                               "Malaya", "British Protectorate", "British Raj", "Australia", "Sudan", "Egypt",
                               "Mesopotamia (GB)", "Union of South Africa", "Botswana", "German E. Africa (Tanganyika)",
                               "German South-West Africa", "Mandatory Palestine (GB)", "Zambia", "Zimbabwe",
                               "New Zealand", "Nigeria"]

        self.land_1939 = ["United Kingdom", "British East Africa", "British Somaliland",
                          "Malaya", "British Protectorate", "British Raj", "Australia", "Sudan", "Egypt",
                          "Mesopotamia (GB)", "Union of South Africa", "Botswana", "Tanzania, United Republic of",
                          "German South-West Africa", "Mandatory Palestine (GB)", "Dominion of Newfoundland",
                          "New Zealand",
                          "Swaziland", "Oman (British Raj)", "Nigeria"]

        self.foreign_relations = {"foreign relations": [
            {"nation name": "Iraq",
             "relations": 76.23,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Afghanistan",
             "relations": 64.34,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Iran",
             "relations": 65.43,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Turkey",
             "relations": 87.45,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "China",
             "relations": 75.45,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Japanese Empire",
             "relations": 70.65,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Austria",
             "relations": 65.45,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Kingdom of Belgium",
             "relations": 86.45,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Kingdom of Denmark",
             "relations": 88.45,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Republic of France",
             "relations": 92.34,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Germany",
             "relations": 65.23,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Kingdom of Greece",
             "relations": 76.87,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Kingdom of Italy",
             "relations": 83.23,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Kingdom of Luxembourg",
             "relations": 89.86,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Kingdom of Netherlands",
             "relations": 95.86,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Kingdom of Norway",
             "relations": 84.86,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Poland",
             "relations": 85.12,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Kingdom of Romania",
             "relations": 90.34,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Russia",
             "relations": 67.34,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Kingdom of Spain",
             "relations": 73.45,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Kingdom of Sweden",
             "relations": 87.12,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Republic of Switzerland",
             "relations": 98.75,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Dominion of Canada",
             "relations": 99.55,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Republic of Cuba",
             "relations": 82.35,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Republic of Mexico",
             "relations": 84.65,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "United States",
             "relations": 80.95,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Argentina",
             "relations": 78.94,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Brazil",
             "relations": 76.45,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Chile",
             "relations": 75.45,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Columbia",
             "relations": 73.76,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Peru",
             "relations": 65.45,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},

            {"nation name": "Venezuela",
             "relations": 73.86,
             "guarantee independence": False,
             "alliance": "",
             "war goal": False,
             "at war with": False},
        ]}
        self.improving_relations = []
        self.worsening_relations = []
        if globe.date.year <= 1932:
            self.objectives = {"objectives": [
                {"International Objectives": ["Contain Germany",
                                              "Improve relations with France",
                                              "Contend with France over Africa",
                                              "Contend with Italy over Africa",
                                              "Keep Canada in Sphere of Influence"]},

                {"National Objectives": ["Maintain positive GDP growth",
                                         "Maintain stable population growth",
                                         "Maintain 50% debt to GDP ratio",
                                         "Maintain strong military"]}
            ]}
        else:
            self.objectives = {"objectives": [
                {"International Objectives": ["Contain Germany",
                                              "Improve relations with France",
                                              "Contend with France over Africa",
                                              "Contain Italy",
                                              "Keep Canada in Sphere of Influence"]},

                {"National Objectives": ["Keep positive GDP growth",
                                         "Keep stable population growth",
                                         "Maintain strong military"]}
            ]}

            """Establishment of both national and international objectives for british AI"""
        self.allies = []
        # rival nations will have diplomacy of rate at above 50% in favorableness in Britain's eyes
        self.rivals = []
        # rival nations will have diplomacy of rate below 50% in favorableness in Britain's eyes
        self.enemies = []
        """self.long_term_mem = {{"Foreign-Policy", []},
                              {"Domestic-Policy", []}}"""
        self.short_term_mem = []
        """AI short and long term memory meant to aid in AIs decision making"""
        self.long_term_mem = {}

    def international_decision(self, foreign_nation_list, globe):
        for foreign_nation in foreign_nation_list:
            actions = ["form alliance", "guarantee independence", "improve relations", "justify war goal", "worsen relations"]
            chance = random.randrange(0, 100)

            if self.political_power >= 10:
                action = actions[random.randrange(0, len(actions))]
                if "Republicanism" or "Democratic" in foreign_nation.political_typology:
                    """Checking if political typology is democratic/republican"""
                    # choosing random action

                    if action == "guarantee independence":
                        for i in range(0, len(self.foreign_relations)):
                            if self.foreign_relations["foreign relations"][i]["nation name"] == foreign_nation.name:
                                if not self.foreign_relations["foreign relations"][i]["guarantee independence"]:
                                    if globe.tension <= 50:
                                        if chance >= 90:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True
                                    else:
                                        if chance >= 25:
                                            self.foreign_relations["foreign relations"][i]["guarantee independence"] = True

                    if action == "form alliance":
                        for i in range(0, len(foreign_nation_list)):
                            if self.foreign_relations["foreign relations"][i]["nation name"] == foreign_nation_list[i].name:
                                if not (foreign_nation_list[i].alliance and
                                        self.foreign_relations["foreign relations"][i]["alliance"]):
                                    if globe.tension <= 35:
                                        if chance >= 95:
                                            self.foreign_relations["foreign relations"][i]["alliance"] = "Anglo-Alliance"
                                            foreign_nation_list[i].alliance = "Anglo-Alliance"
                                    else:
                                        if chance >= 25:
                                            self.foreign_relations["foreign relations"][i]["alliance"] = "Anglo-Alliance"
                                            foreign_nation_list[i].alliance = "Anglo-Alliance"

                    if action == "improve relations":
                        for i in range(0, len(foreign_nation_list)):
                            if not foreign_nation_list[i].name in [foreign_nation for foreign_nation in self.improving_relations]:
                                self.improving_relations.append(foreign_nation_list[i].name)

                                if foreign_nation_list.name in [foreign_nation for foreign_nation in self.worsening_relations]:
                                    self.worsening_relations.pop(foreign_nation_list[i].name)

                    if action == "worsen relations":
                        for i in range(0, len(foreign_nation_list)):
                            if not foreign_nation_list[i].name in [foreign_nation for foreign_nation in self.worsening_relations]:
                                self.worsening_relations.append(foreign_nation_list[i].name)

                            if foreign_nation_list.name in [foreign_nation for foreign_nation in
                                                            self.improving_relations]:
                                self.improving_relations.pop(foreign_nation_list[i].name)

                elif "Communism" or "Socialism" in foreign_nation.political_typology:

                    if action == "guarantee independence":
                        for i in range(0, len(self.foreign_relations)):
                            if self.foreign_relations["foreign relations"][i]["nation name"] == foreign_nation.name:
                                if not self.foreign_relations["foreign relations"][i]["guarantee independence"]:
                                    if globe.tension <= 50:
                                        if chance >= 88:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True
                                    else:
                                        if chance >= 75:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True

                    if action == "form alliance":
                        for i in range(0, len(foreign_nation_list)):
                            if self.foreign_relations["foreign relations"][i]["nation name"] == foreign_nation_list[
                                i].name:
                                if not (foreign_nation_list[i].alliance and
                                        self.foreign_relations["foreign relations"][i]["alliance"]):
                                    if globe.tension <= 35:
                                        if chance >= 88:
                                            self.foreign_relations["foreign relations"][i][
                                                "alliance"] = "Anglo-Alliance"
                                            foreign_nation_list[i].alliance = "Anglo-Alliance"
                                    else:
                                        if chance >= 75:
                                            self.foreign_relations["foreign relations"][i][
                                                "alliance"] = "Anglo-Alliance"
                                            foreign_nation_list[i].alliance = "Anglo-Alliance"

                    if action == "improve relations":
                        for i in range(0, len(foreign_nation_list)):
                            if not foreign_nation_list[i].name in [foreign_nation for foreign_nation in
                                                                   self.improving_relations]:
                                self.improving_relations.append(foreign_nation_list[i].name)

                                if foreign_nation_list.name in [foreign_nation for foreign_nation in
                                                                self.worsening_relations]:
                                    self.worsening_relations.pop(foreign_nation_list[i].name)

                    if action == "worsen relations":
                        for i in range(0, len(foreign_nation_list)):
                            if not foreign_nation_list[i].name in [foreign_nation for foreign_nation in
                                                                   self.worsening_relations]:
                                self.worsening_relations.append(foreign_nation_list[i].name)

                            if foreign_nation_list.name in [foreign_nation for foreign_nation in
                                                            self.improving_relations]:
                                self.improving_relations.pop(foreign_nation_list[i].name)

                elif "Fascism" or "Nazism" in foreign_nation.political_typology:

                    if action == "guarantee independence":
                        for i in range(0, len(self.foreign_relations)):
                            if self.foreign_relations["foreign relations"][i]["nation name"] == foreign_nation.name:
                                if not self.foreign_relations["foreign relations"][i]["guarantee independence"]:
                                    if globe.tension <= 50:
                                        if chance >= 98:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True
                                    else:
                                        if chance >= 95:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True

                    if action == "form alliance":
                        for i in range(0, len(foreign_nation_list)):
                            if self.foreign_relations["foreign relations"][i]["nation name"] == foreign_nation_list[
                                i].name:
                                if not (foreign_nation_list[i].alliance and
                                        self.foreign_relations["foreign relations"][i]["alliance"]):
                                    if globe.tension <= 35:
                                        if chance >= 98:
                                            self.foreign_relations["foreign relations"][i][
                                                "alliance"] = "Anglo-Alliance"
                                            foreign_nation_list[i].alliance = "Anglo-Alliance"
                                    else:
                                        if chance >= 95:
                                            self.foreign_relations["foreign relations"][i][
                                                "alliance"] = "Anglo-Alliance"
                                            foreign_nation_list[i].alliance = "Anglo-Alliance"

                    if action == "improve relations":
                        for i in range(0, len(foreign_nation_list)):
                            if not foreign_nation_list[i].name in [foreign_nation for foreign_nation in
                                                                   self.improving_relations]:
                                self.improving_relations.append(foreign_nation_list[i].name)

                                if foreign_nation_list.name in [foreign_nation for foreign_nation in
                                                                self.worsening_relations]:
                                    self.worsening_relations.pop(foreign_nation_list[i].name)

                    if action == "worsen relations":
                        for i in range(0, len(foreign_nation_list)):
                            if not foreign_nation_list[i].name in [foreign_nation for foreign_nation in
                                                                   self.worsening_relations]:
                                self.worsening_relations.append(foreign_nation_list[i].name)

                            if foreign_nation_list.name in [foreign_nation for foreign_nation in
                                                            self.improving_relations]:
                                self.improving_relations.pop(foreign_nation_list[i].name)

                elif "Autocratic" in foreign_nation.political_typology:
                    if action == "guarantee independence":
                        for i in range(0, len(self.foreign_relations)):
                            if self.foreign_relations["foreign relations"][i]["nation name"] == foreign_nation.name:
                                if not self.foreign_relations["foreign relations"][i]["guarantee independence"]:
                                    if globe.tension <= 50:
                                        if chance >= 90:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True
                                    else:
                                        if chance >= 75:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True

                    if action == "form alliance":
                        for i in range(0, len(foreign_nation_list)):
                            if self.foreign_relations["foreign relations"][i]["nation name"] == foreign_nation_list[i].name:
                                if not (foreign_nation_list[i].alliance and
                                        self.foreign_relations["foreign relations"][i]["alliance"]):
                                    if globe.tension <= 35:
                                        if chance >= 95:
                                            self.foreign_relations["foreign relations"][i][
                                                "alliance"] = "Anglo-Alliance"
                                            foreign_nation_list[i].alliance = "Anglo-Alliance"
                                    else:
                                        if chance >= 75:
                                            self.foreign_relations["foreign relations"][i][
                                                "alliance"] = "Anglo-Alliance"
                                            foreign_nation_list[i].alliance = "Anglo-Alliance"

                    if action == "improve relations":
                        for i in range(0, len(foreign_nation_list)):
                            if not foreign_nation_list[i].name in [foreign_nation for foreign_nation in
                                                                   self.improving_relations]:
                                self.improving_relations.append(foreign_nation_list[i].name)

                                if foreign_nation_list.name in [foreign_nation for foreign_nation in
                                                                self.worsening_relations]:
                                    self.worsening_relations.pop(foreign_nation_list[i].name)

                    if action == "worsen relations":
                        for i in range(0, len(foreign_nation_list)):
                            if not foreign_nation_list[i].name in [foreign_nation for foreign_nation in
                                                                   self.worsening_relations]:
                                self.worsening_relations.append(foreign_nation_list[i].name)

                            if foreign_nation_list.name in [foreign_nation for foreign_nation in
                                                            self.improving_relations]:
                                self.improving_relations.pop(foreign_nation_list[i].name)
    def domestic_decision(self, domestic_issue):
        pass

    def store_in_longterm(self, decision):
        self.short_term_mem.append(decision)
        if decision in self.long_term_mem:
            """if event that occurred is in the long term memory
            increase by one
            """
            self.long_term_mem[decision] += 1

        else:
            """If event is not in long term memory
            set event in long term memory to one
            """
            self.long_term_mem[decision] = 1

    def establish_map_coordinates(self):
        # collection of coordinates will be done separately in every nation,
        # so as to access information specifically to the nation(in this case Austria)
        file_path = 'C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json'
        with open(file_path, 'r') as file:
            nation_json = js.load(file)
        if self.date.year <= 1914:
            for land in range(0, len(self.land_1910_1914)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1910_1914[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year >= 1918 and self.date.year <= 1936:
            for land in range(0, len(self.land_1918_1936)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1918_1936[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

        if self.date.year >= 1939:
            for land in range(0, len(self.land_1939)):
                for i in range(0, len(nation_json['countries'])):
                    if self.land_1939[land] == nation_json['countries'][i]['nation_name']:
                        self.coordinates.append((nation_json['countries'][i]['coordinates']))
            self.coordinates = (retreive_coords(self.coordinates))

    # main function
    def main(self, globe):
        while self.population > 2000000:
            super().check_economic_state()
            super().check_population_growth()
            # random_functions.random_functions(self, globe)
            super().stability_happiness_change(globe)
            self.date += timedelta(days=1)
            break
