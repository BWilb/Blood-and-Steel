import random
import time
from enum import Enum
from datetime import datetime, timedelta
import globe_relations.globe


class EconomicState(Enum):
    RECESSION = 1
    DEPRESSION = 2
    EXPANSION = 3
    RECOVERY = 4


class NationAI:
    def __init__(self):
        self.birth_enhancer = False
        self.birth_control = False

    """def population_decision(self, domestic_issue):
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
                    ]})"""

    def check_population_growth(self, population_calculation):

        """checking to see if an entire year has passed"""


        if population_calculation <= 1.5:
            self.birth_enhancer = True
            self.birth_control = False
            return self.birth_enhancer
            # self.population_decision({"population issue": "insignificant growth"})

        elif population_calculation >= 7.6:
            self.birth_control = True
            self.birth_enhancer = False

            # self.population_decision({"population issue": "extreme growth"})
            return self.birth_control

        else:
            self.birth_control = False
            self.birth_enhancer = False
            return self.birth_enhancer

    """def pop_growth(self):
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
            self.deaths += deaths"""