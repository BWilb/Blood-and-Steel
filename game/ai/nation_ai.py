import random
import time
from enum import Enum
from datetime import datetime, timedelta
class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4
class NationAI:
    def __init__(self, globe):
        # general information
        self.region = ""
        self.name = ""
        self.date = datetime(globe.date.year, 1, 1)
        self.year_placeholder = self.date.year
        self.economic_change_date = self.date + timedelta(days=120)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        # social factors
        """population factors"""
        self.population = 0
        self.past_population = self.population
        self.birth_control = False
        self.birth_enhancer = False
        self.births = 0
        self.deaths = 0
        self.happiness = 98.56
        # political
        self.leader = "Gregory Prescov"
        self.political_typology = "Republicanism"
        self.political_power = 100
        self.political_exponent = 1.00
        """Stability"""
        self.stability = 95.56
        # economic
        self.e_s = EconomicState.RECOVERY
        self.national_debt = 0
        self.current_gdp = 0
        self.past_gdp = self.current_gdp
        self.corporate_taxes = 5.00
        self.income_taxes = 5.00
        """Components of GDP"""
        self.consumer_spending = 100
        self.investment = 100
        self.government_spending = 150
        self.exports = 500
        self.imports = 500
        self.chosen = False
        # international
        self.foreign_relations = {"foreign relations": [
            {"nation name": "name",
             "relations": 60.56,
             "relation status": "rival",
             "guaranteeing independence": False,
             "war goal": False,
             "at war with": False}
        ]}
        # nations that are potential allies of Nation will have diplomacy of rate at above 80%
        # nations that are potential rivals of Nation will have diplomacy of rate from 40 - 79%
        # nations that are potential enemies of Nation will have diplomacy of rate below 40%
        self.improving_relations = []
        self.worsening_relations = []
        """AI short and long term memory meant to aid in AIs decision making"""
        self.long_term_mem = {"Policy": [
            {"Domestic Policy": [{
                "Population": [
                    {"Birth Control": False,
                     "Birth Enhancer": False,
                     "No manipulation": True,
                     "Low growth occurrences": 0.0,
                     "Extreme growth occurrences": 0.0}
                ],
                "Economy": [
                    {}
                ],
                "Political": [
                    {"Repress Far-Left": False,
                     "Repress Far-Right": False,
                     "Repress Autocrats": False,
                     "Repress Liberals": False},
                    {"Far-Right protests": 0,
                     "Far-Left protests": 0,
                     "Autocrat protests": 0,
                     "Liberal Protests": 0}
                ]
            }],
             "Foreign Policy": []}
        ]}
        self.objectives = {"objectives":
                           [{"foreign objectives": [],
                             "domestic objectives": []
                             }]
                           }
    def check_relations_status(self, foreign_nations):
        """checking and updating status of relationship of foreign nations with Nation"""
        for foreign_nation in range(0, len(foreign_nations)):
            # looping through foreign nations list
            for foreign_relation in range(0, len(self.foreign_relations["foreign relations"])):
                if (foreign_nations[foreign_nation].name
                        == self.foreign_relations["foreign relations"][foreign_relation]["nation name"]):
                    """checking to see if a specific name within parameter matches with name
                    in foreign relations list
                    """
                    if self.foreign_relations["foreign relations"][foreign_relation]["relations"] >= 80:
                        """Checking to see if relations with foreign nation are potentially awesome"""
                        self.foreign_relations["foreign relations"][foreign_relation]["relation status"] = "ally"

                    if (self.foreign_relations["foreign relations"][foreign_relation]["relations"] < 80 and
                    self.foreign_relations["foreign relations"][foreign_relation]["relations"] > 40):
                        """Checking to see if relations with foreign nation are potentially rivalrous"""
                        self.foreign_relations["foreign relations"][foreign_relation]["relation status"] = "rival"

                    if (self.foreign_relations["foreign relations"][foreign_relation]["relations"] < 40):
                        """Checking to see if relations with foreign nation are potentially fatal"""
                        self.foreign_relations["foreign relations"][foreign_relation]["relation status"] = "enemy"

    def population_decision(self, domestic_issue):
        if (domestic_issue.keys() == "population issue" and domestic_issue.values()
        == "insignificant growth"):
            if ("maintain low population growth" in
                    list(self.objectives['objectives'][0].values())[1]):
                pass

            elif ("maintain moderate population growth" in
                    list(self.objectives['objectives'][0].values())[1]):
                if self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Control"]:

                    if self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Low growth occurrences"] >= 5:
                        self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Control"] = False
                        self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Low growth occurrences"] = 0

                    self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Low growth occurrences"] += 1

            elif ("maintain high population growth" in
                    list(self.objectives['objectives'][0].values())[1]):
                if self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Control"]:
                    """Checking to see if a measure had been made to implement birth control to control population growth
                    in nation
                    """
                    self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Control"] = False
                    self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Enhancer"] = True

        elif (domestic_issue.keys() == "population issue" and domestic_issue.values()
        == "extreme growth"):
            if ("maintain low population growth" in
                    list(self.objectives['objectives'][0].values())[1]):
                if self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Enhancer"]:
                    """Checking to see if a measure had been made to implement birth enhancer to stimulate population growth
                    in nation
                    """
                    self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Enhancer"] = False

            elif ("maintain high population growth" in
                      list(self.objectives['objectives'][0].values())[1]):
                pass

            elif ("maintain moderate population growth" in
                      list(self.objectives['objectives'][0].values())[1]):
                if self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Extreme growth occurrences"] >= 5:

                    self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Control"] = True
                    self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["No Manipulation"] = False

                    if self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Enhancer"]:
                        self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Enhancer"] = False

    def political_decision(self, political_issue):
        pass

    def economic_decision(self, economic_issue):
        pass

    def check_population_growth(self):
        if self.year_placeholder < self.date.year:
            """checking to see if an entire year has passed"""
            population_calculation = ((self.population - self.past_population) /
                                      ((self.population + self.past_population) / 2)) * 100

            if population_calculation <= 1.5:
                self.population_decision({"population issue": "insignificant growth"})
            elif population_calculation >= 7.6:
                self.population_decision({"population issue": "extreme growth"})
            else:
                self.population_decision({"population issue": "stable growth"})

        else:
            self.pop_growth()

    def pop_growth(self):
        if self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Enhancer"]:
            births = random.randrange(0, 30)
            deaths = random.randrange(0, 20)
            self.population += (births - deaths)
            self.births += births
            self.deaths += deaths

        if self.long_term_mem["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Control"]:
            births = random.randrange(0, 15)
            deaths = random.randrange(0, 20)
            self.population += (births - deaths)
            self.births += births
            self.deaths += deaths

        else:
            births = random.randrange(0, 25)
            deaths = random.randrange(0, 20)
            self.population += (births - deaths)
            self.births += births
            self.deaths += deaths
    def political_power_growth(self):
        self.political_power += self.political_exponent

    def determine_diplomatic_approach(self, foreign_nations, globe):
        if "Republicanism" or "Democratic" in self.political_typology:
            self.democratic_international_decision(foreign_nations, globe)

        if "Communism" or "Socialism" in self.political_typology:
            self.communist_international_decision(foreign_nations, globe)

        if "Fascism" or "Nazism" in self.political_typology:
            self.fascist_international_decision(foreign_nations, globe)

        if "Autocratic" or "Absolutism" in self.political_typology:
            self.autocratic_international_decision(foreign_nations, globe)
    def democratic_international_decision(self, foreign_nation_list, globe):
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
                                    if globe.tension <= 50 and chance >= 90:
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
                    """If nation that NationAI is interacting with is Far-Left"""
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
                    """If nation that NationAI is interacting with is Far-Right"""
                    if action == "guarantee independence":
                        for i in range(0, len(self.foreign_relations)):
                            if self.foreign_relations["foreign relations"][i]["nation name"] == foreign_nation.name:
                                if not self.foreign_relations["foreign relations"][i]["guarantee independence"]:
                                    if globe.tension <= 50 and chance >= 98:
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
                    """If nation that NationAI is interacting with, doesn't fit far-right or far-left"""
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
    def autocratic_international_decision(self, foreign_nation_list, globe):
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
                                        if chance >= 45:
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
                                        if chance >= 45:
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
                                        if chance >= 78:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True
                                    else:
                                        if chance >= 45:
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
    def fascist_international_decision(self, foreign_nation_list, globe):
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
                                        if chance >= 67:
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
                                        if chance >= 87:
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
                                        if chance >= 76:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True
                                    else:
                                        if chance >= 23:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True

                    if action == "form alliance":
                        for i in range(0, len(foreign_nation_list)):
                            if self.foreign_relations["foreign relations"][i]["nation name"] == foreign_nation_list[
                                i].name:
                                if not (foreign_nation_list[i].alliance and
                                        self.foreign_relations["foreign relations"][i]["alliance"]):
                                    if globe.tension <= 35:
                                        if chance >= 89:
                                            self.foreign_relations["foreign relations"][i][
                                                "alliance"] = "Anglo-Alliance"
                                            foreign_nation_list[i].alliance = "Anglo-Alliance"
                                    else:
                                        if chance >= 34:
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
                                        if chance >= 65:
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
                                        if chance >= 55:
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
    def communist_international_decision(self, foreign_nation_list, globe):
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
                                        if chance >= 95:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True
                                    else:
                                        if chance >= 65:
                                            self.foreign_relations["foreign relations"][i]["guarantee independence"] = True

                    if action == "form alliance":
                        for i in range(0, len(foreign_nation_list)):
                            if self.foreign_relations["foreign relations"][i]["nation name"] == foreign_nation_list[i].name:
                                if not (foreign_nation_list[i].alliance and
                                        self.foreign_relations["foreign relations"][i]["alliance"]):
                                    if globe.tension <= 35:
                                        if chance >= 99:
                                            self.foreign_relations["foreign relations"][i]["alliance"] = "Anglo-Alliance"
                                            foreign_nation_list[i].alliance = "Anglo-Alliance"
                                    else:
                                        if chance >= 45:
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
                                        if chance >= 45:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True
                                    else:
                                        if chance >= 15:
                                            self.foreign_relations["foreign relations"][i][
                                                "guarantee independence"] = True

                    if action == "form alliance":
                        for i in range(0, len(foreign_nation_list)):
                            if self.foreign_relations["foreign relations"][i]["nation name"] == foreign_nation_list[
                                i].name:
                                if not (foreign_nation_list[i].alliance and
                                        self.foreign_relations["foreign relations"][i]["alliance"]):
                                    if globe.tension <= 35:
                                        if chance >= 68:
                                            self.foreign_relations["foreign relations"][i][
                                                "alliance"] = "Anglo-Alliance"
                                            foreign_nation_list[i].alliance = "Anglo-Alliance"
                                    else:
                                        if chance >= 35:
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
    # economic functions
    def check_economic_state(self):
        """function dealing with primary economic decisions"""

        if self.e_s == EconomicState.RECESSION or self.e_s == EconomicState.DEPRESSION:
            self.neg_ec_growth()

        elif self.e_s == EconomicState.RECOVERY or self.e_s == EconomicState.EXPANSION:
            self.pos_ec_growth()
    def provide_economic_aid(self):
        pass

    def pos_ec_growth(self):
        self.national_debt += round(
            (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)

        self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                             (self.exports - self.imports))
    def neg_ec_growth(self):
        self.national_debt += round(self.government_spending * round(random.uniform(0.15, 0.35), 4), 2)

        self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                             (self.exports - self.imports))
    # stability functions
    def stability_happiness_change(self, globe):
        if globe.tension > 25 and globe.tension < 50:
            """if global tension is between 25 and 50"""
            if self.e_s.RECESSION or self.e_s.DEPRESSION:
                if self.improve_stability > self.date:
                    """if improving of stability has been activated"""
                    stability_increase = round(random.uniform(0.25, 1.56), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_increase = round(random.uniform(0.25, 1.25), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    happiness_increase = round(random.uniform(1.56, 2.56), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

                else:
                    happiness_increase = round(random.uniform(1.25, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

            else:
                if self.improve_stability > self.date:
                    stability_increase = round(random.uniform(0.50, 1.75), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_increase = round(random.uniform(0.45, 1.65), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    """if improving of happiness has been activated
                    improved happiness improves stability
                    """
                    happiness_increase = round(random.uniform(1.75, 2.76), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
                else:
                    happiness_increase = round(random.uniform(1.25, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

        elif globe.tension > 50 and globe.tension < 75:
            """if global tension is between 50 and 75"""
            if self.e_s.RECESSION or self.e_s.DEPRESSION:
                if self.improve_stability > self.date:
                    stability_increase = round(random.uniform(0.10, 1.25), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_increase = round(random.uniform(0.05, 1.05), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    """if improving of happiness has been activated
                    improved happiness improves stability
                    """
                    happiness_increase = round(random.uniform(1.15, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
                else:
                    happiness_increase = round(random.uniform(1.15, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
            else:
                if self.improve_stability > self.date:
                    stability_increase = round(random.uniform(0.13, 0.96), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_increase = round(random.uniform(0.10, 0.76), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    """if improving of happiness has been activated
                    improved happiness improves stability
                    """
                    happiness_increase = round(random.uniform(1.05, 1.96), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
                else:
                    happiness_increase = round(random.uniform(0.96, 1.56), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

        elif globe.tension > 75:
            """if global tension is above 75"""
            if self.e_s.RECESSION or self.e_s.DEPRESSION:
                if self.improve_stability > self.date:
                    """if improving of stability has been activated"""
                    stability_increase = round(random.uniform(0.05, 0.75), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                else:
                    stability_decrease = round(random.uniform(1.56, 3.75), 2)
                    if (self.stability - stability_decrease) > 5:
                        self.stability -= stability_decrease

                if self.improve_happiness > self.date:
                    stability_increase = round(random.uniform(0.05, 0.99), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_decrease = round(random.uniform(1.56, 2.56), 2)
                    if (self.stability - stability_decrease) > 5:
                        self.stability -= stability_decrease

            else:
                if self.improve_stability > self.date:
                    stability_increase = round(random.uniform(1.56, 2.56), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                else:
                    stability_increase = round(random.uniform(1.45, 2.34), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    """If policies toward improving happiness have been imposed"""
                    happiness_increase = round(random.uniform(1.05, 2.96), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
                else:
                    happiness_increase = round(random.uniform(0.96, 2.56), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

        else:
            if self.improve_stability > self.date:
                stability_increase = round(random.uniform(1.56, 2.56), 2)
                if (self.stability + stability_increase) < 100:
                    self.stability += stability_increase

            else:
                stability_increase = round(random.uniform(1.45, 2.34), 2)
                if (self.stability + stability_increase) < 100:
                    self.stability += stability_increase

            if self.improve_happiness > self.date:
                """If policies toward improving happiness have been imposed"""
                happiness_increase = round(random.uniform(1.05, 2.96), 2)
                if (self.happiness + happiness_increase) < 100:
                    self.happiness += happiness_increase
            else:
                happiness_increase = round(random.uniform(0.96, 2.56), 2)
                if (self.happiness + happiness_increase) < 100:
                    self.happiness += happiness_increase