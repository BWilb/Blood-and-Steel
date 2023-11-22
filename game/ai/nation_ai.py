import random
import time
from enum import Enum
from datetime import datetime, timedelta

import military.soldier
from military import soldier

class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


class NationAI:
    def __init__(self, globe):
        # general information
        self.is_chosen = False
        self.date_checker = globe.date + timedelta(days=3)
        self.conscripting_checker = globe.date
        self.recruiting_checker = globe.date + timedelta(days=5)
        self.region = ""
        self.name = ""
        self.date = datetime(globe.date.year, 1, 1)
        self.year_placeholder = self.date.year
        self.economic_change_date = self.date + timedelta(days=120)
        # social factors
        """population factors"""
        self.population = 1000000
        self.past_population = self.population
        self.births = 0
        self.deaths = 0
        # political
        self.leader = "Gregory Prescov"
        self.alliance = ""
        self.political_typology = "Republicanism"
        self.political_power = 100
        self.political_exponent = 1.00
        # economic
        self.e_s = EconomicState.RECOVERY
        self.national_debt = 0
        self.current_gdp = 0
        self.past_gdp = self.current_gdp
        """Components of GDP"""
        self.consumer_spending = 100
        self.investment = 100
        self.government_spending = 150
        self.exports = 500
        self.imports = 500
        # international
        self.foreign_relations = {"foreign relations": [
            {"nation name": "name",
             "relations": 60.56,
             "relation status": "rival",
             "guaranteeing independence": False,
             "alliance": "",
             "embargoed": False,
             "war goal": False,
             "at war with": False}
        ]}
        # nations that are potential allies of Nation will have diplomacy of rate at above 80%
        # nations that are potential rivals of Nation will have diplomacy of rate from 40 - 79%
        # nations that are potential enemies of Nation will have diplomacy of rate below 40%
        self.improving_relations = []
        self.worsening_relations = []
        """National policy variable stores information that is similar and regards to the Domesticity and 
        foreign status of the AI
        """
        self.national_policy = {"Policy": [
            {"Domestic Policy": [{
                "Population": [
                    {"Birth Control": False,
                     "Birth Enhancer": False,
                     "No manipulation": True,
                     "Low growth occurrences": 0.0,
                     "Stable growth occurrences": 0.0,
                     "Extreme growth occurrences": 0.0},
                    {"Happiness": 88.56}
                    # growth occurrences will be growth that is consistent, once change happens set back to 0
                ],
                "Economy": [
                    {"debt interest payment rate": 2.00},
                    {"Economic stability": 87.56,
                     "Improving ES": False}
                ],
                "Political": [
                    {"Repress Far-Left": False,
                     "Repress Far-Right": False,
                     "Repress Autocrats": False,
                     "Repress Liberals": False},
                    {"Political stability": 90.0,
                     "Improving PS": False}
                    # for political rewards to be utilized, AI must make political decision
                    # for example if there is a far left protest and the AI handles the protest by killing everyone...
                    # then political rewards would be decreased and the action and the outcome of the action would be stored in long term
                    # memory
                ]
            }]},
            {"Foreign Policy": [{
                    "Allies": [],
                    "Rivals": [],
                    "Enemies": [],
                    "Alliance": ""
            }]}
        ]}

        self.objectives = {
            "objectives": [
                {
                    'foreign': []
                },
                {
                    'domestic': [
                        {
                            'population objectives': [],
                            'economic objectives': [],
                            'political objectives': [],
                            'social objectives': []
                        }
                    ]
                }
            ]
        }

        self.long_term_memory = [
            {
                "Domestic Decisions": {
                    "Economic": [],
                    "Population": [],
                    "Political": []
                },
                "Domestic problems": [
                    {"Protests": []}
                ],
                "Domestic Ideologies":{
                    "Democratic": 100,
                    "Fascist": 0,
                    "Communist": 0,
                    "Autocratic": 0
                }
            },
            {
                "Foreign Decisions":
                    {
                        "Allies": [],
                        "Enemies": []
                    },
                "Foreign Influence": []
            }
        ]

        # long term memory stores decisions made by the AI. Used by the AI as game advances, to aid in policymaking
        self.military = {
            "military": {
                "Conscription policy": "Volunteer",
                "Army": {
                    "Figures": {
                        "Army size": [],
                        "Cost": 0
                    }
                },
            },
            "conscript pool": 0,
        }
    # political faction functions
    def determine_ideological_appeals(self):
        if self.political_typology == "Democratic":
            self.democratic_appeal = 90
            self.communist_appeal = 3
            self.fascist_appeal = 4
            self.autocratic_appeal = 3

        if self.political_typology == "Autocratic":
            self.democratic_appeal = 15
            self.communist_appeal = 5
            self.fascist_appeal = 5
            self.autocratic_appeal = 75

        if self.political_typology == "Fascist":
            self.democratic_appeal = 0
            self.communist_appeal = 20
            self.fascist_appeal = 80
            self.autocratic_appeal = 0

        if self.political_typology == "Communist":
            self.democratic_appeal = 10
            self.communist_appeal = 75
            self.fascist_appeal = 10
            self.autocratic_appeal = 5

    # military functions
    def adding_conscription_pool(self, globe):
        self.check_conscprtion_policy(globe)
        if self.conscripting_checker < globe.date:
            if "Volunteer" in self.military['military']['Conscription policy']:
                if self.military['conscript pool'] + self.population * 0.001 < self.population:
                    self.military['conscript pool'] += self.population * 0.001
                    self.conscripting_checker += timedelta(days=30)

            if "Limited" in self.military['military']['Conscription policy']:
                if self.military['conscript pool'] + self.population * 0.005 < self.population:
                    self.military['conscript pool'] += self.population * 0.005
                    self.conscripting_checker += timedelta(days=30)

            if "Extensive" in self.military['military']['Conscription policy']:
                if self.military['conscript pool'] + self.population * 0.01 < self.population:
                    self.military['conscript pool'] += self.population * 0.01
                    self.conscripting_checker += timedelta(days=30)

            if "Total War" in self.military['military']['Conscription policy']:
                if self.military['conscript pool'] + self.population * 0.09 < self.population:
                    self.military['conscript pool'] += self.population * 0.09
                    self.conscripting_checker += timedelta(days=30)

        self.recruit_from_pool(globe)
        self.check_soldier_deployment(globe)

    def check_conscprtion_policy(self, globe):
        for relations in self.foreign_relations['foreign relations']:

            if globe.tension <= 25:
                if "Volunteer" not in self.military['military']['Conscription policy']:
                    self.military['military']['Conscription policy'] = "Volunteer"

            elif 25 < globe.tension < 55:
                if "Limited" not in self.military['military']['Conscription policy']:
                    self.military['military']['Conscription policy'] = "Limited"

            elif 55 < globe.tension < 75:
                if "Extensive" not in self.military['military']['Conscription policy']:
                    self.military['military']['Conscription policy'] = "Extensive"

            elif globe.tension >= 75 or relations['at war with']:
                if "Total War" not in self.military['military']['Conscription policy']:
                    self.military['military']['Conscription policy'] = "Total War"

    def recruit_from_pool(self, globe):
        if (self.national_debt / self.current_gdp) * 100 < 50:

            if globe.date > self.recruiting_checker:
                self.recruiting_checker = globe.date + timedelta(days=5)

                if globe.tension <= 25:
                    recruits = (self.military['conscript pool'] * 0.01)
                    for i in range(0, int(recruits)):
                        soldier = military.soldier.Soldier(self.name, globe)
                        self.military['military']['Army']['Figures']["Army size"].append(soldier)
                        self.military['military']['Army']['Figures']["Cost"] += soldier.monetary_cost
                        self.national_debt += soldier.monetary_cost

                elif 25 < globe.tension < 55:
                    recruits = (self.military['conscript pool'] * 0.05)
                    for i in range(0, int(recruits)):
                        soldier = military.soldier.Soldier(self.name, globe)
                        self.military['military']['Army']['Figures']["Army size"].append(soldier)
                        self.military['military']['Army']['Figures']["Cost"] += soldier.monetary_cost
                        self.national_debt += soldier.monetary_cost

                elif 55 <= globe.tension < 75:
                    recruits = (self.military['conscript pool'] * 0.09)
                    for i in range(0, int(recruits)):
                        soldier = military.soldier.Soldier(self.name, globe)
                        self.military['military']['Army']['Figures']["Army size"].append(soldier)
                        self.military['military']['Army']['Figures']["Cost"] += soldier.monetary_cost
                        self.national_debt += soldier.monetary_cost

                else:
                    recruits = (self.military['conscript pool'] * 0.11)
                    for i in range(0, int(recruits)):
                        soldier = military.soldier.Soldier(self.name, globe)
                        self.military['military']['Army']['Figures']["Army size"].append(soldier)
                        self.military['military']['Army']['Figures']["Cost"] += soldier.monetary_cost
                        self.national_debt += soldier.monetary_cost

    def check_soldier_deployment(self, globe):
        soldiers = self.military['military']['Army']['Figures']["Army size"][:]
        for soldier in soldiers:
            if globe.date > soldier.retiring_date:
                self.military['military']['Army']['Figures']["Army size"].remove(soldier)

    # objective functions
    def establishing_beginning_objectives(self):
        # Function for establishing state objectives
        # Objectives, whether social, economic, or political, depend on the state's stability

        political_stability = self.national_policy["Policy"][0]["Domestic Policy"][0]["Political"][1]["Political stability"]

        if political_stability >= 90:
            political_objectives = ["maintain political growth", "maintain political stability"]
            economic_objectives = ["promote sustainable growth"]

            for political_objective in political_objectives:
                if political_objective not in self.objectives['objectives'][1]['domestic'][0]['political objectives']:
                    self.objectives['objectives'][1]['domestic'][0]['political objectives'].append(political_objective)

            for economic_objective in economic_objectives:
                if economic_objective not in self.objectives['objectives'][1]['domestic'][0]['economic objectives']:
                    self.objectives['objectives'][1]['domestic'][0]['economic objectives'].append(economic_objective)
        else:
            political_objectives = ["suppress rival factions"]
            economic_objectives = ["promote sustainable growth"]

            for political_objective in political_objectives:
                if political_objective not in self.objectives['objectives'][1]['domestic'][0]['political objectives']:
                    self.objectives['objectives'][1]['domestic'][0]['political objectives'].append(political_objective)

            for economic_objective in economic_objectives:
                if economic_objective not in self.objectives['objectives'][1]['domestic'][0]['economic objectives']:
                    self.objectives['objectives'][1]['domestic'][0]['economic objectives'].append(economic_objective)

        population_objective = ["maintain stable population growth"]

        if ('Fascism' or "Communism") in self.political_typology:
            population_objective = ["maintain large population growth"]

            for pop_objective in population_objective:
                if pop_objective not in self.objectives['objectives'][1]['domestic'][0]['population objectives']:
                    self.objectives['objectives'][1]['domestic'][0]['population objectives'].extend(pop_objective)

        # Use append to add a single string to the list
        self.objectives['objectives'][1]['domestic'][0]['population objectives'].extend(population_objective)

        for pop_objective in population_objective:
            if pop_objective not in self.objectives['objectives'][1]['domestic'][0]['population objectives']:
                self.objectives['objectives'][1]['domestic'][0]['population objectives'].append(pop_objective)

    # international relations functions

    def check_relations_status(self, foreign_nations):
        """checking and updating status of relationship of foreign nations with Nation"""
        for foreign_nation in range(0, len(foreign_nations)):

            # looping through foreign nations list
            for foreign_relation in range(0, len(self.foreign_relations["foreign relations"])):
                if (foreign_nations[foreign_nation].name
                        == self.foreign_relations["foreign relations"][foreign_relation]["nation"].name):
                    """checking to see if a specific name within parameter matches with name
                    in foreign relations list
                    """
                    if self.foreign_relations["foreign relations"][foreign_relation]["relations"] >= 80:
                        """Checking to see if relations with foreign nation are potentially awesome"""
                        self.foreign_relations["foreign relations"][foreign_relation]["relation status"] = "friend"

                    if (self.foreign_relations["foreign relations"][foreign_relation]["relations"] < 80 and
                            self.foreign_relations["foreign relations"][foreign_relation]["relations"] > 40):
                        """Checking to see if relations with foreign nation are potentially rivalrous"""
                        self.foreign_relations["foreign relations"][foreign_relation]["relation status"] = "rival"

                    if (self.foreign_relations["foreign relations"][foreign_relation]["relations"] < 40):
                        """Checking to see if relations with foreign nation are potentially fatal"""
                        self.foreign_relations["foreign relations"][foreign_relation]["relation status"] = "enemy"

    def change_relations(self, foreign_nations):
        pass

    def make_positive_decision(self, foreign_nation, globe, network):
        potential_actions = ["Form alliance", "Increase exports", "Increase imports", "Guarantee independence",
                             "Improve relations"]
        action = potential_actions[random.randrange(0, len(potential_actions))]
        print(self.name, self.improving_relations)

        if action == "Form alliance" and self.political_power >= 60:
            for foreign_relation in range(0, len(self.foreign_relations['foreign relations'])):
                """Looping through country's foreign relations"""
                if foreign_nation.name == self.foreign_relations['foreign relations'][foreign_relation][
                    "nation"].name:
                    """checking if name of foreign relation matches that of foreign nation"""
                    for nation in range(0, len(foreign_nation.foreign_relations['foreign relations'])):
                        """looping through foreign relation's list of foreign relations"""
                        if self.name == foreign_nation.foreign_relations['foreign relations'][nation]['nation'].name:
                            """Checking if name of current nation matches with a specific relation"""
                            if ("" in foreign_nation.foreign_relations['foreign relations'][nation][
                                'alliance'] and "" in
                                    self.foreign_relations['foreign relations'][foreign_relation]["alliance"]):

                                self.foreign_relations['foreign relations'][foreign_relation]["alliance"] = \
                                    f"{self.name}-{foreign_nation.name} alliance"

                                foreign_nation.foreign_relations['foreign relations'][nation]['alliance'] = \
                                    f"{self.name}-{foreign_nation.name} alliance"
                                self.political_power -= 60
                                foreign_nation.political_power -= 60

                                if not network.has_edge(self.name, foreign_nation.name):
                                    network.add_edge(self.name, foreign_nation.name)

                            elif ("" not in foreign_nation.foreign_relations['foreign relations'][nation][
                                'alliance'] and "" in
                                  self.foreign_relations['foreign relations'][foreign_relation]["alliance"]):
                                self.foreign_relations['foreign relations'][foreign_relation]["alliance"] = \
                                    foreign_nation.foreign_relations['foreign relations'][nation]['alliance']
                                self.political_power -= 60

                                if not network.has_edge(self.name, foreign_nation.name):
                                    network.add_edge(self.name, foreign_nation.name)

        elif action == "Increase exports" and self.political_power >= 15:
            self.exports += 25
            foreign_nation.imports += 25
            self.political_power -= 15

        elif action == "Increase imports" and self.political_power >= 15:
            self.imports += 25
            foreign_nation.exports += 25
            self.political_power -= 15

        elif action == "Guarantee independence" and self.political_power >= 50:
            for relations in self.foreign_relations['foreign relations']:
                if relations['nation'].name == foreign_nation.name:
                    if not relations['guaranteeing independence']:
                        relations['guaranteeing independence'] = True
                        self.political_power -= 50
                        self.political_exponent -= 0.25

                        if not network.has_edge(self.name, foreign_nation.name):
                            network.add_edge(self.name, foreign_nation.name)

        elif action == "Improve relations" and self.political_power >= 25:
            if len(self.improving_relations) > 0:
                for nation in self.improving_relations:
                    if foreign_nation.name not in nation['nation name']:

                        if len(self.improving_relations) < 10:
                            if not network.has_edge(self.name, foreign_nation.name):
                                network.add_edge(self.name, foreign_nation.name)
                            self.improving_relations.append({"nation name": foreign_nation.name,
                                                             "duration": globe.date + timedelta(days=20)})
                            self.political_power -= 25
                            self.political_exponent -= 0.15
            else:
                self.improving_relations.append({"nation name": foreign_nation.name,
                                                "duration": globe.date + timedelta(days=20)})

    def make_negative_decision(self, foreign_nation, globe, network):
        potential_actions = ["incursion into sphere of influence", "worsen relations", "embargo",
                             "spark protests"]

        action = potential_actions[random.randrange(0, len(potential_actions))]
        print(self.name, self.worsening_relations)

        if action == "incursion into sphere of influence" and self.political_power >= 50:

            """for relation in range(0, len(foreign_nation.foreign_relations['foreign relations'])):
                if (foreign_nation.foreign_relations['foreign relations'][relation]['relation status'] == "ally" and
                        self.political_typology not in
                        foreign_nation.foreign_relations['foreign relations'][relation]['nation'].political_typology):
                    for nation_search in globe.nations:
                        if nation_search.name == foreign_nation.foreign_relations['foreign relations'][relation][
                            'nation'].name:
                            for foreign_memories in range(0,
                                                          len(nation_search.long_term_memory['Foreign influence'])):
                                if not f"{self.political_typology} Influence" in \
                                       nation_search.long_term_memory['Foreign influence'][foreign_memories]:
                                    nation_search.long_term_memory['Foreign influence'].append({
                                        f"{self.political_typology} Influence": [
                                            {
                                                "Expiration date": globe.date + timedelta(days=30)
                                            }
                                        ]
                                    })
                                    self.political_power -= 50"""
            pass

        elif action == "worsen relations" and self.political_power >= 15:
            chance = random.randrange(1, 40)

            if chance % 6 == 4:
                for worsening in self.worsening_relations:
                    if not foreign_nation.name in worsening['nation name']:
                        if len(self.worsening_relations) < 10:
                            network.add_edge(self.name, foreign_nation.name)

                        self.worsening_relations.append({
                            "nation name": foreign_nation.name,
                            "duration": globe.date + timedelta(days=20)
                        })
                        self.political_power -= 15
                        self.political_exponent -= 0.15


        """elif action == "spark protests" and self.political_power >= 25:
            chance = random.randrange(1, 40)
            if chance % 6 == 4:
                if "Democratic" in self.political_typology:
                    foreign_nation.political_decision({
                        "Issue": "Democratic protest"
                    }, globe)

                if "Fascist" in self.political_typology:
                    foreign_nation.political_decision({
                        "Issue": "Fascist protest"
                    }, globe)

                if "Communist" in self.political_typology:
                    foreign_nation.political_decision({
                        "Issue": "Communist protest"
                    }, globe)

                if "Autocratic" in self.political_typology:
                    foreign_nation.political_decision({
                        "Issue": "Autocratic protest"
                    }, globe)
                self.political_power -= 25"""

    def determine_diplomatic_approach(self, globe, network, user_nation):
        self.make_international_decision(globe, network, user_nation)

    def make_international_decision(self, globe, network, user_nation):
        for foreign_nation in globe.nations:
            if self.name == foreign_nation.name or user_nation.name == foreign_nation.name:
                continue

            else:
                if (f"Challenge {foreign_nation.name}" or
                        f"Contain {foreign_nation.name}" in self.objectives["objectives"][0]['foreign']):
                    self.make_negative_decision(foreign_nation, globe, network)

                if (f"Establish ties with {foreign_nation.name}" or f"Improve relations with {foreign_nation.name}" in
                        self.objectives["objectives"][0]['foreign']):

                    self.make_positive_decision(foreign_nation, globe, network)

    # population functions

    def handle_insignificant_growth(self, globe):
        if len(self.long_term_memory[0]['Domestic Decisions']['Population']) > 0:
            insignificant_found = False
            # search variable for finding insignificant growth within long term memory
            for decision in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'])):
                if self.long_term_memory[0]['Domestic Decisions']['Population'][decision][
                    "Issue"] == "Insignificant population growth":
                    self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"].append(globe.date)
                    insignificant_found = True
                    # setting insignificant growth found to true if ig found

            if not insignificant_found:
                # if not found add to memory
                self.long_term_memory[0]['Domestic Decisions']['Population'].append({
                    "Issue": "Insignificant population growth",
                    "Date": [globe.date],
                    "Action taken": []
                })

            if self.political_typology == "Democratic" or self.political_typology == "Autocratic":
                sum = 0
                for decision in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'])):
                    if (len(self.long_term_memory[0]['Domestic Decisions']['Population'][decision]['Date']) > 1 and
                            self.long_term_memory[0]['Domestic Decisions']['Population'][decision][
                                "Issue"] == "Insignificant population growth"):

                        for date in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"])):
                            if date >= 1:
                                if self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"][date] == (
                                        self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"][
                                            date - 1] + timedelta(days=30)
                                ):
                                    sum += 1
                                    if 4 < sum <= 10:
                                        self.objectives['objectives'][0]['domestic'][0]['population objectives'].clear()
                                        if self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][
                                            'Birth Control']:
                                            self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][

                                                'Birth Control'] = False

                                    else:
                                        self.objectives['objectives'][0]['domestic'][0]['population objectives'].append(
                                            "Maintain high population growth")
                                        self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][
                                            'Birth Enhancer'] = True

            else:
                sum = 0
                for decision in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'])):
                    if (len(self.long_term_memory[0]['Domestic Decisions']['Population'][decision]['Date']) > 1 and
                            self.long_term_memory[0]['Domestic Decisions']['Population'][decision][
                                "Issue"] == "Insignificant population growth"):

                        for date in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"])):
                            if date >= 1:
                                if self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"][date] == (
                                        self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"][
                                            date - 1] + timedelta(days=30)
                                ):

                                    sum += 1
                                    if 2 < sum <= 6:
                                        self.objectives['objectives'][0]['domestic'][0]['population objectives'].clear()
                                        if self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][
                                            'Birth Control']:
                                            self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][
                                                'Birth Control'] = False

                                    else:
                                        self.objectives['objectives'][0]['domestic'][0]['population objectives'].append(
                                            "Maintain high population growth")
                                        self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][
                                            'Birth Enhancer'] = True

        else:
            self.long_term_memory[0]['Domestic Decisions']['Population'].append({
                "Issue": "Insignificant population growth",
                "Date": [globe.date],
                "Action taken": []
            })

    def handle_extreme_growth(self, globe):
        if len(self.long_term_memory[0]['Domestic Decisions']['Population']) > 0:
            extreme_found = False
            # search variable for finding extreme growth within long term memory
            for decision in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'])):
                if self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Issue"] == "Extreme population growth":
                    self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"].append(globe.date)
                    extreme_found = True
                    # setting extreme_found to true if extreme pop growth found

            if not extreme_found:
                # if not found add to memory
                self.long_term_memory[0]['Domestic Decisions']['Population'].append({
                    "Issue": "Extreme population growth",
                    "Date": [globe.date],
                    "Action taken": []
                })

            if self.political_typology == "Democratic" or self.political_typology == "Autocratic":
                sum = 0
                for decision in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'])):
                    if (len(self.long_term_memory[0]['Domestic Decisions']['Population'][decision]['Date']) > 1 and
                            self.long_term_memory[0]['Domestic Decisions']['Population'][decision][
                                "Issue"] == "Extreme population growth"):
                        for date in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"])):
                            if date >= 1:
                                # checking if number is greater or equal to one, to prevent out of bounds
                                if self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"][date] == (
                                        self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"][
                                            date - 1] + timedelta(days=30)
                                ):
                                    sum += 1
                                    if 2 < sum <= 5:
                                        self.objectives['objectives'][0]['domestic'][0]['population objectives'].clear()
                                        if self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][
                                            'Birth Enhancer']:
                                            self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][
                                                'Birth Enhancer'] = False

                                    else:
                                        self.objectives['objectives'][0]['domestic'][0]['population objectives'].append(
                                            "Maintain low population growth")
                                        self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][
                                            'Birth Control'] = True

                                else:
                                    sum = 0
            else:
                # else statement for fascism and communism
                sum = 0
                for decision in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'])):
                    if (len(self.long_term_memory[0]['Domestic Decisions']['Population'][decision]['Date']) > 1 and
                            self.long_term_memory[0]['Domestic Decisions']['Population'][decision][
                                "Issue"] == "Extreme population growth"):
                        for date in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"])):
                            if date >= 1:
                                if self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"][date] == (
                                        self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"][
                                            date - 1] + timedelta(days=30)
                                ):
                                    sum += 1
                                    if 3 < sum <= 9:
                                        self.objectives['objectives'][0]['domestic'][0]['population objectives'].clear()
                                        if self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][
                                            'Birth Enhancer']:
                                            self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][
                                                'Birth Enhancer'] = False

                                    else:
                                        self.objectives['objectives'][0]['domestic'][0]['population objectives'].append(
                                            "reduce population growth")
                                        self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][
                                            'Birth Control'] = True

                                else:
                                    sum = 0

        else:
            self.long_term_memory[0]['Domestic Decisions']['Population'].append({
                "Issue": "Extreme population growth",
                "Date": [globe.date],
                "Action taken": []
            })

    def handle_stable_growth(self, globe):
        if len(self.long_term_memory[0]['Domestic Decisions']['Population']) > 0:
            stable_found = False
            # search variable for finding stable growth within long term memory
            for decision in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'])):
                # searching through previous population decisions
                if self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Issue"] == "stable population growth":
                    self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"].append(globe.date)
                    stable_found = True
                    # setting stable_found to true if stable population found

            if not stable_found:
                # if not found add to memory
                self.long_term_memory[0]['Domestic Decisions']['Population'].append({
                    "Issue": "Stable population growth",
                    "Date": [globe.date],
                    "Action taken": []
                })

            if self.political_typology == "Democratic" or self.political_typology == "Autocratic":
                pass

            else:
                # else statement designed for communist and fascist ideologies
                sum = 0
                for decision in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'])):
                    if (len(self.long_term_memory[0]['Domestic Decisions']['Population'][decision]['Date']) > 1 and
                            self.long_term_memory[0]['Domestic Decisions']['Population'][decision][
                                "Issue"] == "Stable population growth"):
                        for date in range(0, len(self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"])):
                            if date >= 1:
                                if self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"][date] == (
                                        self.long_term_memory[0]['Domestic Decisions']['Population'][decision]["Date"][
                                            date - 1] + timedelta(days=30)
                                ):
                                    sum += 1
                                    if sum >= 9:
                                        self.national_policy['Policy'][0]['Domestic Policy'][0]["Population"][0][
                                            'Birth Enhancer'] = True
                                else:
                                    sum = 0

        else:
            self.long_term_memory[0]['Domestic Decisions']['Population'].append({
                "Issue": "Stable population growth",
                "Date": [globe.date],
                "Action taken": []
            })

    def determine_population_decision(self, domestic_issue, globe):
        if domestic_issue == "extreme growth":
            self.handle_extreme_growth(globe)

        elif domestic_issue == "stable growth":
            self.handle_stable_growth(globe)

        elif domestic_issue == "insignificant growth":
            self.handle_insignificant_growth(globe)

    def check_population_growth(self, globe):
        if self.year_placeholder < self.date.year:
            """checking to see if an entire year has passed"""
            population_calculation = ((self.population - self.past_population) /
                                      ((self.population + self.past_population) / 2)) * 100

            if population_calculation <= 1.5:
                self.determine_population_decision("Insignificant growth", globe)

            elif population_calculation >= 7.6:
                self.determine_population_decision("Extreme growth", globe)

            else:
                self.determine_population_decision("Stable growth", globe)

        else:
            self.pop_growth()

    def pop_growth(self):
        if self.national_policy["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Enhancer"]:
            births = random.randrange(0, 30)
            deaths = random.randrange(0, 20)
            self.population += (births - deaths)
            self.births += births
            self.deaths += deaths

        if self.national_policy["Policy"][0]["Domestic Policy"][0]["Population"][0]["Birth Control"]:
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

        for objective in self.objectives['objectives'][1]['domestic'][0]['population objectives']:
            if objective == "Maintain low population growth":
                chance = random.randrange(3, 140)
                if chance % 10 == 6 or chance % 15 == 2:
                    killings = self.population * 0.001
                    self.population -= killings
                    self.deaths += killings

    # political functions

    def handle_protest(self, political_issue, globe):
        days = random.randrange(10, 30)
        if len(self.long_term_memory[0]["Domestic problems"][0]["Protests"]) > 0:
            issue_found = False
            for memory in self.long_term_memory[0]["Domestic problems"][0]["Protests"]:
                if memory['Protest ideology'] == political_issue:
                    memory['Duration'] += timedelta(days=days)
                    issue_found = True

            if not issue_found:
                self.long_term_memory[0]["Domestic problems"][0]["Protests"].append(
                    {"Protest ideology": f"{political_issue}",
                     "Date": globe.date,
                     "Duration": globe.date + timedelta(days=days),
                     "Influence": round(random.uniform(0.01, 0.10), 2)}
                )

        else:
            self.long_term_memory[0]["Domestic problems"][0]["Protests"].append(
                {"Protest ideology": f"{political_issue}",
                 "Date": globe.date,
                 "Duration": globe.date + timedelta(days=days),
                 "Influence": round(random.uniform(0.01, 0.10), 2)}
            )

        self.updating_ideology(globe)
        self.instill_ideological_growth()

    def political_decision(self, political_issue, globe):
        self.handle_protest(political_issue, globe)

    def updating_ideology(self, globe):
        ideologies = ['Democratic protest', "Fascist protest", "Communist protest", "Autocratic protest"]
        for protest in self.long_term_memory[0]["Domestic problems"][0]["Protests"]:
            # looping through protest dictionaries within long term memory
            for ideology in ideologies:
                if ideology == protest['Protest ideology']:
                    if "Democratic" in ideology:
                        self.long_term_memory[0]['Domestic Ideologies']['Democratic'] += (
                            protest["Influence"])

                    elif "Communist" in ideology:
                        self.long_term_memory[0]['Domestic Ideologies']['Communist'] += (
                            protest["Influence"])

                    elif "Fascist" in ideology:
                        self.long_term_memory[0]['Domestic Ideologies']['Fascist'] += (
                            protest["Influence"])

                    elif "Autocratic" in ideology:
                        self.long_term_memory[0]['Domestic Ideologies']['Autocratic'] += (
                            protest["Influence"])

        # Create a copy of the list to iterate over
        protests = self.long_term_memory[0]["Domestic problems"][0]["Protests"][:]
        # Iterate through the copy and remove items from the original list
        for memory in protests:
            if memory['Duration'] < globe.date:
                self.long_term_memory[0]["Domestic problems"][0]["Protests"].remove(memory)
        self.instill_ideological_growth()

    def instill_ideological_growth(self):
        # function developed to aid in increasing influence of current ideology
        if self.political_typology == "Democratic" and self.long_term_memory[0]['Domestic Ideologies']["Democratic"] <= 50:
            self.long_term_memory[0]['Domestic Ideologies']["Democratic"] += round(random.uniform(0.03, 0.10), 2)

        if self.political_typology == "Communist" and self.long_term_memory[0]['Domestic Ideologies']["Communist"] <= 50:
            self.long_term_memory[0]['Domestic Ideologies']["Communist"] += round(random.uniform(0.03, 0.10), 2)

        if self.political_typology == "Fascist" and self.long_term_memory[0]['Domestic Ideologies']["Fascist"] <= 50:
            self.long_term_memory[0]['Domestic Ideologies']["Fascist"] += round(random.uniform(0.03, 0.10), 2)

        if self.political_typology == "Autocratic" and self.long_term_memory[0]['Domestic Ideologies']["Autocratic"] <= 50:
            self.long_term_memory[0]['Domestic Ideologies']["Autocratic"] += round(random.uniform(0.03, 0.10), 2)

    def protests(self, globe):
        """Protests will only occur if political stability drops below 75% or economic stability drops below 65%"""
        if (self.national_policy["Policy"][0]["Domestic Policy"][0]["Political"][1]["Political stability"] >= 75.00 or
                self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Economic stability"] >= 65.00):
            """protests occurring in relative peaceful and stable times"""
            number = random.randrange(1, 101)
            if number % 9 == 5 or number % 6 == 4:
                """chance, based upon remainder of 0 or 4 that fascist protest will occur with relative stability"""

                self.political_decision("Fascist protest", globe)

            if number % 3 == 2 or number % 7 == 5:
                """chance, based upon remainder of 1 or 2 that liberal protest will occur with relative stability"""

                self.political_decision("Democratic protest", globe)

            if number % 7 == 6 or number % 9 == 7:
                """chance, based upon remainder of 5 or 7 that liberal protest will occur with relative stability"""

                self.political_decision("Communist protest", globe)

            if number % 10 == 2 or number % 12 == 7:
                """chance, based upon remainder of 6 or 8 that liberal protest will occur with relative stability"""

                self.political_decision("Autocratic protest", globe)

        if (self.national_policy["Policy"][0]["Domestic Policy"][0]["Political"][1]["Political stability"] < 75.00 or
                self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Economic stability"] < 65.00):
            """protests occurring in relative non-peaceful times"""
            number = random.randrange(1, 101)
            if number % 2 == 1 or number % 3 == 2:
                """chance, based upon remainder of 0 or 4 that fascist protest will occur with relative stability"""

                self.political_decision("Fascist protest", globe)

            if number % 3 == 1 or number % 4 == 0:
                """chance, based upon remainder of 1 or 2 that liberal protest will occur with relative stability"""

                self.political_decision("Democratic protest", globe)

            if number % 4 == 3 or number % 5 == 4:
                """chance, based upon remainder of 5 or 7 that liberal protest will occur with relative stability"""

                self.political_decision("Communist protest", globe)

            if number % 6 == 2 or number % 7 == 3:
                """chance, based upon remainder of 6 or 8 that liberal protest will occur with relative stability"""

                self.political_decision("Autocratic protest", globe)

    def political_power_growth(self):
        self.political_power += self.political_exponent

    # economic functions
    def handle_depression(self, depress_sum):
        if depress_sum >= 4:
            actions = ['Decrease Corporate Taxes', "Decrease Income Taxes", "Increase Exports", "Decrease Imports"]
            action = actions[random.randrange(0, len(actions))]
            if action == 'Decrease Corporate Taxes':
                self.investment += 35

            elif action == "Decrease Income Taxes":
                self.consumer_spending += 25

            elif action == "Increase Exports":
                self.exports += 100

            elif action == "Decrease Imports":
                self.imports -= 10

    def handle_negative_growth(self, issue, globe):
        recess_sum = 0
        depress_sum = 0
        recess_found = False
        # variable designed for finding recoveries in decisions
        depress_found = False
        # variable designed for finding expansions in decisions
        if len(self.long_term_memory[0]["Domestic Decisions"]['Economic']) > 0:
            for decision in self.long_term_memory[0]["Domestic Decisions"]['Economic']:
                if decision['Issue'] == "Recession" and issue == "Recession":
                    recess_found = True
                    for date in range(0, len(decision['Date'])):
                        if date >= 1 and (decision['Date'][date - 1] + timedelta(days=120)) == decision['Date'][date]:
                            recess_sum += 1
                            if 3 <= recess_sum < 6 and not self.e_s == EconomicState.RECESSION:
                                self.e_s = EconomicState.RECESSION

                            elif recess_sum >= 6:
                                self.e_s = EconomicState.DEPRESSION
                        else:
                            recess_sum = 0

                elif decision['Issue'] == "Depression" and issue == "Depression":
                    recess_found = True
                    for date in range(0, len(decision['Date'])):
                        if date >= 1 and (decision['Date'][date - 1] + timedelta(days=120)) == decision['Date'][date]:
                            depress_sum += 1
                            self.handle_depression(depress_sum)

                        else:
                            depress_sum = 0

            if not recess_found and issue == "Recession":
                self.long_term_memory[0]["Domestic Decisions"]['Economic'].append({
                    "Issue": issue,
                    "Date": [globe.date]
                })

            if not depress_found and issue == "Depression":
                self.long_term_memory[0]["Domestic Decisions"]['Economic'].append({
                    "Issue": issue,
                    "Date": [globe.date]
                })
        else:
            self.long_term_memory[0]['Domestic Decisions']['Economic'].append({
                "Issue": issue,
                "Date": [globe.date]
            })

    def handle_expansion(self, expan_sum):
        if expan_sum >= 4:
            actions = ['Increase taxes', "Decrease government spending", "increase corporate taxes"]
            action = actions[random.randrange(0, len(actions))]
            if action == "Increase taxes":
                self.consumer_spending -= 25

            elif action == "Decrease government spending":
                self.government_spending -= 35

            elif action == "increase corporate taxes":
                self.investment -= 45

    def handle_positive_growth(self, issue, globe):
        recov_sum = 0
        expan_sum = 0
        recov_found = False
        # variable designed for finding recoveries in decisions
        expan_found = False
        # variable designed for finding expansions in decisions
        if len(self.long_term_memory[0]["Domestic Decisions"]['Economic']) > 0:
            # checking length of domestic economic decisions
            for decision in self.long_term_memory[0]["Domestic Decisions"]['Economic']:
                if decision['Issue'] == "Recovery" and issue == "Recovery":
                    recov_found = True
                    for date in range(0, len(decision['Date'])):
                        if date >= 1 and (decision['Date'][date - 1] + timedelta(days=120)) == decision['Date'][date]:
                            recov_sum += 1

                            if 3 < recov_sum < 6 and not self.e_s == EconomicState.RECOVERY:
                                self.e_s = EconomicState.RECOVERY

                            elif recov_sum == 6:
                                self.e_s = EconomicState.EXPANSION

                        else:
                            recov_sum = 0

                if decision['Issue'] == "Expansion" and issue == "Expansion":
                    expan_found = True
                    for date in range(0, len(decision['Date'])):
                        if date >= 1 and (decision['Date'][date - 1] + timedelta(days=120)) == decision['Date'][date]:
                            expan_sum += 1
                            self.handle_expansion(expan_sum)

                        else:
                            expan_sum = 0

            if not recov_found and issue == "Recovery":
                self.long_term_memory[0]["Domestic Decisions"]['Economic'].append({
                    "Issue": issue,
                    "Date": [globe.date]
                })

            if not expan_found and issue == "Expansion":
                self.long_term_memory[0]["Domestic Decisions"]['Economic'].append({
                    "Issue": issue,
                    "Date": [globe.date]
                })

        else:
            self.long_term_memory[0]["Domestic Decisions"]['Economic'].append({
                "Issue": issue,
                "Date": [globe.date]
            })

    def check_economic_growth(self, globe):
        if globe.date > self.economic_change_date:
            growth = ((self.current_gdp - self.past_gdp) / (self.current_gdp + self.past_gdp) / 2) * 100
            if growth <= 1.95:
                if self.e_s == EconomicState.RECESSION:
                    self.handle_positive_growth("Recession", globe)

                if self.e_s == EconomicState.DEPRESSION:
                    self.handle_positive_growth("Depression", globe)

            elif growth >= 6.95:
                if self.e_s == EconomicState.RECOVERY:
                    self.handle_positive_growth("Recovery", globe)

                if self.e_s == EconomicState.EXPANSION:
                    self.handle_positive_growth("Expansion", globe)
            self.check_economic_growth(globe)
            self.check_national_debt()

        else:
            self.check_economic_state(globe)
            self.check_national_debt()

    def check_national_debt(self):
        debt_gdp_ratio = (self.national_debt / self.current_gdp) * 100
        # calculation of total debt to total current gdp ratio
        if debt_gdp_ratio <= 55.00:
            self.national_policy["Policy"][0]["National Policy"][0]["Economy"][1]["Economic stability"] -= 0.5

        if debt_gdp_ratio <= 65.50:
            # if ratio becomes excessive, AI has chance to pay off its debt in one fell swoop
            chance = random.randrange(2, 140)
            if chance % 5 == 4 or chance % 10 == 6:
                self.current_gdp -= self.national_debt
                self.national_debt = 0
        self.paying_national_debt()

    def paying_national_debt(self):
        # function developed for nations to pay off their internal debt
        debt_payment = (self.national_debt *
                        (self.national_policy['Policy']
                         [0]['Domestic Policy'][1]['Economy'][0]['debt interest payment rate'] / 100))

        self.national_debt -= debt_payment

    def check_economic_state(self, globe):
        """function dealing with primary economic decisions"""

        if self.e_s == EconomicState.RECESSION or self.e_s == EconomicState.DEPRESSION:
            self.investment -= 12.5
            self.consumer_spending -= 25
            self.government_spending += 35
            self.exports -= 15
            self.imports += 25
            if not self.national_policy['Policy'][0]["Domestic Policy"][0]["Economy"][1]['Improving ES']:
                self.national_policy["Policy"][0]["National Policy"][0]["Economy"][1]["Economic stability"] -= 1.5

            else:
                self.national_policy["Policy"][0]["National Policy"][0]["Economy"][1]["Economic stability"] += 0.5
            if self.national_policy["Policy"][0]["National Policy"][0]["Economy"][1]["Economic stability"] <= 65:
                self.handle_other_economic_problems("Low economic stability")
            self.neg_ec_growth()

        elif self.e_s == EconomicState.RECOVERY or self.e_s == EconomicState.EXPANSION:
            self.investment += 15
            self.consumer_spending += 25
            self.exports += 15
            # specific components of GDP are incremented each cycle if e_s is recovery or expansion
            if ((self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Economic stability"] + 1.5) < 100):
                """Checking to see if adding of 1.5 to economic stability will exceed 100 or not"""
                self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Economic stability"] += 1.5

            if (self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Economic stability"] >= 85 and
                self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Improving ES"]):
                self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Improving ES"] = False
            self.pos_ec_growth()

    def pos_ec_growth(self):
        self.national_debt += round(
            (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)

        self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                             (self.exports - self.imports))

    def neg_ec_growth(self):
        if self.consumer_spending > 0:
            self.national_debt += round(
                (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        else:
            self.national_debt += round(self.government_spending * round(random.uniform(0.15, 0.35), 4), 2)

        self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                             (self.exports - self.imports))

    def handle_low_es(self):
        chance = random.randrange(4, 200)
        if (chance % 5 == 4 or chance % 20 == 3) and not (self.national_policy['Policy'][0]['Domestic Policy']
        [1]['Economy'][1]['Improving ES']):
            self.national_policy['Policy'][0]['Domestic Policy'][1]['Economy'][1]['Improving ES'] = True

    def handle_other_economic_problems(self, issue):
        if issue == "Low economic stability":
            self.handle_low_es()

    # stability functions

    def check_stability(self):
        chance = random.randrange(10, 200)
        if self.political_typology == "Communism" or self.political_typology == "Fascist" or self.political_typology == "Autocratic":
            if self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Political stability'] <= 80:
                if chance % 3 == 1 or chance % 6 == 2:
                    if not self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Improving PS']:
                        self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Improving PS'] = True
        else:
            if self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Political stability'] <= 60:
                if chance % 9 == 5 or chance % 15 == 6:
                    if not self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Improving PS']:
                        self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Improving PS'] = True

        if 90 <= self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Political stability'] <= 100:
            self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Improving PS'] = False

    def stability_change(self):
        if self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Political stability'] <= 50:
            if self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Improving PS']:
                if (self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Political stability'] + 0.25) < 100:
                    self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Political stability'] += 0.25
            else:
                self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Political stability'] -= 2.5

        else:
            if self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Improving PS']:
                if (self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Political stability'] + 4.25) < 100:
                    self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Political stability'] += 4.25
            else:
                if (self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Political stability'] + 2.25) < 100:
                    self.national_policy['Policy'][0]['Domestic Policy'][0]['Political'][1]['Political stability'] += 2.25

    def main(self, globe, network, user_nation):
        while self.population > 250000:
            self.check_population_growth(globe)
            self.political_power_growth()
            #self.stability_change()
            if globe.date > self.date_checker:
                self.determine_diplomatic_approach(globe, network, user_nation)
                self.date_checker = globe.date + timedelta(days=3)
            self.change_relations(globe.nations)
            chance = random.randrange(1, 50)
            if chance % 8 == 2 or chance % 5 == 4:
                self.protests(globe)
            self.pop_growth()
            self.check_economic_state(globe)
            self.adding_conscription_pool(globe)
            break