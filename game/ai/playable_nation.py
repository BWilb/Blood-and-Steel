import random
import time
from datetime import datetime, timedelta
from enum import Enum


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4

class PlayableNation:
    def __init__(self, globe):
        self.nation_color = (0, random.randrange(0, 255), random.randrange(0, 250))
        # general information
        self.is_chosen = False
        self.conscripting_checker = globe.date
        self.region = ""
        self.name = ""
        self.date = datetime(globe.date.year, 1, 1)
        self.population_checker = globe.date + timedelta(days=31)
        self.economic_change_date = globe.date + timedelta(days=31)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        # social factors
        """population factors"""
        self.population = 0
        self.past_population = self.population
        self.population_growth = 0
        self.births = 0
        self.deaths = 0
        # political
        self.leader = "Gregory Prescov"
        self.political_power = 100
        self.political_exponent = 1.00
        self.political_typology = "Democratic"
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
        self.coordinates = []
        self.foreign_relations = {"foreign relations": []}
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
                "Domestic Ideologies": {
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
        self.messages = {
            "messages": [
                {
                    "political": [],
                    "economic": [],
                    "social": []
                }
            ]
        }
    def beginning_objectives(self):
        self.objectives['objectives'][1]['domestic'][0]['population objectives'].append("Maintain stable population growth")
        economic_list = ['keep corporate taxes moderate', "keep income taxes moderate","maintain government spending levels", "maintain stable GDP growth",
                         "prevent national debt exceeding GDP"]
        for objective in economic_list:
            self.objectives['objectives'][1]['domestic'][0]['economic objectives'].append(objective)
        political_list = ['maintain influence of state ideology', 'maintain political stability']
        for objective in political_list:
            self.objectives['objectives'][1]['domestic'][0]['political objectives'].append(objective)

    def adding_conscription_pool(self, globe):
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

    def check_population_growth(self, globe):
        if self.population_checker < globe.date:
            # checking if population growth should be calculated
            population_calculation = ((self.population - self.past_population) /
                                      ((self.population + self.past_population) / 2)) * 100
            self.population_growth = population_calculation

            if population_calculation <= 1.5:
                if "low population growth occurred" not in self.messages['messages'][0]['social']:
                    self.messages['messages'][0]['social'].append({
                        "low population growth occurred": [
                            {"potential solutions": ['implement birth enhancer'],
                             "expiration date": globe.date + timedelta(days=30)}
                        ]
                    })

            elif population_calculation >= 7.6:
                if "high population growth occurred" not in self.messages['messages'][0]['social']:
                    self.messages['messages'][0]['social'].append({
                        "low population growth occurred": [
                            {"potential solutions": ['implement birth enhancer', "sacrifice a couple thousand people"],
                             "expiration date": globe.date + timedelta(days=30)}
                        ]
                    })
            self.population_checker = globe.date + timedelta(days=31)
            # resetting value of population checker
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

    def remove_improving_relations(self, network, nation2):
        if network.has_edge(self.name, nation2.name):
            network.remove_edge(self.name, nation2.name)

        for i in range(0, len(self.worsening_relations)):
            if nation2.name == self.improving_relations[i]:
                self.improving_relations.pop(i)

    def add_improve_relations(self, network, nation2):
        if not network.has_edge(self.name, nation2.name):
            network.add_edge(self.name, nation2.name)

        self.improving_relations.append(nation2.name)

    def add_worsening_relations(self, network, nation2):
        if not network.has_edge(self.name, nation2.name):
            network.add_edge(self.name, nation2.name)

        self.worsening_relations.append(nation2.name)

    def remove_worsening_relations(self, network, nation2):
        if network.has_edge(self.name, nation2.name):
            network.remove_edge(self.name, nation2.name)

        for i in range(0, len(self.worsening_relations)):
            if nation2.name == self.worsening_relations[i]:
                self.worsening_relations.pop(i)

    def add_embargo(self, network, nation2):
        if not network.has_edge(self.name, nation2.name):
            network.add_edge(self.name, nation2.name)

        for foreign_nation in self.foreign_relations['foreign relations']:
            if nation2.name == foreign_nation['nation'].name:
                foreign_nation['embargoed'] = True

    def remove_embargo(self, network, nation2):
        if network.has_edge(self.name, nation2.name):
            network.remove_edge(self.name, nation2.name)

        for foreign_nation in self.foreign_relations['foreign relations']:
            if nation2.name == foreign_nation['nation'].name and foreign_nation['embargoed']:
                foreign_nation['embargoed'] = False

    # economic functions
    def check_economic_state(self, globe):
        if globe.date > self.economic_change_date:
            growth = ((self.current_gdp - self.past_gdp) / (self.current_gdp + self.past_gdp) / 2) * 100
            if growth <= 1.95:
                if self.e_s == EconomicState.RECOVERY or self.e_s == EconomicState.EXPANSION:
                    self.e_s = EconomicState.RECESSION
                    if "low economic growth occurred" not in self.messages['messages'][0]['social']:
                        self.messages['messages'][0]['social'].append({
                            "low economic growth occurred": [
                                {"potential solutions": ['decrease income taxes', 'decrease corporate taxes',
                                                         "increase government spending", "increase exports"],
                                 "expiration date": globe.date + timedelta(days=10)}
                            ]
                        })
            elif growth >= 6.95:
                if self.e_s == EconomicState.DEPRESSION or self.e_s == EconomicState.RECESSION:
                    self.e_s = EconomicState.RECOVERY
                    if "high economic growth occurred" not in self.messages['messages'][0]['social']:
                        self.messages['messages'][0]['social'].append({
                            "high economic growth occurred": [
                                {"potential solutions": ['increase corporate taxes', "increase income taxes"],
                                 "expiration date": globe.date + timedelta(days=10)}
                            ]
                        })
            self.economic_change_date = globe.date + timedelta(days=31)

        else:
            if self.e_s == EconomicState.RECESSION or self.e_s == EconomicState.DEPRESSION:
                self.neg_ec_growth()

            elif self.e_s == EconomicState.RECOVERY or self.e_s == EconomicState.EXPANSION:
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
        pass

    def main(self, globe):
        while self.population > 100000:
            self.check_economic_state(globe)
            self.check_population_growth(globe)
            self.adding_conscription_pool(globe)
            self.political_power_growth()
            break