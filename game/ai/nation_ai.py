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
                     "Extreme growth occurrences": 0.0},
                    {"Happiness": 78.56,
                     "Social rewards": 0.0}
                ],
                "Economy": [
                    {"tax rate": 15.00,
                     "government stimulus": False,
                     "low growth occurrences": 0,
                     "high growth occurrences": 0},
                    {"Economic stability": 87.56,
                     "Economic rewards": 0.0}
                ],
                "Political": [
                    {"Repress Far-Left": False,
                     "Repress Far-Right": False,
                     "Repress Autocrats": False,
                     "Repress Liberals": False},
                    {"Far-Right protests": 0,
                     "Far-Left protests": 0,
                     "Autocrat protests": 0,
                     "Liberal Protests": 0},
                    {"Political stability": 90.0,
                     "Political rewards": 0.0}
                    # for political rewards to be utilized, AI must make political decision
                    # for example if there is a far left protest and the AI handles the protest by killing everyone...
                    # then political rewards would be decreased and the action and the outcome of the action would be stored in long term
                    # memory
                ]
            }],
                "Foreign Policy": []}
        ]}

        self.objectives = {"objectives":
                               [{"foreign objectives": [],
                                 "domestic objectives": []
                                 }]
                           }
        self.long_term_memory = {
            "Domestic decisions": [
                {"Economic Decisions": [],
                 "Political Decisions": [],
                 "Social Decisions": []}
            ],
            "Foreign decisions": [
                {"allies": []},
                {"rivals": []},
                {"enemies": []}
            ]
        }
        # long term memory stores decisions made by the AI. Used by the AI as game advances, to aid in policymaking
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

        if (domestic_issue.values() == "insignificant growth" and "maintain low population growth" in
                self.objectives['objectives'][0]['domestic objectives']):
            """Checking if domestic issue is low growth in population and if one of nation's objectives is to maintain low growth"""
            self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Low growth occurrences'] += 1

            if self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Low growth occurrences'] >= 6:
                self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Birth Enhancer'] = True
                self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Low growth occurrences'] = 0

                if self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Birth control'] == True:
                    self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Birth control'] = False

                    self.long_term_memory["Domestic decisions"][0]["Social Decisions"].append({
                        "Issue": [
                            {"Low population growth": [
                                {"Decision": ["Birth control policy removed", "Birth enhancer policy implemented"]}
                            ]}
                        ]
                    })
                else:
                    self.long_term_memory["Domestic decisions"][0]["Social Decisions"].append({
                        "Issue": [
                            {"Low population growth": [
                                {"Decision": ["Birth enhancer policy implemented"]}
                            ]}
                        ]
                    })

        elif (domestic_issue.values() == "insignificant growth" and "maintain high population growth" in
              self.objectives['objectives'][0]['domestic objectives']):
            """Checking if domestic issue is low growth in population and if one of nation's objectives is to maintain high growth"""
            self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Low growth occurrences'] += 1

            if self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Low growth occurrences'] >= 2:
                self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Birth Enhancer'] = True
                self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Low growth occurrences'] = 0

                if self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Birth control'] == True:
                    self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Birth control'] = False

                    self.long_term_memory["Domestic decisions"][0]["Social Decisions"].append({
                        "Issue": [
                            {"Low population growth": [
                                {"Decision": ["Birth control policy removed", "Birth enhancer policy implemented"]}
                            ]}
                        ]
                    })
                else:
                    self.long_term_memory["Domestic decisions"][0]["Social Decisions"].append({
                        "Issue": [
                            {"Low population growth": [
                                {"Decision": ["Birth enhancer policy implemented"]}
                            ]}
                        ]
                    })

        elif (domestic_issue.values() == "extreme growth" and "maintain high population growth" in
              self.objectives['objectives'][0]['domestic objectives']):

            if (self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['high growth occurrences'] >= 5 or
                    "maintain sustainable food production" in self.objectives["domestic objectives"]):
                self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Birth Control'] = True
                self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['high growth occurrences'] = 0

                if self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Birth Enhancer']:
                    self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Birth Enhancer'] = False

                    self.long_term_memory["Domestic decisions"][0]["Social Decisions"].append({
                        "Issue": [
                            {"Extreme population growth": [
                                {"Decision": ["Implement Birth Control", "Remove Birth Enhancer"]}
                            ]}
                        ]
                    })

                else:
                    self.long_term_memory["Domestic decisions"][0]["Social Decisions"].append({
                        "Issue": [
                            {"Extreme population growth": [
                                {"Decision": ["Implement Birth Control"]}
                            ]}
                        ]
                    })

            else:
                self.long_term_memory["Domestic decisions"][0]["Social Decisions"].append({
                    "Issue": [
                        {"Extreme population growth": [
                            {"Decision": ["Do nothing"]}
                        ]}
                    ]
                })

        elif (domestic_issue.values() == "extreme growth" and "maintain low population growth" in
              self.objectives['objectives'][0]['domestic objectives']):

            if (self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['high growth occurrences'] >= 2):
                self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Birth Control'] = True
                self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['high growth occurrences'] = 0

                if self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Birth Enhancer']:
                    self.national_policy["Policy"][0]['Domestic Policy'][0]['Population'][0]['Birth Enhancer'] = False

                    self.long_term_memory["Domestic decisions"][0]["Social Decisions"].append({
                        "Issue": [
                            {"Extreme population growth": [
                                {"Decision": ["Implement Birth Control", "Remove Birth Enhancer"]}
                            ]}
                        ]
                    })

                else:
                    self.long_term_memory["Domestic decisions"][0]["Social Decisions"].append({
                        "Issue": [
                            {"Extreme population growth": [
                                {"Decision": ["Implement Birth Control"]}
                            ]}
                        ]
                    })
    def political_decision(self, political_issue):
        pass
    def economic_decision(self, economic_issue):
        """Economic decisions based upon Objectives and policy.
        stored in long term memory for AI, if nation were to experience situation again
        """
        if economic_issue.values() == ("Recession started" or "Depression started" or "Continued economic downturn"):
            """checking to see if value is off a depression that has started or is perpetuating itself"""
            if len(self.long_term_memory['Domestic decisions'][0]['Economic Decisions']):
                """checking to see if an event, similar to the current issue exists within long term memory"""
                for objective in range(0, len(self.objectives['objectives'][0]['Domestic objectives'])):
                    if objective in False:
                        pass

            else:

                if (("Maintain economic stability" or "Maintain economic hegemony")
                        in self.objectives['objectives'][0]["domestic objectives"]):

                    self.long_term_memory["Domestic decisions"][0]["Economic Decisions"].append({
                        "Issue": [
                            {f"Economic Depression occurred": [
                                {"Current Economic Objectives": ["Maintain economic stability", "Maintain economic hegemony"]},
                                {"Decision": ["Increased exports and minimized imports"]},
                                {"Effects": ["Increased national gdp", "Increased economic stability",
                                             "Hurt relations with allies", "Worsened relations with rivals"]}
                            ]}
                        ]
                    })
                    self.exports += 50
                    self.imports -= 25
                    self.national_policy["Policy"][0]["National Policy"][0]["Economy"][0]['Economic Stability'] += 1.5

                    for nation in range(0, len(self.foreign_relations['foreign relations'])):
                        if (self.foreign_relations['foreign relations'][nation]['relation status'] == "ally" or
                        self.foreign_relations['foreign relations'][nation]['relation status'] == "rival"):
                            self.foreign_relations['foreign relations'][nation]['relations'] -= 1.5

                elif (("Maintain low taxes" or "Maintain consumer confidence")
                      in self.objectives['objectives'][0]["domestic objectives"]):
                    if self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0]["low growth occurrences"] <= 3:
                        self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0]["tax rate"] -= 1.5

                        self.long_term_memory["Domestic decisions"][0]["Economic Decisions"].append({
                            "Issue": [
                                {f"Economic Depression occurred": [
                                    {"Current Economic Objectives": ["Maintain low taxes", "Maintain consumer confidence"]},
                                    {"Decision": ["Decreased taxes"]},
                                    {"Effects": ["Increased Overall happiness", "Decreased economic stability",
                                                 "Decreased political stability"]}
                                ]}
                            ]
                        })

                    else:
                        self.consumer_spending += 150
                        self.long_term_memory["Domestic decisions"][0]["Economic Decisions"].append({
                            "Issue": [
                                {f"Economic Depression occurred": [
                                    {"Decision": ["Provide stimulus money to civilians"]},
                                    {"Effects": ["Increased Overall happiness", "Decreased economic stability", "Increased national debt"]}
                                ]}
                            ]
                        })

                elif (("Increase government involvement in economy" or "seize private assets")
                      in self.objectives['objectives'][0]["domestic objectives"]):
                    if self.national_policy["Policy"][0]["Domestic Policy"][0]["Economy"][0]["low growth occurrences"] <= 4:

                        self.long_term_memory["Domestic decisions"][0]["Economic Decisions"].append({
                            "Issue": [
                                {f"Economic downturn occurred": [
                                    {"Current Economic Objectives": ["Seize private assets", "Increase government involvement in economy"]},
                                    {"Decision": ["Increased government involvement in economy"]},
                                    {"Effects": ["Increased Overall happiness", "Decreased economic stability",
                                                 "Increased national debt", "Increased government spending"]}
                                ]}
                            ]
                        })

                    else:
                        self.long_term_memory["Domestic decisions"][0]["Economic Decisions"].append({
                            "Issue": [
                                {f"Economic Depression occurred": [
                                    {"Decision": ["Private assets seized"]},
                                    {"Effects": ["Decreased Overall happiness", "Decreased economic stability",
                                                 "Increased national debt", "Increased government spending"]}
                                ]}
                            ]
                        })

                elif (("Maintain isolationist policies")
                      in self.objectives['objectives'][0]["domestic objectives"]):

                    self.long_term_memory["Domestic decisions"][0]["Economic Decisions"].append({
                        "Issue": [
                            {f"Economic Depression occurred": [
                                {"Current Economic Objectives": ["Maintain isolationist policies"]},
                                {"Decision": ["Isolationist policies implemented"]},
                                {"Effects": ["Decreased Overall happiness", "Decreased economic stability",
                                             "Decreased imports", "Decreased exports",
                                             "Increased Political stability"]}
                            ]}
                        ]
                    })

                elif (("Enslave minorities")
                      in self.objectives['objectives'][0]["domestic objectives"]):
                    self.long_term_memory["Domestic decisions"][0]["Economic Decisions"].append({
                        "Issue": [
                            {f"Economic Depression occurred": [
                                {"Current Economic Objectives": ["Enslave minorities"]},
                                {"Decision": ["Isolationist policies implemented"]},
                                {"Effects": ["Decreased Overall happiness", "Increased economic stability",
                                             "Increased Political stability"]}
                            ]}
                        ]
                    })

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

    def check_economic_growth(self):
        if self.date > self.economic_change_date:
            growth = ((self.current_gdp - self.past_gdp) / (self.current_gdp + self.past_gdp) / 2) * 100
            if growth <= 1.95:
                if self.e_s == EconomicState.RECESSION:
                    self.e_s = EconomicState.DEPRESSION
                    self.economic_decision({"economic issue": "Depression started"})

                if self.e_s == EconomicState.RECOVERY:
                    self.e_s = EconomicState.RECESSION
                    self.economic_decision({"economic issue": "Recession started"})

                if self.e_s == EconomicState.EXPANSION:
                    self.e_s = EconomicState.RECOVERY

            elif growth >= 8.95:
                self.e_s = EconomicState.EXPANSION
                self.economic_decision({"economic issue": "extraordinary growth"})
            else:
                self.economic_decision({"economic issue": "stable growth"})
        else:
            self.check_economic_state()

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
        pass
