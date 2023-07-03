import random
from datetime import datetime

population = {
    "1910": 6524372,
    "1914": 6850398,
    "1918": 6789583,
    "1932": 7230273,
    "1936": 7459328,
    "1939": 7645352,

}
gdp = {
    "1910": 8295000,
    "1914": 8308825,
    "1918": 8258880,
    "1932": 8328162,
    "1936": 8400000,
    "1939": 1051596,
}

def recovery(bavaria):
    if bavaria.master.economic_stimulus:
        bavaria.consumer_spending = round(random.uniform(10, 400), 2)
        bavaria.government_spending = round(random.uniform(500, 2000), 2)
        bavaria.debt += round(
            (bavaria.consumer_spending + bavaria.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        bavaria.investment = round(random.uniform(1000, 4500), 2)
        bavaria.exports = round(random.uniform(600, 1000), 2)
        bavaria.imports = round(random.uniform(600, 900), 2)

        bavaria.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

        bavaria.master.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

    else:
        bavaria.consumer_spending = round(random.uniform(10, 400), 2)
        bavaria.government_spending = round(random.uniform(3000, 6000), 2)
        bavaria.debt += round(
            (bavaria.consumer_spending + bavaria.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        bavaria.investment = round(random.uniform(1000, 4000), 2)
        bavaria.exports = round(random.uniform(600, 900), 2)
        bavaria.imports = round(random.uniform(600, 900), 2)

        bavaria.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

        bavaria.master.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

def recession(bavaria):
    if bavaria.master.economic_stimulus:
        bavaria.consumer_spending = -round(random.uniform(10, 200), 2)
        bavaria.government_spending = round(random.uniform(2000, 3500), 2)
        bavaria.debt += round(
            (-bavaria.consumer_spending + bavaria.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        bavaria.investment = -round(random.uniform(200, 1200), 2)
        bavaria.exports = round(random.uniform(600, 900), 2)
        bavaria.imports = round(random.uniform(700, 900), 2)

        bavaria.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

        bavaria.master.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))
    else:
        bavaria.consumer_spending = -round(random.uniform(10, 400), 2)
        bavaria.government_spending = round(random.uniform(4000, 8000), 2)
        bavaria.debt += round(
            (-bavaria.consumer_spending + bavaria.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        bavaria.investment = -round(random.uniform(1000, 4000), 2)
        bavaria.exports = round(random.uniform(600, 900), 2)
        bavaria.imports = round(random.uniform(700, 900), 2)

        bavaria.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

        bavaria.master.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

def depression(bavaria):
    if bavaria.master.economic_stimulus:

        bavaria.consumer_spending = -round(random.uniform(200, 1200), 2)
        bavaria.government_spending = round(random.uniform(8000, 10000), 2)
        bavaria.debt += round(
            (-bavaria.consumer_spending + bavaria.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        bavaria.investment = -round(random.uniform(1500, 3500), 2)
        bavaria.exports = round(random.uniform(600, 1500), 2)
        bavaria.imports = round(random.uniform(700, 1800), 2)

        bavaria.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

        bavaria.master.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

    else:
        bavaria.consumer_spending = -round(random.uniform(200, 1600), 2)
        bavaria.government_spending = round(random.uniform(10000, 12000), 2)
        bavaria.debt += round(
            (-bavaria.consumer_spending + bavaria.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        bavaria.investment = -round(random.uniform(2000, 4000), 2)
        bavaria.exports = round(random.uniform(600, 900), 2)
        bavaria.imports = round(random.uniform(700, 1800), 2)

        bavaria.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

        bavaria.master.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))


def expansion(bavaria):
    if bavaria.master.economic_stimulus:
        bavaria.consumer_spending = round(random.uniform(200, 3200), 2)
        bavaria.government_spending = round(random.uniform(2000, 5000), 2)
        bavaria.debt += round(
            (bavaria.consumer_spending + bavaria.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        bavaria.investment = round(random.uniform(2000, 6000), 2)
        bavaria.exports = round(random.uniform(600, 1200), 2)
        bavaria.imports = round(random.uniform(600, 900), 2)

        bavaria.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

        bavaria.master.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))
    else:
        bavaria.consumer_spending = round(random.uniform(200, 1600), 2)
        bavaria.government_spending = round(random.uniform(5000, 8000), 2)
        bavaria.debt += round(
            (bavaria.consumer_spending + bavaria.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        bavaria.investment = round(random.uniform(2000, 4000), 2)
        bavaria.exports = round(random.uniform(600, 1200), 2)
        bavaria.imports = round(random.uniform(600, 900), 2)

        bavaria.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

        bavaria.master.current_gdp += (bavaria.consumer_spending + bavaria.investment + bavaria.government_spending +
                                (bavaria.exports - bavaria.imports))

def economic_growth(bavaria):
    """function determines which type of economic growth function code takes"""
    if bavaria.current_date > bavaria.economic_change_date:
        if bavaria.current_gdp > bavaria.past_gdp:

            if bavaria.economic_state == "recovery":
                bavaria.economic_state = "expansion"

            elif bavaria.economic_state == "recession":
                bavaria.economic_state = "recovery"

            elif bavaria.economic_state == "depression":
                bavaria.economic_state = "recession"

        elif bavaria.current_gdp < bavaria.past_gdp:

            if bavaria.economic_state == "recovery":
                bavaria.economic_state = "recession"

                choice = input(
                    "The administrative region of Bavaria is requesting that you pass an economic stimulus.\n"
                    "The Bavaria economy is starting to fail. Will you do this?: ")

                if choice.lower() == "yes" or choice.lower() == 'y':
                    bavaria.master.economic_stimulus = True

                else:
                    chance = random.randrange(0, 11)
                    if chance % 6 == 0:
                        """27.27% chance that Prussian officials officiate a stimulus anyway"""
                        print("Bavarian officials decided to go around your back an establish a stimulus anyway.\n")
                        bavaria.master.economic_stimulus = True

            elif bavaria.economic_state == "recession":
                bavaria.economic_state = "depression"

                choice = input(
                    "The administrative region of Bavaria is requesting that you pass an economic stimulus.\n"
                    "The Bavarian economy has fallen into a depression. Will you do this?: ")

                if choice.lower() == "yes" or choice.lower() == 'y':
                    bavaria.master.economic_stimulus = True

                else:
                    chance = random.randrange(0, 11)
                    if chance % 2 == 0:
                        """54.54% chance that Prussian officials officiate a stimulus anyway"""
                        print("Bavarian officials decided to go around your back an establish a stimulus anyway.\n")
                        bavaria.master.economic_stimulus = True

            elif bavaria.economic_state == "expansion":
                bavaria.economic_state = "recovery"

    else:
        if bavaria.economic_state == "recovery":
            recovery(bavaria)

        if bavaria.economic_state == "depression":
            depression(bavaria)

        if bavaria.economic_state == "recession":
            recession(bavaria)

        if bavaria.economic_state == "expansion":
            expansion(bavaria)


"""Population growth"""
def population_growth(bavaria):
    if bavaria.master.subsidize_pop_growth:
        births = random.randrange(3, 10)
        deaths = random.randrange(5, 8)
        bavaria.current_pop += births
        bavaria.master.current_pop += (births - deaths)
        bavaria.master.births += births
        bavaria.master.deaths += deaths
        if bavaria.master.date.year < 1933:

            for i in range(0, (births - deaths)):
                """assigning political parties to each birth"""
                chance = random.randrange(0, 3)
                if chance == 0:
                    bavaria.master.center_party += 1

                elif chance == 1:
                    bavaria.master.progressives += 1

                elif chance == 2:
                    bavaria.master.free_conservatives += 1

        else:
            chance = random.randrange(0, 2)
            if chance == 0:
                """Chance that the births go to the Nazi party"""
                bavaria.master.national_socialists += 1

            elif chance == 1:
                """Chance that the births go to the rebels"""
                bavaria.master.rebels += 1

    elif bavaria.master.subsidize_pop_slow:
        births = random.randrange(2, 7)
        deaths = random.randrange(5, 8)
        bavaria.current_pop += births
        bavaria.master.current_pop += (births - deaths)
        bavaria.master.births += births
        bavaria.master.deaths += deaths

        if bavaria.master.date.year < 1933:

            for i in range(0, (births - deaths)):
                """assigning political parties to each birth"""
                chance = random.randrange(0, 3)
                if chance == 0:
                    bavaria.master.center_party += 1

                elif chance == 1:
                    bavaria.master.progressives += 1

                elif chance == 2:
                    bavaria.master.free_conservatives += 1

        else:
            chance = random.randrange(0, 2)
            if chance == 0:
                """Chance that the births go to the Nazi party"""
                bavaria.master.national_socialists += 1

            elif chance == 1:
                """Chance that the births go to the rebels"""
                bavaria.master.rebels += 1

    else:
        births = random.randrange(3, 9)
        deaths = random.randrange(3, 9)
        bavaria.current_pop += births
        bavaria.master.current_pop += (births - deaths)
        bavaria.master.births += births
        bavaria.master.deaths += deaths

        if bavaria.master.date.year < 1933:

            for i in range(0, (births - deaths)):
                """assigning political parties to each birth"""
                chance = random.randrange(0, 3)
                if chance == 0:
                    bavaria.master.center_party += 1

                elif chance == 1:
                    bavaria.master.progressives += 1

                elif chance == 2:
                    bavaria.master.free_conservatives += 1

        else:
            chance = random.randrange(0, 2)
            if chance == 0:
                """Chance that the births go to the Nazi party"""
                bavaria.master.national_socialists += 1

            elif chance == 1:
                """Chance that the births go to the rebels"""
                bavaria.master.rebels += 1

class Bavaria:
    def __init__(self, year, master_nation):
        self.current_date = datetime(year, 1, 1)
        # administrative variables
        self.name = "Bavaria"
        # social variables
        self.current_pop = 0
        self.births = 0
        self.deaths = 0
        self.happiness = 85.56
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