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
        self.year_placeholder = self.date.year
        self.economic_change_date = self.date + timedelta(days=120)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        # social factors
        """population factors"""
        self.population = 0
        self.past_population = self.population
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
                     "Repress Liberals": False},
                    {"Political stability": 90.0}
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

        self.long_term_memory = {
            "Domestic decisions":
                [
                    {"Economic Decisions": [],
                     "Political Decisions": [],
                     "Population Decisions": []}
                ],
            "Foreign decisions": [
                {"allies": []},
                {"rivals": []},
                {"enemies": []},
            ],
            "Foreign influence": [],
            "protests": [],
            "Ideologies": {
                "Democratic": 100,
                "Communist": 0,
                "Fascist": 0,
                "Autocratic": 0
            }
        }
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
        if self.year_placeholder < self.date.year:
            population_calculation = ((self.population - self.past_population) /
                                      ((self.population + self.past_population) / 2)) * 100

            if population_calculation <= 1.5:
                if "low population growth occurred" not in self.messages['messages'][0]['social']:
                    self.messages['messages'][0]['social'].append({
                        "low population growth occurred": [
                            {"potential solutions": ['implement birth enhancer'],
                             "expiration date": globe.date + timedelta(days=10)}
                        ]
                    })

            elif population_calculation >= 7.6:
                if "high population growth occurred" not in self.messages['messages'][0]['social']:
                    self.messages['messages'][0]['social'].append({
                        "low population growth occurred": [
                            {"potential solutions": ['implement birth enhancer'],
                             "expiration date": globe.date + timedelta(days=10)}
                        ]
                    })
            else:
                pass

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

    # economic functions
    def check_economic_state(self, globe):
        if self.date > self.economic_change_date:
            growth = ((self.current_gdp - self.past_gdp) / (self.current_gdp + self.past_gdp) / 2) * 100
            if growth <= 1.95:
                if self.e_s == EconomicState.RECOVERY or self.e_s == EconomicState.EXPANSION:
                    self.e_s = EconomicState.RECESSION
                    if "low economic growth occurred" not in self.messages['messages'][0]['social']:
                        self.messages['messages'][0]['social'].append({
                            "low economic growth occurred": [
                                {"potential solutions": ['implement birth enhancer'],
                                 "expiration date": globe.date + timedelta(days=10)}
                            ]
                        })
            elif growth >= 6.95:
                if self.e_s == EconomicState.DEPRESSION or self.e_s == EconomicState.RECESSION:
                    self.e_s = EconomicState.RECOVERY
                    if "high economic growth occurred" not in self.messages['messages'][0]['social']:
                        self.messages['messages'][0]['social'].append({
                            "high economic growth occurred": [
                                {"potential solutions": ['implement birth enhancer'],
                                 "expiration date": globe.date + timedelta(days=10)}
                            ]
                        })
            else:
                pass

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