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
        # social factors
        """population factors"""
        self.population = 1000000
        self.past_population = self.population
        self.birth_control = False
        self.birth_enhancer = False
        self.births = 0
        self.deaths = 0
        self.happiness = 98.56
        # political
        self.leader = "Gregory Prescov"
        self.alliance = ""
        self.political_typology = "Republicanism"
        self.democratic_appeal = 75
        self.communist_appeal = 15
        self.fascist_appeal = 7
        self.autocratic_appeal = 3
        self.political_power = 100
        self.political_exponent = 1.00
        """Stability"""
        self.stability = 95.56
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
        self.chosen = False
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
                    {"Happiness": 78.56}
                    # growth occurrences will be growth that is consistent, once change happens set back to 0
                ],
                "Economy": [
                    {"tax rate": 15.00,
                     "government stimulus": False,
                     "low growth occurrences": 0,
                     "high growth occurrences": 0},
                    {"Economic stability": 87.56}
                ],
                "Political": [
                    {"Repress Far-Left": False,
                     "Repress Far-Right": False,
                     "Repress Autocrats": False,
                     "Repress Liberals": False,
                     "Suppress Far-Left": False,
                     "Supress Far-Right": False,
                     "Suppress Autocrats": False,
                     "Suppress Liberals": False},
                    {"Far-Right protests": [],
                     "Far-Left protests": [],
                     "Autocrat protests": [],
                     "Liberal protests": []},
                    {"Political stability": 90.0}
                    # for political rewards to be utilized, AI must make political decision
                    # for example if there is a far left protest and the AI handles the protest by killing everyone...
                    # then political rewards would be decreased and the action and the outcome of the action would be stored in long term
                    # memory
                ]
            }],
                "Foreign Policy": [{
                    "Allies": [],
                    "Rivals": [],
                    "Enemies": [],
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

        self.long_term_memory = {
            "Domestic decisions":
                [
                {"Economic Decisions": [],
                 "Political Decisions": [],
                 "Social Decisions": [],
                 "Population Decisions": []}
            ],
            "Foreign decisions": [
                {"allies": []},
                {"rivals": []},
                {"enemies": []},
            ],
            "Foreign influence": []
        }
        # long term memory stores decisions made by the AI. Used by the AI as game advances, to aid in policymaking

    def establishing_beginning_objectives(self):
        # Function for establishing state objectives
        # Objectives, whether social, economic, or political, depend on the state's stability

        political_stability = self.national_policy["Policy"][0]["Domestic Policy"][0]["Political"][2]["Political stability"]
        economic_stability = self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Economic stability"]
        political_objectives = []
        economic_objectives = []

        if political_stability >= 90:
            political_objectives = ["suppress rival factions", "maintain political growth"]
            economic_objectives = ["promote sustainable growth"]

            for political_objective in political_objectives:
                if political_objective not in self.objectives['objectives'][1]['domestic'][0]['political objectives']:
                    self.objectives['objectives'][1]['domestic'][0]['political objectives'].append(political_objective)

            for economic_objective in economic_objectives:
                if economic_objective not in self.objectives['objectives'][1]['domestic'][0]['economic objectives']:
                    self.objectives['objectives'][1]['domestic'][0]['economic objectives'].append(economic_objective)

        population_objective = ["maintain stable population growth"]

        if 'Fascism' in self.political_typology or "Communism" in self.political_typology:
            population_objective = ["maintain large population growth"]

            for pop_objective in population_objective:
                if pop_objective not in self.objectives['objectives'][1]['domestic'][0]['population objectives']:
                    self.objectives['objectives'][1]['domestic'][0]['population objectives'].extend(pop_objective)

        # Use append to add a single string to the list
        self.objectives['objectives'][1]['domestic'][0]['population objectives'].extend(population_objective)

        for pop_objective in population_objective:
            if pop_objective not in self.objectives['objectives'][1]['domestic'][0]['population objectives']:
                self.objectives['objectives'][1]['domestic'][0]['population objectives'].append(pop_objective)
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
                        self.foreign_relations["foreign relations"][foreign_relation]["relation status"] = "friend"

                    if (self.foreign_relations["foreign relations"][foreign_relation]["relations"] < 80 and
                            self.foreign_relations["foreign relations"][foreign_relation]["relations"] > 40):
                        """Checking to see if relations with foreign nation are potentially rivalrous"""
                        self.foreign_relations["foreign relations"][foreign_relation]["relation status"] = "rival"

                    if (self.foreign_relations["foreign relations"][foreign_relation]["relations"] < 40):
                        """Checking to see if relations with foreign nation are potentially fatal"""
                        self.foreign_relations["foreign relations"][foreign_relation]["relation status"] = "enemy"

    def change_relations(self, foreign_nations):
        for relation in self.improving_relations:
            """looping through nations that nation is currently improving relations with"""
            for nation in self.foreign_relations['foreign relations'][0]['nation_name']:
                """looping through nations in foreign relations book of nation"""
                if nation == relation:
                    """checking if nation in book matches with nation that current nation is improving relations with"""
                    if (self.foreign_relations['foreign relations'][0]["relations"] + 1.5) < 100:
                        self.foreign_relations['foreign relations'][0]["relations"] += 1.5

                    else:
                        self.political_exponent += 0.25
                        for i in range(0, len(self.objectives['objectives'][1]['foreign'])):
                            if (f"improve relations with {nation}") in self.objectives['objectives'][1]['foreign'][i]:
                                self.objectives['objectives'][1]['foreign'].pop(
                                    self.objectives['objectives'][1]['foreign'][i])
                                self.objectives['objectives'][1]['foreign'].append(
                                    f"create alliance with {self.foreign_relations['foreign relations'][0]['nation_name']}")

        for relation in self.worsening_relations:
            """looping through nations that nation is currently worsening relations with"""
            for nation in self.foreign_relations['foreign relations'][0]['nation_name']:
                """looping through nations in foreign relations book of nation"""
                if nation == relation:
                    """checking if nation in book matches with nation that current nation is worsening relations with"""
                    if (self.foreign_relations['foreign relations'][0]["relations"] - 1.5) > -100:
                        self.foreign_relations['foreign relations'][0]["relations"] -= 1.5

                        for foreign_nation in foreign_nations:

                            if self.foreign_relations['foreign relations'][0]["relations"] < -25 and (
                                    self.political_typology not in
                                    foreign_nation.political_typology):
                                "poor relations with specific nation that isn't of similar ideology"
                                (self.objectives['objectives'][1]['foreign'].
                                append(
                                    f"develop war goal against {self.foreign_relations['foreign relations'][0]['nation_name']}"))

                            else:
                                (self.objectives['objectives'][1]['foreign'].
                                append(
                                    f"Improve relations with {self.foreign_relations['foreign relations'][0]['nation_name']}"))

        for nation in foreign_nations:
            for relations in range(0, len(nation.foreign_relations['foreign relations'])):
                if (self.name == nation.foreign_relations['foreign relations'][relations]['nation name'] and
                        nation.foreign_relations['foreign relations'][relations]['relations'] <= 45):
                    if f"Improve relations with {nation.name}" not in self.objectives['objectives'][0]['foreign']:
                        self.objectives['objectives'][0]['foreign'].append(f"Improve relations with {nation.name}")

        self.check_relations_status(foreign_nations)

    def determine_diplomatic_approach(self, globe, network, user_nation):
        if "Republicanism" or "Democratic" in self.political_typology:
            self.democratic_international_decision(globe, network, user_nation)

        if "Communism" or "Socialism" in self.political_typology:
            self.communist_international_decision(globe, network, user_nation)

        if "Fascism" or "Nazism" in self.political_typology:
            self.fascist_international_decision(globe, network, user_nation)

        if "Autocratic" or "Absolutism" in self.political_typology:
            self.autocratic_international_decision(globe, network, user_nation)

    def democratic_decisions_enemies(self, globe, network, foreign_nation):
        potential_actions = ["incursion into sphere of influence", "worsen relations", "embargo",
                             "spark democratic protests"]

        action = potential_actions[random.randrange(0, len(potential_actions))]

        if action == "incursion into sphere of influence":
            for allies in range(0, len(foreign_nation.foreign_relations['foreign relations'])):
                # searching through foreign nation's list of foreign relations
                if "ally" or "friend" in foreign_nation.foreign_relations['foreign relations'][allies][
                    'relation status']:

                    for potential_ally in globe.nations:
                        if potential_ally.name == foreign_nation.foreign_relations['foreign relations'][allies][
                            'nation name'] and "Democratic" not in potential_ally.political_typology:
                            # checking if nation name matches with ally name and that ally is not democratic
                            for foreign_memories in potential_ally.long_term_memory["Foreign influence"]:
                                if not "Democratic Influence" in foreign_memories:
                                    potential_ally.long_term_memory["Foreign influence"].append({
                                        "Democratic Influence": [
                                            {
                                                "Expiration date": globe.date + timedelta(days=30)
                                            }
                                        ]
                                    })
                                    self.political_power -= 10
                                    break

        elif action == "worsen relations":
            chance = random.randrange(1, 40)
            if chance % 6 == 4:
                for worsening in self.worsening_relations:
                    if foreign_nation.name in worsening['nation name']:
                        worsening['duration'] += timedelta(days=20)
                        break

                    else:
                        if len(self.worsening_relations) < 10:
                            if not network.has_edge(self.name, foreign_nation.name):
                                network.add_edge(self.name, foreign_nation.name)

                            self.worsening_relations.append({
                                "nation name": foreign_nation.name,
                                "duration": globe.date + timedelta(days=20)
                            })
                            self.political_power -= 10
                            self.political_exponent -= 0.15
                            break

        elif action == "spark democratic protests":
            chance = random.randrange(1, 40)
            if chance % 6 == 4:
                foreign_nation.political_decision({
                    "Issue": "Liberal protest"
                })

    def democratic_decisions_allies(self, globe, network, foreign_nation):
        potential_actions = ["Form alliance", "Increase exports", "Increase imports", "Guarantee independence",
                             "Improve relations"]
        action = potential_actions[random.randrange(0, len(potential_actions))]

        if action == "Form alliance":
            # action generated to form alliance
            for relations in self.foreign_relations['foreign relations']:
                # searching through nation's foreign relations
                if relations['nation name'] == foreign_nation.name:
                    # checking if foreign nation name equal to foreign nation name
                    for nations in foreign_nation.foreign_relations['foreign relations']:
                        # searching through nations in foreign nation's foreign relations
                        if self.name == nations['nation name']:
                            # checking if nation's name is equal to nation in foreign nation's foreign relations
                            if "" not in relations['alliance'] and "" in nations["alliance"]:
                                nations['alliance'] = relations['alliance']

                            elif "" in relations['alliance'] and "" not in nations['alliance']:
                                relations['alliance'] = nations['alliance']

                            else:
                                pass

        elif action == "Increase exports":
            self.exports += 25
            foreign_nation.imports += 25

        elif action == "Increase imports":
            self.imports += 25
            foreign_nation.exports += 25

        elif action == "Guarantee independence":
            for relations in self.foreign_relations['foreign relations']:
                if relations['nation name'] == foreign_nation.name:
                    if not relations['guaranteeing independence']:
                        relations['guaranteeing independence'] = True

                        if not network.has_edge(self.name, foreign_nation.name):
                            network.add_edge(self.name, foreign_nation.name)

        elif action == "Improve relations":
            for nation in self.improving_relations:
                if foreign_nation.name in nation['nation name']:
                    nation['duration'] += timedelta(days=20)

                else:
                    if len(self.improving_relations) < 10:
                        if not network.has_edge(self.name, foreign_nation.name):
                            network.add_edge(self.name, foreign_nation.name)
                            self.improving_relations.append({"nation name": foreign_nation.name,
                                                             "duration": globe.date + timedelta(days=20)})

    def democratic_international_decision(self, globe, network, user_nation):
        for foreign_nation in globe.nations:
            if self.name == foreign_nation.name or user_nation.name == foreign_nation.name:
                continue

            else:
                if self.political_power >= 10:

                    if f"Challenge {foreign_nation.name}" in self.objectives["objectives"][0]['foreign']:
                        self.democratic_decisions_enemies(globe, network, foreign_nation)

                    elif (f"Establish ties with {foreign_nation.name}" or f"Improve relations with {foreign_nation.name}" in
                          self.objectives["objectives"][0]['foreign']):
                        self.democratic_decisions_allies(globe, network, foreign_nation)

    def autocratic_decisions_allies(self, globe, network, foreign_nation):
        potential_actions = ["Form alliance", "Increase exports", "Increase imports", "Guarantee independence",
                             "Improve relations"]
        action = potential_actions[random.randrange(0, len(potential_actions))]

        if action == "Form alliance":
            # action generated to form alliance
            for relations in self.foreign_relations['foreign relations']:
                # searching through nation's foreign relations
                if relations['nation name'] == foreign_nation.name:
                    # checking if foreign nation name equal to foreign nation name
                    for nations in foreign_nation.foreign_relations['foreign relations']:
                        # searching through nations in foreign nation's foreign relations
                        if self.name == nations['nation name']:
                            # checking if nation's name is equal to nation in foreign nation's foreign relations
                            if "" not in relations['alliance'] and "" in nations["alliance"]:
                                nations['alliance'] = relations['alliance']

                            elif "" in relations['alliance'] and "" not in nations['alliance']:
                                relations['alliance'] = nations['alliance']

                            else:
                                pass

        elif action == "Increase exports":
            self.exports += 25
            foreign_nation.imports += 25

        elif action == "Increase imports":
            self.imports += 25
            foreign_nation.exports += 25

        elif action == "Guarantee independence":
            for relations in self.foreign_relations['foreign relations']:
                if relations['nation name'] == foreign_nation.name:
                    if not relations['guaranteeing independence']:
                        relations['guaranteeing independence'] = True

                        if not network.has_edge(self.name, foreign_nation.name):
                            network.add_edge(self.name, foreign_nation.name)

        elif action == "Improve relations":
            for nation in self.improving_relations:
                if foreign_nation.name in nation['nation name']:
                    nation['duration'] += timedelta(days=20)

                else:
                    if len(self.improving_relations) < 10:
                        if not network.has_edge(self.name, foreign_nation.name):
                            network.add_edge(self.name, foreign_nation.name)
                            self.improving_relations.append({"nation name": foreign_nation.name,
                                                             "duration": globe.date + timedelta(days=20)})
    def autocratic_decisions_enemies(self, globe, network, foreign_nation):
        potential_actions = ["incursion into sphere of influence", "worsen relations", "embargo",
                             "spark autocratic protests"]

        action = potential_actions[random.randrange(0, len(potential_actions))]

        if action == "incursion into sphere of influence":
            for allies in range(0, len(foreign_nation.foreign_relations['foreign relations'])):
                # searching through foreign nation's list of foreign relations
                if "ally" or "friend" in foreign_nation.foreign_relations['foreign relations'][allies][
                    'relation status']:

                    for potential_ally in globe.nations:
                        if potential_ally.name == foreign_nation.foreign_relations['foreign relations'][allies][
                            'nation name'] and "Autocratic" not in potential_ally.political_typology:
                            # checking if nation name matches with ally name and that ally is not democratic
                            for foreign_memories in potential_ally.long_term_memory["Foreign influence"]:
                                if not "Autocratic Influence" in foreign_memories:
                                    potential_ally.long_term_memory["Foreign influence"].append({
                                        "Autocratic Influence": [
                                            {
                                                "Expiration date": globe.date + timedelta(days=30)
                                            }
                                        ]
                                    })
                                    self.political_power -= 10
                                    break

        elif action == "worsen relations":
            chance = random.randrange(1, 40)
            if chance % 6 == 4:
                for worsening in self.worsening_relations:
                    if foreign_nation.name in worsening['nation name']:
                        worsening['duration'] += timedelta(days=20)
                        break

                    else:
                        if len(self.worsening_relations) < 10:
                            if not network.has_edge(self.name, foreign_nation.name):
                                network.add_edge(self.name, foreign_nation.name)

                            self.worsening_relations.append({
                                "nation name": foreign_nation.name,
                                "duration": globe.date + timedelta(days=20)
                            })

                            self.political_power -= 10
                            self.political_exponent -= 0.15
                            break

        elif action == "spark autocratic protests":
            chance = random.randrange(1, 40)
            if chance % 6 == 4:
                foreign_nation.political_decision({
                    "Issue": "Autocratic protest"
                })

    def autocratic_international_decision(self, globe, network, user_nation):
        for foreign_nation in globe.nations:
            if self.name == foreign_nation.name or user_nation.name == foreign_nation.name:
                continue

            else:
                if self.political_power >= 10:

                    if f"Challenge {foreign_nation.name}" in self.objectives["objectives"][0]['foreign']:
                        self.autocratic_decisions_enemies(globe, network, foreign_nation)

                    elif (f"Establish ties with {foreign_nation.name}" or f"Improve relations with {foreign_nation.name}" in
                          self.objectives["objectives"][0]['foreign']):
                        self.autocratic_decisions_allies(globe, network, foreign_nation)

    def fascist_decisions_allies(self, globe, network, foreign_nation):
        potential_actions = ["Form alliance", "Increase exports", "Increase imports", "Guarantee independence",
                             "Improve relations"]
        action = potential_actions[random.randrange(0, len(potential_actions))]

        if action == "Form alliance":
            # action generated to form alliance
            for relations in self.foreign_relations['foreign relations']:
                # searching through nation's foreign relations
                if relations['nation name'] == foreign_nation.name:
                    # checking if foreign nation name equal to foreign nation name
                    for nations in foreign_nation.foreign_relations['foreign relations']:
                        # searching through nations in foreign nation's foreign relations
                        if self.name == nations['nation name']:
                            # checking if nation's name is equal to nation in foreign nation's foreign relations
                            if "" not in relations['alliance'] and "" in nations["alliance"]:
                                nations['alliance'] = relations['alliance']

                            elif "" in relations['alliance'] and "" not in nations['alliance']:
                                relations['alliance'] = nations['alliance']

                            else:
                                pass

        elif action == "Increase exports":
            self.exports += 25
            foreign_nation.imports += 25

        elif action == "Increase imports":
            self.imports += 25
            foreign_nation.exports += 25

        elif action == "Guarantee independence":
            for relations in self.foreign_relations['foreign relations']:
                if relations['nation name'] == foreign_nation.name:
                    if not relations['guaranteeing independence']:
                        relations['guaranteeing independence'] = True

                        if not network.has_edge(self.name, foreign_nation.name):
                            network.add_edge(self.name, foreign_nation.name)

        elif action == "Improve relations":
            for nation in self.improving_relations:
                if foreign_nation.name in nation['nation name']:
                    nation['duration'] += timedelta(days=20)

                else:
                    if len(self.improving_relations) < 10:
                        if not network.has_edge(self.name, foreign_nation.name):
                            network.add_edge(self.name, foreign_nation.name)
                            self.improving_relations.append({"nation name": foreign_nation.name,
                                                             "duration": globe.date + timedelta(days=20)})

    def fascist_decisions_enemies(self, globe, network, foreign_nation):
        potential_actions = ["incursion into sphere of influence", "worsen relations", "embargo",
                             "spark fascist protests"]

        action = potential_actions[random.randrange(0, len(potential_actions))]

        if action == "incursion into sphere of influence":
            for allies in range(0, len(foreign_nation.foreign_relations['foreign relations'])):
                # searching through foreign nation's list of foreign relations
                if "ally" or "friend" in foreign_nation.foreign_relations['foreign relations'][allies][
                    'relation status']:

                    for potential_ally in globe.nations:
                        if potential_ally.name == foreign_nation.foreign_relations['foreign relations'][allies][
                            'nation name'] and "Fascism" not in potential_ally.political_typology:
                            # checking if nation name matches with ally name and that ally is not democratic
                            for foreign_memories in potential_ally.long_term_memory["Foreign influence"]:
                                if not "Far right Influence" in foreign_memories:
                                    potential_ally.long_term_memory["Foreign influence"].append({
                                        "Far right Influence": [
                                            {
                                                "Expiration date": globe.date + timedelta(days=30)
                                            }
                                        ]
                                    })
                                    self.political_power -= 10
                                    break

        elif action == "worsen relations":
            chance = random.randrange(1, 40)
            if chance % 6 == 4:
                for worsening in self.worsening_relations:
                    if foreign_nation.name in worsening['nation name']:
                        worsening['duration'] += timedelta(days=20)
                        break

                    else:
                        if len(self.worsening_relations) < 10:
                            if not network.has_edge(self.name, foreign_nation.name):
                                network.add_edge(self.name, foreign_nation.name)

                            self.worsening_relations.append({
                                "nation name": foreign_nation.name,
                                "duration": globe.date + timedelta(days=20)
                            })
                            self.political_power -= 10
                            self.political_exponent -= 0.15
                            break

        elif action == "spark fascist protests":
            chance = random.randrange(1, 40)
            if chance % 6 == 4:
                foreign_nation.political_decision({
                    "Issue": "far-right protest"
                })

    def fascist_international_decision(self, globe, network, user_nation):
        for foreign_nation in globe.nations:
            if self.name == foreign_nation.name or user_nation.name == foreign_nation.name:
                continue

            else:
                if self.political_power >= 10:

                    if f"Challenge {foreign_nation.name}" in self.objectives["objectives"][0]['foreign']:
                        self.fascist_decisions_enemies(globe, network, foreign_nation)

                    elif (f"Establish ties with {foreign_nation.name}" or f"Improve relations with {foreign_nation.name}" in
                          self.objectives["objectives"][0]['foreign']):
                        self.fascist_decisions_allies(globe, network, foreign_nation)

    def communist_decisions_allies(self, globe, network, foreign_nation):
        potential_actions = ["Form alliance", "Increase exports", "Increase imports", "Guarantee independence",
                             "Improve relations"]
        action = potential_actions[random.randrange(0, len(potential_actions))]

        if action == "Form alliance":
            # action generated to form alliance
            for relations in self.foreign_relations['foreign relations']:
                # searching through nation's foreign relations
                if relations['nation name'] == foreign_nation.name:
                    # checking if foreign nation name equal to foreign nation name
                    for nations in foreign_nation.foreign_relations['foreign relations']:
                        # searching through nations in foreign nation's foreign relations
                        if self.name == nations['nation name']:
                            # checking if nation's name is equal to nation in foreign nation's foreign relations
                            if "" not in relations['alliance'] and "" in nations["alliance"]:
                                nations['alliance'] = relations['alliance']

                            elif "" in relations['alliance'] and "" not in nations['alliance']:
                                relations['alliance'] = nations['alliance']

                            else:
                                pass

        elif action == "Increase exports":
            self.exports += 25
            foreign_nation.imports += 25

        elif action == "Increase imports":
            self.imports += 25
            foreign_nation.exports += 25

        elif action == "Guarantee independence":
            for relations in self.foreign_relations['foreign relations']:
                if relations['nation name'] == foreign_nation.name:
                    if not relations['guaranteeing independence']:
                        relations['guaranteeing independence'] = True

                        if not network.has_edge(self.name, foreign_nation.name):
                            network.add_edge(self.name, foreign_nation.name)

        elif action == "Improve relations":
            for nation in self.improving_relations:
                if foreign_nation.name in nation['nation name']:
                    nation['duration'] += timedelta(days=20)

                else:
                    if len(self.improving_relations) < 10:
                        if not network.has_edge(self.name, foreign_nation.name):
                            network.add_edge(self.name, foreign_nation.name)
                            self.improving_relations.append({"nation name": foreign_nation.name,
                                                             "duration": globe.date + timedelta(days=20)})

    def communist_decisions_enemies(self, globe, network, foreign_nation):
        potential_actions = ["incursion into sphere of influence", "worsen relations", "embargo",
                             "spark communist protests"]

        action = potential_actions[random.randrange(0, len(potential_actions))]

        if action == "incursion into sphere of influence":
            for allies in range(0, len(foreign_nation.foreign_relations['foreign relations'])):
                # searching through foreign nation's list of foreign relations
                if "ally" or "friend" in foreign_nation.foreign_relations['foreign relations'][allies][
                    'relation status']:

                    for potential_ally in globe.nations:
                        if potential_ally.name == foreign_nation.foreign_relations['foreign relations'][allies][
                            'nation name'] and ("Communist" or "Socialist") not in potential_ally.political_typology:
                            # checking if nation name matches with ally name and that ally is not democratic
                            for foreign_memories in potential_ally.long_term_memory["Foreign influence"]:
                                if not "Far right Influence" in foreign_memories:
                                    potential_ally.long_term_memory["Foreign influence"].append({
                                        "Far left Influence": [
                                            {
                                                "Expiration date": globe.date + timedelta(days=30)
                                            }
                                        ]
                                    })
                                    self.political_power -= 10
                                    break

        elif action == "worsen relations":
            chance = random.randrange(1, 40)
            if chance % 6 == 4:
                for worsening in self.worsening_relations:
                    if foreign_nation.name in worsening['nation name']:
                        worsening['duration'] += timedelta(days=20)
                        break

                    else:
                        if len(self.worsening_relations) < 10:
                            if not network.has_edge(self.name, foreign_nation.name):
                                network.add_edge(self.name, foreign_nation.name)

                            self.worsening_relations.append({
                                "nation name": foreign_nation.name,
                                "duration": globe.date + timedelta(days=20)
                            })
                            self.political_power -= 10
                            self.political_exponent -= 0.15
                            break

        elif action == "spark communist protests":
            chance = random.randrange(1, 40)
            if chance % 6 == 4:
                foreign_nation.political_decision({
                    "Issue": "far-left protest"
                })

    def communist_international_decision(self, globe, network, user_nation):
        for foreign_nation in globe.nations:
            if self.name == foreign_nation.name or user_nation.name == foreign_nation.name:
                continue

            else:
                if self.political_power >= 10:

                    if f"Challenge {foreign_nation.name}" in self.objectives["objectives"][0]['foreign']:
                        self.communist_decisions_enemies(globe, network, foreign_nation)

                    elif (f"Establish ties with {foreign_nation.name}" or f"Improve relations with {foreign_nation.name}" in
                          self.objectives["objectives"][0]['foreign']):
                        self.communist_decisions_allies(globe, network, foreign_nation)
    def population_decision(self, domestic_issue):
        if len(self.long_term_memory['Domestic decisions'][0]["Population Decisions"]) > 0:
            # checking if long term memory for population decisions is larger then 0
            if domestic_issue.values() == "extreme growth":
                if "Fascism" or "Communism" in self.political_typology:
                    if self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                        'Extreme population growth occurred'][1]['Number of occurrences'] > 10 and (
                            not "Slow down population growth"
                                in self.objectives['objectives'][0]['domestic objectives'][0]['population objectives']):

                        self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'].clear()

                        self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'].append(
                            "Slow down population growth")

                        if self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Enhancer"]:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Enhancer"] = False

                    if self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                        'Extreme population growth occurred'][1]['Number of occurrences'] > 15:

                        if not self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Control"]:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Control"] = True

                        self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                            'Extreme population growth occurred'][1]['Number of occurrences'] = 0
                else:

                    if self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                        'Extreme population growth occurred'][1]['Number of occurrences'] > 4:
                        self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'].clear()

                        self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'].append(
                            "Slow down population growth")

                        if self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Enhancer"]:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Enhancer"] = False

                    if self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                        'Extreme population growth occurred'][1]['Number of occurrences'] > 6:

                        if not self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Control"]:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Control"] = True

                        self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                            'Extreme population growth occurred'][1]['Number of occurrences'] = 0

            elif domestic_issue.values() == "stable growth":
                if "Fascism" or "Communism" in self.political_typology:
                    if (self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                        'Stable population growth occurred'][1]['Number of occurrences'] > 6 and (
                            not 'Increase population growth' in
                                self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'])):
                        # checking if stable population growth over 6 times and increase population growth has not become
                        # an objective

                        self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'].clear()

                        self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'].append(
                            "Increase population growth")
                        # implementing objective of increased population growth

                        if self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Control"]:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Control"] = False

                    if self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                        'Stable population growth occurred'][1]['Number of occurrences'] > 8:
                        # checking if stable population growth over 8 times

                        if not self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Enhancer"]:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Enhancer"] = True
                            # birth enhancer implemented if population doesn't grow fast enough

                        self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                            'Low population growth occurred'][1]['Number of occurrences'] = 0

                else:
                    if (self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                        'Stable population growth occurred'][1]['Number of occurrences'] > 12 and (
                            not 'Increase population growth' in
                                self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'])):
                        # checking if stable population growth over 6 times and increase population growth has not become
                        # an objective

                        self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'].clear()

                        self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'].append(
                            "Increase population growth")
                        # implementing objective of increased population growth

                        if self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Control"]:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Control"] = False

                    if self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                        'Stable population growth occurred'][1]['Number of occurrences'] > 18:
                        # checking if stable population growth over 8 times

                        if not self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Enhancer"]:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Enhancer"] = True
                            # birth enhancer implemented if population doesn't grow fast enough

                        self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                            'Low population growth occurred'][1]['Number of occurrences'] = 0

            elif domestic_issue.values() == "insignificant growth":
                if "Fascism" or "Communism" in self.political_typology:
                    if self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                        'Low population growth occurred'][1]['Number of occurrences'] > 2:
                        # checking if low growth has occurred more than twice
                        self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'].clear()

                        self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'].append(
                            "Increase population growth")

                        if self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Control"]:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Control"] = False

                    elif self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                        'Low population growth occurred'][1]['Number of occurrences'] > 4:
                        # checking if low growth has occurred more than 4 times

                        if not self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Enhancer"]:
                            # implementing birth enhancer
                            self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Enhancer"] = True

                        self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                            'Low population growth occurred'][1]['Number of occurrences'] = 0

                else:
                    if self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                        'Low population growth occurred'][1]['Number of occurrences'] > 5:
                        # checking if low growth has occurred more than twice
                        self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'].clear()

                        self.objectives['objectives'][0]['domestic objectives'][0]['population objectives'].append(
                            "Increase population growth")

                        if self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Control"]:
                            self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Control"] = False

                    elif self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                        'Low population growth occurred'][1]['Number of occurrences'] > 9:
                        # checking if low growth has occurred more than 4 times

                        if not self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Enhancer"]:
                            # implementing birth enhancer
                            self.national_policy["Policy"][0]["Domestic Policy"][0]['Population'][0]["Birth Enhancer"] = True

                        self.long_term_memory["Domestic Decisions"][0]['Population Decisions'][0][
                            'Low population growth occurred'][1]['Number of occurrences'] = 0

        else:
            if domestic_issue.values() == "extreme growth":
                self.long_term_memory["Domestic Decisions"][0]['Population Decisions'].append(
                    {"Extreme population growth occurred": [
                        {"Action Taken": "No action"},
                        {"Number of occurrences": 1}
                    ]})

            elif domestic_issue.values() == "insignificant growth":
                self.long_term_memory["Domestic Decisions"][0]['Population Decisions'].append({"low population growth occurred": [
                    {"Action Taken": "No action"},
                    {"Number of occurrences": 1}
                ]})

            elif domestic_issue.values() == "stable growth":
                self.long_term_memory["Domestic Decisions"][0]['Population Decisions'].append(
                    {"stable population growth occurred": [
                        {"Action Taken": "No action"},
                        {"Number of occurrences": 1}
                    ]})

    def check_population_growth(self):
        if self.year_placeholder < self.date.year:
            """checking to see if an entire year has passed"""
            population_calculation = ((self.population - self.past_population) /
                                      ((self.population + self.past_population) / 2)) * 100

            if population_calculation <= 1.5:
                if len(self.long_term_memory["Domestic decisions"][0]['Population Decisions']) > 0:
                    self.long_term_memory["Domestic decisions"][0]['Population Decisions'][0][
                        'Low population growth occurred'][1]['Number of occurrences'] += 1
                self.population_decision({"population issue": "insignificant growth"})

            elif population_calculation >= 7.6:
                if len(self.long_term_memory["Domestic decisions"][0]['Population Decisions']) > 0:
                    self.long_term_memory["Domestic decisions"][0]['Population Decisions'][0][
                        'Extreme population growth occurred'][1]['Number of occurrences'] += 1
                self.population_decision({"population issue": "extreme growth"})

            else:
                if len(self.long_term_memory["Domestic decisions"][0]['Population Decisions']) > 0:
                    self.long_term_memory["Domestic decisions"][0]['Population Decisions'][0][
                        'Stable population growth occurred'][1]['Number of occurrences'] += 1
                self.population_decision({"population issue": "stable growth"})

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

    def democratic_handling_protest(self, political_issue):
        # function handles how democracies approach protests of different ideologies
        days = random.randrange(10, 30)
        if (self.national_policy["Policy"][0]["Domestic Policy"][2][
            "Political stability"] > self.long_term_memory["Domestic Decisions"][0]["Political Decisions"][1][
            'Current stability']):
            for objective in range(0, len(self.objectives[0]["domestic objectives"])):
                """iterating through current objectives"""
                for past_objective in range(0, len(
                        self.long_term_memory['Domestic decisions'][0]["Political Decisions"][0]['protest']
                        [3]['Current political objective'])):
                    """iterating through objectives within past decisions"""
                    if (self.objectives[0]["domestic objectives"][objective] ==
                            self.long_term_memory['Domestic decisions'][0]["Political Decisions"][0]['protest']
                            [3]['Current political objective'][past_objective]):
                        """Checking if current objective matches with past objective"""
                        if political_issue.values() == "Fascist protest":
                            """Checking if fascist protest"""
                            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Right"]:
                                """Checking if nation is still suppressing far right"""
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-Right protests"][0]["Dates"][1][
                                    "End date"] += timedelta(days=days)

                            else:
                                self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Right"] = True
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-Right protests"].append(
                                    {"Dates": [
                                        {"Start date": self.date},
                                        {"End date": self.date + timedelta(days=days)}
                                    ]})

                        elif political_issue.values() == "Communist protest":
                            """Checking if far left protest"""
                            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Left"]:
                                """Checking if nation is still suppressing far left"""
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-Left protests"][0]["Dates"][1][
                                    "End date"] += timedelta(days=days)

                            else:
                                self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Left"] = True
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-Left protests"].append(
                                    {"Dates": [
                                        {"Start date": self.date},
                                        {"End date": self.date + timedelta(days=days)}
                                    ]})

                        elif political_issue.values() == "Autocratic protest":
                            """Checking if autocrat protest"""
                            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Autocrats"]:
                                """Checking if nation is still suppressing far left"""
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Autocrat protests"][0]["Dates"][1][
                                    "End date"] += timedelta(days=days)

                            else:
                                self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Autocrats"] = True
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Autocrat protests"].append(
                                    {"Dates": [
                                        {"Start date": self.date},
                                        {"End date": self.date + timedelta(days=days)}
                                    ]})

                    else:
                        if "Arrest dissidents" in self.objectives["objectives"][0]['domestic objectives']:
                            pass
                        elif "Eliminate dissidents" in self.objectives["objectives"][0]['domestic objectives']:
                            pass

    def communist_handling_protest(self, political_issue):
        days = random.randrange(10, 30)
        if (self.national_policy["Policy"][0]["Domestic Policy"][2][
            "Political stability"] > self.long_term_memory["Domestic Decisions"][0]["Political Decisions"][1][
            'Current stability']):
            for objective in range(0, len(self.objectives[0]["domestic objectives"])):
                """iterating through current objectives"""
                for past_objective in range(0, len(
                        self.long_term_memory['Domestic decisions'][0]["Political Decisions"][0]['protest']
                        [3]['Current political objective'])):
                    """iterating through objectives within past decisions"""
                    if (self.objectives[0]["domestic objectives"][objective] ==
                            self.long_term_memory['Domestic decisions'][0]["Political Decisions"][0]['protest']
                            [3]['Current political objective'][past_objective]):
                        """Checking if current objective matches with past objective"""
                        if political_issue.values() == "Fascist protest":
                            """Checking if fascist protest"""
                            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Right"]:
                                """Checking if nation is still suppressing far right"""
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-Right protests"][0]["Dates"][1][
                                    "End date"] += timedelta(days=days)

                            else:
                                self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Right"] = True
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-Right protests"].append(
                                    {"Dates": [
                                        {"Start date": self.date},
                                        {"End date": self.date + timedelta(days=days)}
                                    ]})

                        elif political_issue.values() == "Liberal protest":
                            """Checking if far left protest"""
                            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Liberals"]:
                                """Checking if nation is still suppressing far left"""
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Liberal protests"][0]["Dates"][1][
                                    "End date"] += timedelta(days=days)

                            else:
                                self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Liberals"] = True
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Liberal protests"].append(
                                    {"Dates": [
                                        {"Start date": self.date},
                                        {"End date": self.date + timedelta(days=days)}
                                    ]})

                        elif political_issue.values() == "Autocratic protest":
                            """Checking if autocrat protest"""
                            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Autocrats"]:
                                """Checking if nation is still suppressing far left"""
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Autocrat protests"][0]["Dates"][1][
                                    "End date"] += timedelta(days=days)

                            else:
                                self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Autocrats"] = True
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Autocrat protests"].append(
                                    {"Dates": [
                                        {"Start date": self.date},
                                        {"End date": self.date + timedelta(days=days)}
                                    ]})

    def fascist_handling_protest(self, political_issue):
        days = random.randrange(10, 30)
        if (self.national_policy["Policy"][0]["Domestic Policy"][2][
            "Political stability"] > self.long_term_memory["Domestic Decisions"][0]["Political Decisions"][1][
            'Current stability']):
            for objective in range(0, len(self.objectives[0]["domestic objectives"])):
                """iterating through current objectives"""
                for past_objective in range(0, len(
                        self.long_term_memory['Domestic decisions'][0]["Political Decisions"][0]['protest']
                        [3]['Current political objective'])):
                    """iterating through objectives within past decisions"""
                    if (self.objectives[0]["domestic objectives"][objective] ==
                            self.long_term_memory['Domestic decisions'][0]["Political Decisions"][0]['protest']
                            [3]['Current political objective'][past_objective]):
                        """Checking if current objective matches with past objective"""
                        if political_issue.values() == "Communist protest":
                            """Checking if fascist protest"""
                            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Left"]:
                                """Checking if nation is still suppressing far right"""
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-left protests"][0]["Dates"][1][
                                    "End date"] += timedelta(days=days)

                            else:
                                self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Left"] = True
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-left protests"].append(
                                    {"Dates": [
                                        {"Start date": self.date},
                                        {"End date": self.date + timedelta(days=days)}
                                    ]})

                        elif political_issue.values() == "Liberal protest":
                            """Checking if far left protest"""
                            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Liberals"]:
                                """Checking if nation is still suppressing far left"""
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Liberal protests"][0]["Dates"][1][
                                    "End date"] += timedelta(days=days)

                            else:
                                self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Liberals"] = True
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Liberal protests"].append(
                                    {"Dates": [
                                        {"Start date": self.date},
                                        {"End date": self.date + timedelta(days=days)}
                                    ]})

                        elif political_issue.values() == "Autocratic protest":
                            """Checking if autocrat protest"""
                            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Autocrats"]:
                                """Checking if nation is still suppressing far left"""
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Autocrat protests"][0]["Dates"][1][
                                    "End date"] += timedelta(days=days)

                            else:
                                self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Autocrats"] = True
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Autocrat protests"].append(
                                    {"Dates": [
                                        {"Start date": self.date},
                                        {"End date": self.date + timedelta(days=days)}
                                    ]})

    def autocrat_handling_protest(self, political_issue):
        days = random.randrange(10, 30)
        if (self.national_policy["Policy"][0]["Domestic Policy"][2][
            "Political stability"] > self.long_term_memory["Domestic Decisions"][0]["Political Decisions"][1][
            'Current stability']):
            for objective in range(0, len(self.objectives[0]["domestic objectives"])):
                """iterating through current objectives"""
                for past_objective in range(0, len(
                        self.long_term_memory['Domestic decisions'][0]["Political Decisions"][0]['protest']
                        [3]['Current political objective'])):
                    """iterating through objectives within past decisions"""
                    if (self.objectives[0]["domestic objectives"][objective] ==
                            self.long_term_memory['Domestic decisions'][0]["Political Decisions"][0]['protest']
                            [3]['Current political objective'][past_objective]):
                        """Checking if current objective matches with past objective"""
                        if political_issue.values() == "Communist protest":
                            """Checking if fascist protest"""
                            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Left"]:
                                """Checking if nation is still suppressing far right"""
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-left protests"][0]["Dates"][1][
                                    "End date"] += timedelta(days=days)

                            else:
                                self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Left"] = True
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-left protests"].append(
                                    {"Dates": [
                                        {"Start date": self.date},
                                        {"End date": self.date + timedelta(days=days)}
                                    ]})

                        elif political_issue.values() == "Liberal protest":
                            """Checking if far left protest"""
                            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Liberals"]:
                                """Checking if nation is still suppressing far left"""
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Liberal protests"][0]["Dates"][1][
                                    "End date"] += timedelta(days=days)

                            else:
                                self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Liberals"] = True
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Liberal protests"].append(
                                    {"Dates": [
                                        {"Start date": self.date},
                                        {"End date": self.date + timedelta(days=days)}
                                    ]})

                        elif political_issue.values() == "Autocratic protest":
                            """Checking if autocrat protest"""
                            if self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Autocrats"]:
                                """Checking if nation is still suppressing far left"""
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Autocrat protests"][0]["Dates"][1][
                                    "End date"] += timedelta(days=days)

                            else:
                                self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Autocrats"] = True
                                self.national_policy["Policy"][0]["Domestic Policy"][1]["Autocrat protests"].append(
                                    {"Dates": [
                                        {"Start date": self.date},
                                        {"End date": self.date + timedelta(days=days)}
                                    ]})

    def political_decision(self, political_issue):
        if len(self.long_term_memory['Domestic decisions'][0]["Political Decisions"]) > 0:
            if "Democratic" or "Republicanism" in self.political_typology:
                # checking if current typology is liberal
                self.democratic_handling_protest(political_issue)

            elif "Communist" or "Socialism" in self.political_typology:
                # checking if current typology is Far-left
                self.communist_handling_protest(political_issue)

            elif "Autocratic" in self.political_typology:
                # checking if current typology is autocratic
                self.autocrat_handling_protest(political_issue)

            elif "Fascist" or "Nazism" in self.political_typology:
                # checking if current typology is far-right
                self.fascist_handling_protest(political_issue)

        else:
            days = random.randrange(10, 30)
            if political_issue.values() == "Fascist protest" and ("Fascist" or "Nazism" not in self.political_typology):

                # only option for any ideology within this path is to maintain stability
                if "Maintain stability" in self.objectives["objectives"][0]["domestic objectives"]:
                    self.long_term_memory["Domestic decisions"][0]["Political Decisions"].append({"protest": [
                        {"Decision": "Arrested far-right leaders"},
                        {"Effects": ["Decreased stability", "Began crack down on far-right parties"]},
                        {"Current stability": self.national_policy["Policy"][0]["Domestic Policy"][2][
                            "Political stability"]},
                        {"Current political objective": "Maintain stability"}
                    ]})
                    self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Right"] = True
                    self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-Right protests"].append({"Dates": [
                        {"Start date": self.date},
                        {"End date": self.date + timedelta(days=days)}
                    ]})

            elif political_issue.values() == "Liberal protest" and (
                    "Democratic" or "Republicanism" not in self.political_typology):
                if "Maintain stability" in self.objectives["objectives"][0]["domestic"]:
                    self.long_term_memory["Domestic decisions"][0]["Political Decisions"].append({"protest": [
                        {"Decision": "Arrested liberal leaders"},
                        {"Effects": ["Decreased stability", "Began crack down on liberal parties"]},
                        {"Current stability": self.national_policy["Policy"][0]["Domestic Policy"][2]["Political stability"]},
                        {"Current political objective": "Maintain stability"}
                    ]})
                    self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Liberals"] = True
                    self.national_policy["Policy"][0]["Domestic Policy"][1]["Liberal protests"].append({"Dates": [
                        {"Start date": self.date},
                        {"End date": self.date + timedelta(days=days)}
                    ]})

            elif political_issue.values() == "Communist protest" and ("Communist" or "Socialist" not in self.political_typology):
                if "Maintain stability" in self.objectives["objectives"][0]["domestic"]:
                    self.long_term_memory["Domestic decisions"][0]["Political Decisions"].append({"protest": [
                        {"Decision": "Arrested far-left leaders"},
                        {"Effects": ["Decreased stability", "Began crack down on far-left parties"]},
                        {"Current stability": self.national_policy["Policy"][0]["Domestic Policy"][2]["Political stability"]},
                        {"Current political objective": "Maintain stability"}
                    ]})

                    self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Far-Left"] = True
                    self.national_policy["Policy"][0]["Domestic Policy"][1]["Far-Left protests"].append({"Dates": [
                        {"Start date": self.date},
                        {"End date": self.date + timedelta(days=days)}
                    ]})

            elif political_issue.values() == "Autocratic protest" and "Autocratic" not in self.political_typology:
                if "Maintain stability" in self.objectives["objectives"][0]["domestic"]:
                    self.long_term_memory["Domestic decisions"][0]["Political Decisions"].append({"protest": [
                        {"Decision": "Arrested autocratic leaders"},
                        {"Effects": ["Decreased stability", "Began crack down on autocratic parties"]},
                        {"Current stability": self.national_policy["Policy"][0]["Domestic Policy"][2][
                            "Political stability"]},
                        {"Current political objective": "Maintain stability"}
                    ]})

                    self.national_policy["Policy"][0]["Domestic Policy"][0]["Suppress Autocrats"] = True
                    self.national_policy["Policy"][0]["Domestic Policy"][1]["Autocrat protests"].append({"Dates": [
                        {"Start date": self.date},
                        {"End date": self.date + timedelta(days=days)}
                    ]})

    def protests(self):
        """Protests will only occur if political stability drops below 75% or economic stability drops below 65%"""
        if (self.national_policy["Policy"][0]["Domestic Policy"][0]["Political"][2]["Political stability"] >= 75.00 or
                self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Economic stability"] >= 65.00):
            """protests occurring in relative peaceful and stable times"""
            number = random.randrange(1, 101)
            if number % 9 == 5 or number % 6 == 4:
                """chance, based upon remainder of 0 or 4 that fascist protest will occur with relative stability"""
                print("fascism")
                self.political_decision({"Issue": "Fascist protest"})

            if number % 3 == 2 or number % 7 == 5:
                """chance, based upon remainder of 1 or 2 that liberal protest will occur with relative stability"""
                print('liberalism')
                self.political_decision({"Issue": "Liberal protest"})

            if number % 7 == 6 or number % 9 == 7:
                """chance, based upon remainder of 5 or 7 that liberal protest will occur with relative stability"""
                print('communism')
                self.political_decision({"Issue": "Communist protest"})

            if number % 10 == 2 or number % 12 == 7:
                """chance, based upon remainder of 6 or 8 that liberal protest will occur with relative stability"""
                print('autocratic')
                self.political_decision({"Issue": "Autocratic protest"})

        if (self.national_policy["Policy"][0]["Domestic Policy"][0]["Political"][2]["Political stability"] < 75.00 or
                self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Economic stability"] < 65.00):
            """protests occurring in relative non-peaceful times"""
            for i in range(1, 101):
                days = random.randrange(10, 31)
                number = random.randrange(1, 10)
                # lesser amount of options to be generated, creates greater possibilities of uprisings
                if number % i == 0 or number % i == 4:
                    """chance, based upon remainder of 0 or 4 fascist protest will occur with relative stability"""
                    self.political_decision({"Issue": "Fascist protest"})
                    break

                if number % i == 1 or number % i == 2:
                    """chance, based upon remainder of 1 or 2 liberal protest will occur with relative stability"""
                    self.national_policy["Policy"][0]['Domestic Policy'][0]['Political'][1]["Liberal protests"].append(
                        {"Start Date": self.date,
                         "End Date": self.date + timedelta(days=days)})
                    self.political_decision({"Issue": "Liberal protest"})
                    break

                if number % i == 5 or number % i == 7:
                    """chance, based upon remainder of 5 or 7 liberal protest will occur with relative stability"""
                    self.political_decision({"Issue": "Communist protest"})
                    break

                if number % i == 6 or number % i == 8:
                    """chance, based upon remainder of 6 or 8 that liberal protest will occur with relative stability"""
                    self.political_decision({"Issue": "Autocratic protest"})
                    break

    def political_power_growth(self):
        self.political_power += self.political_exponent

    def economic_decision(self, economic_issue, date):
        """Economic decisions based upon Objectives and policy.
        stored in long term memory for AI, if nation were to experience situation again
        """
        if self.long_term_memory['Domestic Decisions'][0]["Economic Decisions"] > 0:

            if "Continued Recession" in economic_issue.values():
                options = ["Increase corporate taxes", "Increase income taxes",
                           "Increase government spending"]
                option = options[random.randrange(0, len(options))]

                for action in range(0, len(self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'])):
                    # looping through past actions within long term memory
                    if "Continued Depression" in self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action]:
                        for potential_options in self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action][
                            "Action Taken"]:
                            # looping through actions taken from past action
                            if (option == potential_options and
                                    (self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action][
                                         "Timestamps"][
                                         -1] +
                                     timedelta(days=120) == date)):
                                # checking
                                # 1. random option equals that of the past option
                                # 2. the timestamp of the past action is 3 months earlier then current action
                                self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action][
                                    "Timestamps"].append(
                                    date)

                            else:
                                # if continued recovery not in past action
                                self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'].append(
                                    {"Continued Depression": [
                                        {"Action Taken": option},
                                        {"Time stamps": [date]}
                                    ]})

                    else:
                        # if original two constraints did not match
                        self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'].append(
                            {"Continued Depression": [
                                {"Action Taken": option},
                                {"Time stamps": [date]}
                            ]})

                    if option == "Increase government spending":
                        self.government_spending += 135

                    elif option == "Increase income taxes":
                        self.consumer_spending -= 75
                        self.government_spending += 75

                    elif option == "Increase corporate taxes":
                        self.investment -= 50
                        self.government_spending += 50


            elif "Continued Depression" in economic_issue.values():
                options = ["Decrease corporate taxes", "Decrease income taxes",
                           "Increase government spending", "Decrease worker wages"]
                option = options[random.randrange(0, len(options))]

                for action in range(0, len(self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'])):
                    # looping through past actions within long term memory
                    if "Continued Depression" in self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action]:
                        for potential_options in self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action][
                            "Action Taken"]:
                            # looping through actions taken from past action
                            if (option == potential_options and
                                    (self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action][
                                         "Timestamps"][
                                         -1] +
                                     timedelta(months=3) == date)):
                                # checking
                                # 1. random option equals that of the past option
                                # 2. the timestamp of the past action is 3 months earlier then current action
                                self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action][
                                    "Timestamps"].append(
                                    date)

                            else:
                                # if continued recovery not in past action
                                self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'].append(
                                    {"Continued Depression": [
                                        {"Action Taken": option},
                                        {"Time stamps": [date]}
                                    ]})
                    else:
                        # if original two constraints did not match
                        self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'].append(
                            {"Continued Depression": [
                                {"Action Taken": option},
                                {"Time stamps": [date]}
                            ]})

                    if option == "Decrease corporate taxes":
                        self.investment += 50

                    elif option == 'Decrease income taxes':
                        self.consumer_spending += 50

                    elif option == "Increase government spending":
                        self.government_spending += 100

                    elif option == "Decrease worker wages":
                        self.consumer_spending -= 45
                        self.investment += 45

            elif "Continued Recovery" in economic_issue.values():
                options = ["Increase income taxes", "Increase worker wages"]
                option = options[random.randrange(0, len(options))]
                for action in range(0, len(self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'])):
                    # looping through past actions within long term memory
                    if "Continued Recovery" in self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action]:
                        for potential_options in self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action][
                            "Action Taken"]:
                            # looping through actions taken from past action
                            if (option == potential_options and
                                    (self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action]["Timestamps"][
                                         -1] +
                                     timedelta(months=3) == date)):
                                # checking
                                # 1. random option equals that of the past option
                                # 2. the timestamp of the past action is 3 months earlier then current action
                                self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action]["Timestamps"].append(
                                    date)

                            else:
                                # if continued recovery not in past action
                                self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'].append(
                                    {"Continued Recovery": [
                                        {"Action Taken": option},
                                        {"Time stamps": [date]}
                                    ]})
                    else:
                        # if original two constraints did not match
                        self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'].append(
                            {"Continued Recovery": [
                                {"Action Taken": option},
                                {"Time stamps": [date]}
                            ]})


            elif "Continued Expansion" in economic_issue.values():
                options = ["Decrease government spending", "Increase income taxes",
                           "Increase corporate taxes"]
                option = options[random.randrange(0, len(options))]

                for action in range(0, len(self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'])):
                    # looping through past actions within long term memory
                    for potential_options in self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action][
                        "Action Taken"]:
                        # looping through actions taken from past action
                        if (option == potential_options and
                                (self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action]["Timestamps"][-1] +
                                 timedelta(months=3) == date)):
                            # checking
                            # 1. random option equals that of the past option
                            # 2. the timestamp of the past action is 3 months earlier then current action

                            for actions in range(0, len(self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'])):
                                # doing another search through the long term memory of economic decisions
                                if "Continued Expansion" in self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][
                                    actions]:
                                    # searching for if continued recovery in past action
                                    self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][action][
                                        "Timestamps"].append(date)
                                else:
                                    # if continued recovery not in past action
                                    self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'].append(
                                        {"Continued Expansion": [
                                            {"Action Taken": option},
                                            {"Time stamps": [date]}
                                        ]})
                        else:
                            self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'].append(
                                {"Continued Recession": [
                                    {"Action Taken": option},
                                    {"Time stamps": [date]}
                                ]})

        else:
            if "Recession started" in economic_issue.values():
                self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'].append(
                    {"Recession started": [
                        {"Action Taken": "No action"},
                        {"Time stamps": [date]}
                    ]})

            elif "Depression started":
                self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'].append(
                    {"Depression started": [
                        {"Action Taken": "No action"},
                        {"Time stamps": [date]}
                    ]})

            elif "Recovery started":
                self.long_term_memory["Domestic decisions"][0]['Economic Decisions'].append(
                    {"Recovery started": [
                        {"Action Taken": "No action"},
                        {"Time stamps": [date]}
                    ]})

            elif "Expansion started":
                self.long_term_memory["Domestic decisions"][0]['Economic Decisions'].append(
                    {"Expansion started": [
                        {"Action Taken": "No action"},
                        {"Time stamps": [date]}
                    ]})

    # economic functions
    def check_economic_growth(self, date):
        if self.date > self.economic_change_date:
            growth = ((self.current_gdp - self.past_gdp) / (self.current_gdp + self.past_gdp) / 2) * 100
            if len(self.long_term_memory["Domestic decisions"][0]['Economic Decisions']) == 0:
                if growth <= 1.95:
                    if self.e_s == EconomicState.RECOVERY or self.e_s == EconomicState.EXPANSION:
                        self.e_s = EconomicState.RECESSION
                        self.economic_decision({"Economic Issue": "Recession started"}, date)
                        self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0]['low growth occurrences'] = 1

                elif growth >= 6.95:
                    if self.e_s == EconomicState.DEPRESSION or self.e_s == EconomicState.RECESSION:
                        self.e_s = EconomicState.RECOVERY
                        self.economic_decision({"Economic Issue": "Recovery started"}, date)
                        self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0]['high growth occurrences'] = 1

            else:
                if growth <= 1.95:
                    self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0][
                        'high growth occurrences'] = 0
                    """for action in range(0, len(self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'])):
                        # looping through past actions within long term memory
                        if "Continued Depression" in self.long_term_memory["Domestic Decisions"][0]['Economic Decisions'][
                            action]:"""
                    if self.e_s == EconomicState.EXPANSION or self.e_s == EconomicState.RECOVERY:

                        self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0][
                            'low growth occurrences'] = 1
                        self.economic_decision({"Issue": "Recession started"}, date)
                        self.e_s = EconomicState.RECESSION

                    elif self.e_s == EconomicState.RECESSION:
                        self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0][
                            'low growth occurrences'] += 1

                        if self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0][
                            'low growth occurrences'] < 4:
                            self.economic_decision({"Issue": "Continued Recession"}, date)

                        if self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0][
                            'low growth occurrences'] == 4:
                            self.economic_decision({"Issue": "Depression started"}, date)
                            self.e_s = EconomicState.DEPRESSION

                        else:
                            self.economic_decision({"Issue": "Continued Depression"}, date)

                elif growth >= 6.95:
                    if self.e_s == EconomicState.RECESSION or self.e_s == EconomicState.DEPRESSION:
                        self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0][
                            'low growth occurrences'] = 0
                        self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0][
                            'high growth occurrences'] = 1
                        self.e_s = EconomicState.RECOVERY
                        self.economic_decision({"Issue": "Recovery started"}, date)

                    elif self.e_s == EconomicState.RECOVERY:
                        self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0][
                            'high growth occurrences'] += 1

                        if self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0][
                            'high growth occurrences'] < 4:
                            self.economic_decision({"Issue": "Continued Recovery"}, date)

                        if self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0][
                            'high growth occurrences'] == 4:
                            self.economic_decision({"Issue": "Expansion started"}, date)
                            self.e_s = EconomicState.EXPANSION

                        else:
                            self.economic_decision({"Issue": "Continued Expansion"}, date)

        else:
            self.check_economic_state(date)

    def check_economic_state(self, date):
        """function dealing with primary economic decisions"""

        if self.e_s == EconomicState.RECESSION or self.e_s == EconomicState.DEPRESSION:
            self.national_policy["Policy"][0]["National Policy"][0]["Economy"][1]["Economic stability"] -= 1.5
            if self.national_policy["Policy"][0]["National Policy"][0]["Economy"][1]["Economic stability"] <= 65:
                self.economic_decision({"Issue": "Low economic stability"}, date)
            self.neg_ec_growth()

        elif self.e_s == EconomicState.RECOVERY or self.e_s == EconomicState.EXPANSION:
            if ((self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Economic stability"] + 1.5) < 100):
                """Checking to see if adding of 1.5 to economic stability will exceed 100 or not"""
                self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Economic stability"] += 1.5
            self.pos_ec_growth()

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
        #1. check economic stability
        #2. check current economic state
        if self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][1]["Economic stability"] > 65:
            if self.e_s == EconomicState.RECOVERY or self.e_s == EconomicState.EXPANSION:
                if "Improve political stability" in self.objectives['objectives'][1]['domestic'][0]['political objectives']:

                    if (self.objectives['objectives'][1]['domestic'][0]['political objectives']
                    ['Improve stability']['Expiration date'][0] > globe.date):
                        if self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] + 6.5 < 100:
                            self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] += 6.5

                else:

                    if self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] + 3.5 < 100:
                        self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] += 3.5

                if "Improve happiness levels" in self.objectives['objectives'][1]['domestic'][0]['political objectives']:

                    if (self.objectives['objectives'][1]['domestic'][0]['political objectives']
                    ['Improve happiness']['Expiration date'] > globe.date):
                        if self.happiness + 7.5 < 100:
                            self.happiness += 7.5
                else:

                    if self.happiness + 4.5 < 100:
                        self.happiness += 4.5

            else:
                if "Improve political stability" in self.objectives['objectives'][1]['domestic'][0]['political objectives']:
                    if (self.objectives['objectives'][1]['domestic'][0]['political objectives']
                    ['Improve stability']['Expiration date'] > globe.date):
                        if self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2][
                            'Political stability'] + 4.5 < 100:
                            self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] += 4.5
                else:

                    if self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] - 1.5 > -100:
                        self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] -= 1.5

                if "Improve happiness levels" in self.objectives['objectives'][1]['domestic'][0]['political objectives']:

                    if (self.objectives['objectives'][1]['domestic'][0]['political objectives']
                    ['Improve happiness']['Expiration date'] > globe.date):
                        if self.happiness + 3 < 100:
                            self.happiness += 3

                else:
                    if self.happiness - 2.5 > -100:
                        self.happiness -= 2.5

        else:
            if self.e_s == EconomicState.RECOVERY or self.e_s == EconomicState.EXPANSION:

                if "Improve political stability" in self.objectives['objectives'][1]['domestic'][0]['political objectives']:

                    if (self.objectives['objectives'][1]['domestic'][0]['political objectives']
                    ['Improve stability']['Expiration date'] > globe.date):
                        if self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] + 4.5 < 100:
                            self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] += 4.5

                else:
                    if self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] + 2.5 < 100:
                        self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] += 2.5

                if "Improve happiness levels" in self.objectives['objectives'][1]['domestic'][0]['political objectives']:

                    if (self.objectives['objectives'][1]['domestic'][0]['political objectives']
                    ['Improve happiness']['Expiration date'] > globe.date):
                        if self.happiness + 5.5 < 100:
                            self.happiness += 5.5

                else:
                    if self.happiness + 2.5 < 100:
                        self.happiness += 2.5

            else:
                if "Improve political stability" in self.objectives['objectives'][1]['domestic'][0]['political objectives']:
                    if (self.objectives['objectives'][1]['domestic'][0]['political objectives']
                    ['Improve stability']['Expiration date'] > globe.date):
                        if self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2][
                            'Political stability'] + 0.5 < 100:
                            self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] += 0.5

                else:
                    if self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2][
                        'Political stability'] - 1.5 > -100:
                        self.national_policy['Policy'][0]['Domestic Policy'][0]["Political"][2]['Political stability'] -= 1.5

                if "Improve happiness levels" in self.objectives['objectives'][1]['domestic'][0]['political objectives']:
                    if (self.objectives['objectives'][1]['domestic'][0]['political objectives']
                    ['Improve happiness']['Expiration date'] > globe.date):
                        if self.happiness + 0.75 < 100:
                            self.happiness += 3

                else:
                    if self.happiness - 2.5 > -100:
                        self.happiness -= 2.5