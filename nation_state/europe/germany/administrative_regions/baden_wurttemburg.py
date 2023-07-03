import random
from datetime import datetime

population = {
    "1910": 4537574,
    "1914": 4658473,
    "1918": 4424252,
    "1932": 4631225,
    "1936": 4653498,
    "1939": 4675366,

}
gdp = {
    "1910": 1185000,
    "1914": 1186975,
    "1918": 1179840,
    "1932": 1189737,
    "1936": 1200000,
    "1939": 1502280,
}

def recovery(a_l):
    if a_l.master.economic_stimulus:
        a_l.consumer_spending = round(random.uniform(10, 400), 2)
        a_l.government_spending = round(random.uniform(500, 2000), 2)
        a_l.debt += round(
            (a_l.consumer_spending + a_l.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        a_l.investment = round(random.uniform(1000, 4500), 2)
        a_l.exports = round(random.uniform(600, 1000), 2)
        a_l.imports = round(random.uniform(600, 900), 2)

        a_l.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

        a_l.master.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

    else:
        a_l.consumer_spending = round(random.uniform(10, 400), 2)
        a_l.government_spending = round(random.uniform(3000, 6000), 2)
        a_l.debt += round(
            (a_l.consumer_spending + a_l.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        a_l.investment = round(random.uniform(1000, 4000), 2)
        a_l.exports = round(random.uniform(600, 900), 2)
        a_l.imports = round(random.uniform(600, 900), 2)

        a_l.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

        a_l.master.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

def recession(a_l):
    if a_l.master.economic_stimulus:
        a_l.consumer_spending = -round(random.uniform(10, 200), 2)
        a_l.government_spending = round(random.uniform(2000, 3500), 2)
        a_l.debt += round(
            (-a_l.consumer_spending + a_l.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        a_l.investment = -round(random.uniform(200, 1200), 2)
        a_l.exports = round(random.uniform(600, 900), 2)
        a_l.imports = round(random.uniform(700, 900), 2)

        a_l.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

        a_l.master.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))
    else:
        a_l.consumer_spending = -round(random.uniform(10, 400), 2)
        a_l.government_spending = round(random.uniform(4000, 8000), 2)
        a_l.debt += round(
            (-a_l.consumer_spending + a_l.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        a_l.investment = -round(random.uniform(1000, 4000), 2)
        a_l.exports = round(random.uniform(600, 900), 2)
        a_l.imports = round(random.uniform(700, 900), 2)

        a_l.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

        a_l.master.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

def depression(a_l):
    if a_l.master.economic_stimulus:

        a_l.consumer_spending = -round(random.uniform(200, 1200), 2)
        a_l.government_spending = round(random.uniform(8000, 10000), 2)
        a_l.debt += round(
            (-a_l.consumer_spending + a_l.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        a_l.investment = -round(random.uniform(1500, 3500), 2)
        a_l.exports = round(random.uniform(600, 1500), 2)
        a_l.imports = round(random.uniform(700, 1800), 2)

        a_l.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

        a_l.master.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

    else:
        a_l.consumer_spending = -round(random.uniform(200, 1600), 2)
        a_l.government_spending = round(random.uniform(10000, 12000), 2)
        a_l.debt += round(
            (-a_l.consumer_spending + a_l.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        a_l.investment = -round(random.uniform(2000, 4000), 2)
        a_l.exports = round(random.uniform(600, 900), 2)
        a_l.imports = round(random.uniform(700, 1800), 2)

        a_l.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

        a_l.master.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

def expansion(a_l):
    if a_l.master.economic_stimulus:
        a_l.consumer_spending = round(random.uniform(200, 3200), 2)
        a_l.government_spending = round(random.uniform(2000, 5000), 2)
        a_l.debt += round(
            (a_l.consumer_spending + a_l.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        a_l.investment = round(random.uniform(2000, 6000), 2)
        a_l.exports = round(random.uniform(600, 1200), 2)
        a_l.imports = round(random.uniform(600, 900), 2)

        a_l.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

        a_l.master.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))
    else:
        a_l.consumer_spending = round(random.uniform(200, 1600), 2)
        a_l.government_spending = round(random.uniform(5000, 8000), 2)
        a_l.debt += round(
            (a_l.consumer_spending + a_l.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        a_l.investment = round(random.uniform(2000, 4000), 2)
        a_l.exports = round(random.uniform(600, 1200), 2)
        a_l.imports = round(random.uniform(600, 900), 2)

        a_l.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))

        a_l.master.current_gdp += (a_l.consumer_spending + a_l.investment + a_l.government_spending +
                                (a_l.exports - a_l.imports))


def economic_growth(a_l):
    """function determines which type of economic growth function code takes"""
    if a_l.current_date > a_l.economic_change_date:
        if a_l.current_gdp > a_l.past_gdp:

            if a_l.economic_state == "recovery":
                a_l.economic_state = "expansion"

            elif a_l.economic_state == "recession":
                a_l.economic_state = "recovery"

            elif a_l.economic_state == "depression":
                a_l.economic_state = "recession"

        elif a_l.current_gdp < a_l.past_gdp:

            if a_l.economic_state == "recovery":
                a_l.economic_state = "recession"

                choice = input(
                    "The administrative region of Baden-Wurrtemburg is requesting that you pass an economic stimulus.\n"
                    "The PBaden-Wurrtemburgian economy is starting to fail. Will you do this?: ")

                if choice.lower() == "yes" or choice.lower() == 'y':
                    a_l.master.economic_stimulus = True

                else:
                    chance = random.randrange(0, 11)
                    if chance % 6 == 0:
                        """27.27% chance that Prussian officials officiate a stimulus anyway"""
                        print("Baden-Wurrtemburgian officials decided to go around your back an establish a stimulus anyway.\n")
                        a_l.master.economic_stimulus = True

            elif a_l.economic_state == "recession":
                a_l.economic_state = "depression"

                choice = input(
                    "The administrative region of Baden-Wurrtemburg is requesting that you pass an economic stimulus.\n"
                    "The Baden-Wurrtemburgian economy has fallen into a depression. Will you do this?: ")

                if choice.lower() == "yes" or choice.lower() == 'y':
                    a_l.master.economic_stimulus = True

                else:
                    chance = random.randrange(0, 11)
                    if chance % 2 == 0:
                        """54.54% chance that Prussian officials officiate a stimulus anyway"""
                        print("Baden-Wurrtemburgian officials decided to go around your back an establish a stimulus anyway.\n")
                        a_l.master.economic_stimulus = True

            elif a_l.economic_state == "expansion":
                a_l.economic_state = "recovery"

    else:
        if a_l.economic_state == "recovery":
            recovery(a_l)

        if a_l.economic_state == "depression":
            depression(a_l)

        if a_l.economic_state == "recession":
            recession(a_l)

        if a_l.economic_state == "expansion":
            expansion(a_l)

"""Population growth"""
def population_growth(a_l):
    if a_l.master.subsidize_pop_growth:
        births = random.randrange(3, 10)
        deaths = random.randrange(5, 8)
        a_l.current_pop += births
        a_l.master.current_pop += (births - deaths)
        a_l.master.births += births
        a_l.master.deaths += deaths
        if a_l.master.date.year < 1933:

            for i in range(0, (births - deaths)):
                """assigning political parties to each birth"""
                chance = random.randrange(0, 3)
                if chance == 0:
                    a_l.master.center_party += 1

                elif chance == 1:
                    a_l.master.progressives += 1

                elif chance == 2:
                    a_l.master.free_conservatives += 1

        else:
            chance = random.randrange(0, 2)
            if chance == 0:
                """Chance that the births go to the Nazi party"""
                a_l.master.national_socialists += 1

            elif chance == 1:
                """Chance that the births go to the rebels"""
                a_l.master.rebels += 1

    elif a_l.master.subsidize_pop_slow:
        births = random.randrange(2, 7)
        deaths = random.randrange(5, 8)
        a_l.current_pop += births
        a_l.master.current_pop += (births - deaths)
        a_l.master.births += births
        a_l.master.deaths += deaths

        if a_l.master.date.year < 1933:

            for i in range(0, (births - deaths)):
                """assigning political parties to each birth"""
                chance = random.randrange(0, 3)
                if chance == 0:
                    a_l.master.center_party += 1

                elif chance == 1:
                    a_l.master.progressives += 1

                elif chance == 2:
                    a_l.master.free_conservatives += 1

        else:
            chance = random.randrange(0, 2)
            if chance == 0:
                """Chance that the births go to the Nazi party"""
                a_l.master.national_socialists += 1

            elif chance == 1:
                """Chance that the births go to the rebels"""
                a_l.master.rebels += 1

    else:
        births = random.randrange(3, 9)
        deaths = random.randrange(3, 9)
        a_l.current_pop += births
        a_l.master.current_pop += (births - deaths)
        a_l.master.births += births
        a_l.master.deaths += deaths

        if a_l.master.date.year < 1933:

            for i in range(0, (births - deaths)):
                """assigning political parties to each birth"""
                chance = random.randrange(0, 3)
                if chance == 0:
                    a_l.master.center_party += 1

                elif chance == 1:
                    a_l.master.progressives += 1

                elif chance == 2:
                    a_l.master.free_conservatives += 1

        else:
            chance = random.randrange(0, 2)
            if chance == 0:
                """Chance that the births go to the Nazi party"""
                a_l.master.national_socialists += 1

            elif chance == 1:
                """Chance that the births go to the rebels"""
                a_l.master.rebels += 1

class Wurttemburg:
    def __init__(self, year, master_nation):
        self.current_date = datetime(year, 1, 1)
        # administrative variables
        self.name = "Wurttemburg"
        # social variables
        self.current_pop = 0
        self.happiness = 89.45
        # economic variables
        self.government_spending = 0
        self.investment = 0
        self.consumer_spending = 0
        self.exports = 0
        self.imports = 0
        self.economic_stimulus = False
        self.economic_state = "recovery"
        # political variables
        self.stability = 76
        self.prussian_tolerance = 87.67
        self.master = master_nation