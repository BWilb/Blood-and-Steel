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
